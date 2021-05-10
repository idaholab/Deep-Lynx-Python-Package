import pytest
import sys
import os
import logging
import requests
import requests_mock
import dateutil.parser
import datetime
import random_word

from deep_lynx import deep_lynx_service

class TestServiceHelpers:

    dl_service = None
    log_path = 'test.log'
    # setup logging
    # remove log file if it exists
    if os.path.exists(log_path):
        os.remove(log_path)
    
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        filename=log_path,
                        level=logging.INFO)
    logger = logging.getLogger('deep-lynx')

    # placeholder variables for env parameters
    DEEP_LYNX_URL = os.getenv('DEEP_LYNX_URL')
    CONTAINER_NAME = os.getenv('CONTAINER_NAME')
    DATA_SOURCE_NAME = os.getenv('DATA_SOURCE_NAME')

    def set_env_success(self):
        """Setup for env variables
            Test Case: Correct env variables"""
        self.DEEP_LYNX_URL = os.getenv('DEEP_LYNX_URL')
        self.CONTAINER_NAME = os.getenv('CONTAINER_NAME')
        self.DATA_SOURCE_NAME = os.getenv('DATA_SOURCE_NAME')

    def set_env_fail(self):
        """Setup for env variables
            Test Case: Invalid DEEP_LYNX_URL: Wrong port"""
        self.DEEP_LYNX_URL = 'http://127.0.0.1:1000'
        self.CONTAINER_NAME = 'DL_PY_Test'
        self.DATA_SOURCE_NAME = 'DL_PY'

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class """
        cls.logger.info('Setting up test class')
        cls.set_env_success(cls)
        cls.dl_service = deep_lynx_service.DeepLynxService(cls.DEEP_LYNX_URL, cls.CONTAINER_NAME, cls.DATA_SOURCE_NAME)

        # ensure there is a Deep Lynx connection
        try:
            resp = requests.get(cls.DEEP_LYNX_URL + '/containers?offset=0&limit=100')
        except requests.exceptions.RequestException as e:
            # cannot reach Deep Lynx, skip all tests
            cls.logger.error('RequestException: ' + str(e))
            cls.logger.error('Skipping all tests')
            pytest.xfail('Cannot reach Deep Lynx')

        # create a test container
        if cls.dl_service.check_container() == False:
            cls.dl_service.create_container({
                'name': cls.CONTAINER_NAME,
                'description': 'Test container'
            })

        # create a data source
        cls.dl_service.init()

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        cls.logger.info('Tearing down test class')
        cls.set_env_success(cls)
        if cls.dl_service.check_container() == True:
            # delete datasource
            cls.dl_service.delete_data_source(cls.dl_service.container_id,
                                            cls.dl_service.data_source_id)
            # delete container
            resp = cls.dl_service.delete_container(cls.dl_service.container_id)

    def test_connection_success(self):
        """Determine if there is a Deep Lynx connection. Skip remaining tests if a connection to Deep Lynx is not established
            Test Case: Establish a connection to Deep Lynx"""
        try:
            resp = requests.get(self.DEEP_LYNX_URL + '/containers?offset=0&limit=100')
            assert resp.ok is True
        except requests.exceptions.RequestException as e:
            pytest.fail("RequestException: " + str(e))

    def test_connection_fail(self):
        """Determine if there is a Deep Lynx connection.
            Test Case: No connection to Deep Lynx"""
        self.set_env_fail()
        with pytest.raises(requests.exceptions.RequestException):
            resp = requests.get(self.DEEP_LYNX_URL + '/containers?offset=0&limit=100')
        self.set_env_success()

    def test_init_success(self):
        """Initialize the class by ensuring there is a container and datasource
            Test Case: Valid init"""
        self.dl_service.init()
        # check if log file has correct output
        is_verified = False
        log_file = open(self.log_path, 'r')
        lines = log_file.readlines()
        for line in lines:
            if 'Successful connection to Deep Lynx container' in line:
                is_verified = True
        log_file.close()
        assert is_verified == True

    def test_import_time_success(self):
        """Create an import and verify import time is received
            Test Case: Time is returned"""
        import_result = self.dl_service.create_manual_import(
            self.dl_service.container_id,
            self.dl_service.data_source_id,
            {'test': 'Test Data'}
        )
        assert import_result['value']['id'] is not None
        import_id = import_result['value']['id']
        
        import_time = self.dl_service.get_latest_import_time()
        assert import_time is not False

        # delete import
        import_delete = self.dl_service.delete_import(
            self.dl_service.container_id,
            import_id
        )
        assert import_delete is not None

    # CONTAINERS

    def test_health(self):
        resp = self.dl_service.health()
        assert resp == 'OK'

    def test_retrieve_container(self):
        resp = self.dl_service.retrieve_container(self.dl_service.container_id)
        assert resp['value']['id'] is not None

    def test_list_containers(self):
        resp = self.dl_service.list_containers()
        assert len(resp['value']) > 0

    def test_update_container(self):
        resp = self.dl_service.update_container(
            self.dl_service.container_id,
            {
                'name': self.CONTAINER_NAME,
                'description': 'test container updated'
            }
        )
        assert resp['value']['id'] is not None

    def test_batch_update_containers(self):
        resp = self.dl_service.batch_update_containers(
            {
                'name': self.CONTAINER_NAME,
                'description': 'test container updated',
                'id': self.dl_service.container_id
            }
        )

        assert len(resp['value']) > 0

    def test_archive_container(self):
        """Also covers set_container_active and delete_container."""
        container = self.dl_service.create_container(
            {
                'name': 'archive container',
                'description': 'test container to be archived'
            }
        )
        assert container['value'][0]['id'] is not None
        container_id = container['value'][0]['id']

        resp = self.dl_service.archive_container(container_id)
        assert resp['value'] is True

        # set the container active
        container_active = self.dl_service.set_container_active(container_id)
        assert container_active['value'] is True

        container_delete = self.dl_service.delete_container(container_id)
        assert container_delete['value'] is True

    def test_import_container(self):
        resp = self.dl_service.import_container({
            'file_path': 'tests/test.owl',
            'name': 'Test_Import_Container',
            'description': 'Description for my test container'
        })
        assert resp['value'] is not None

        container_id = resp['value']
        update_resp = self.dl_service.update_import(
            container_id,
            {
                'file_path': 'tests/test.owl',
                'name': 'Test_Import_Container',
                'description': 'Description updated for my test container'
            }
        )
        assert update_resp['value'] is not None

        # cleanup container
        container_delete = self.dl_service.delete_container(container_id)
        assert container_delete is not None
        

    def test_repair_container_permissions(self):
        resp = self.dl_service.repair_container_permissions(self.dl_service.container_id)
        assert resp['value'] is True

    # DATA SOURCES

    def test_create_manual_import(self):
        """Also covers list imports for data source"""
        resp = self.dl_service.create_manual_import(
            self.dl_service.container_id,
            self.dl_service.data_source_id,
            {'test': 'test import'}
        )
        assert resp['value']['id'] is not None

        list_resp = self.dl_service.list_imports_for_data_source(
            self.dl_service.container_id,
            self.dl_service.data_source_id
        )
        assert len(list_resp['value']) > 0

    def test_list_data_sources(self):
        resp = self.dl_service.list_data_sources(self.dl_service.container_id)
        assert len(resp['value']) > 0

    def test_retrieve_data_source(self):
        resp = self.dl_service.retrieve_data_source(
            self.dl_service.container_id,
            self.dl_service.data_source_id
        )
        assert resp['value']['id'] is not None

    def test_count_unmapped_data(self):
        resp = self.dl_service.count_unmapped_data(self.dl_service.container_id)
        assert resp['isError'] is False

    def test_upload_file(self):
        """Note that the FILESYSTEM_STORAGE_DIRECTORY parameter of Deep Lynx must be set."""
        resp = self.dl_service.upload_file(
            self.dl_service.container_id,
            self.dl_service.data_source_id,
            ['tests/sample.txt']
        )
        file_id = resp[0]['value']['id']
        assert file_id is not None

        retrieve_resp = self.dl_service.retrieve_file(
            self.dl_service.container_id,
            file_id
        )
        assert retrieve_resp['isError'] is False

        download_resp = self.dl_service.download_file(
            self.dl_service.container_id,
            file_id
        )
        assert len(download_resp) > 0

    def test_update_datasource_configuration(self):
        resp = self.dl_service.update_datasource_configuration(
            self.dl_service.container_id,
            self.dl_service.data_source_id,
            {
                'name': os.getenv('DATA_SOURCE_NAME') + '_Updated'
            }
        )

        assert resp['isError'] is False

    def test_set_data_source_inactive(self):
        resp = self.dl_service.set_data_source_inactive(
            self.dl_service.container_id,
            self.dl_service.data_source_id
        )

        assert resp['value'] is True

        active_resp = self.dl_service.set_data_source_active(
            self.dl_service.container_id,
            self.dl_service.data_source_id
        )

        assert active_resp['value'] is True
