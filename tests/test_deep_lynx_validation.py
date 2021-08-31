import pytest
import os
import logging
import settings
import datetime
import json

from deep_lynx import deep_lynx_service
from validation import deep_lynx_validation


class TestDeepLynxValidation:
    dl_service = None
    log_path = 'test.log'
    # setup logging
    # remove log file if it exists
    if os.path.exists(log_path):
        os.remove(log_path)

    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename=log_path, level=logging.INFO)
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

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class """
        cls.logger.info('Setting up test class')
        cls.set_env_success(cls)
        cls.dl_service = deep_lynx_service.DeepLynxService(cls.DEEP_LYNX_URL,
                                                           cls.CONTAINER_NAME,
                                                           cls.DATA_SOURCE_NAME,
                                                           init=True)
        resp = cls.dl_service.import_container({
            'file_path': 'tests/test.owl',
            'name': 'Test_Import_Container',
            'description': 'Description for my test container',
            'data_versioning_enabled': 'false'
        })
        if resp['isError']:
            cls.logger.error(resp)
        cls.container_id = resp['value']
        cls.dl_validator = deep_lynx_validation.DeepLynxValidator(cls.dl_service)

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        cls.logger.info('Tearing down test class')
        cls.set_env_success(cls)
        if cls.dl_service.check_container() == True:
            # delete datasource
            cls.dl_service.delete_data_source(cls.dl_service.container_id, cls.dl_service.data_source_id)
            # delete container
            resp = cls.dl_service.delete_container(cls.dl_service.container_id)
        if cls.container_id:
            resp = cls.dl_service.delete_container(cls.container_id)

    def test_invalid_metatype(self):
        # Invalid metatype
        metatype = 'DataItem'
        json_data = {'id': 'data_item_id', 'name': 'data item name', 'description': 'description of data item'}
        invalid_metatype = self.dl_validator.validate_properties(metatype, json_data, self.container_id)
        invalid_metatype = json.loads(invalid_metatype)
        assert invalid_metatype['isError'] is True
        assert len(invalid_metatype['error']) > 0

    def test_invalid_property(self):
        # Invalid property
        metatype = 'Document'
        json_data = {
            'id': 'document_id',
            'name': 'document name',
            'description': 'description of document',
            'file': True,
            'file path': os.path.join('tests', 'test.owl'),
            'file size': 3.14
        }
        invalid_property = self.dl_validator.validate_properties(metatype, json_data, self.container_id)
        invalid_property = json.loads(invalid_property)
        assert invalid_property['isError'] is True
        assert len(invalid_property['error']) > 0

    def test_invalid_datatype(self):
        # Invalid datatype
        metatype = 'Equipment'
        date = datetime.datetime.utcnow().isoformat()[:-3] + 'Z'
        json_data = {
            'id': 'equipment_id',
            'name': 100,
            'description': 'description of equipment',
            'flex flag': True,
            'maintenance last performed': date
        }
        invalid_datatype = self.dl_validator.validate_properties(metatype, json_data, self.container_id)
        invalid_datatype = json.loads(invalid_datatype)
        assert invalid_datatype['isError'] is True
        assert len(invalid_datatype['error']) > 0

    def test_invalid_id(self):
        # Invalid id
        metatype = 'Note'
        date = datetime.datetime.utcnow().isoformat()[:-3]
        json_data = {'name': "Note name", 'description': 'description of note', 'creation date': date}
        invalid_id = self.dl_validator.validate_properties(metatype, json_data, self.container_id)
        invalid_id = json.loads(invalid_id)
        assert invalid_id['isError'] is True
        assert len(invalid_id['error']) > 0

    def test_valid_json(self):
        # Valid json
        metatype = 'History'
        json_data = {'id': 'history_id', 'name': 'history name'}
        valid_json = self.dl_validator.validate_properties(metatype, json_data, self.container_id)
        valid_json = json.loads(valid_json)
        print(valid_json)
        assert valid_json['isError'] is False
        assert len(valid_json['error']) == 0
