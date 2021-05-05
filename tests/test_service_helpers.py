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
            pytest.fail("RequestException: " + str(e))

        # create a test container
        if cls.dl_service.check_container() == False:
            cls.dl_service.create_container({
                'name': cls.CONTAINER_NAME,
                'description': 'Test container'
            })

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

    def test_service_init_success(self, mocker):
        """Mock that the data source is validated
            Test Case: Valid data source"""
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

