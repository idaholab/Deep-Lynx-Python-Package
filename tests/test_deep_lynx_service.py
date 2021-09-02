# Copyright 2021, Battelle Energy Alliance, LLC

import pytest
import os
import logging
import requests
import settings

from deep_lynx import deep_lynx_service


class TestDeepLynxService:

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

    def set_env_fail(self):
        """Setup for env variables
            Test Case: Invalid DEEP_LYNX_URL: Wrong port"""
        self.DEEP_LYNX_URL = 'http://127.0.0.1:1000'
        self.CONTAINER_NAME = 'DL_PY_Test'
        self.DATA_SOURCE_NAME = 'DL_PY'

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class """
        cls.logger.info('Setting up TestDeepLynxService class')
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
            cls.dl_service.create_container({'name': cls.CONTAINER_NAME, 'description': 'Test container'})

        # create a data source
        cls.dl_service.init()

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        cls.logger.info('Tearing down TestDeepLynxService class')
        cls.set_env_success(cls)
        if cls.dl_service.check_container() == True:
            # delete datasource
            cls.dl_service.delete_data_source(cls.dl_service.container_id, cls.dl_service.data_source_id,
                                              {'forceDelete': 'true'})
            # delete container
            resp = cls.dl_service.delete_container(cls.dl_service.container_id)

    def test_connection_success(self):
        """Determine if there is a Deep Lynx connection.
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
        """Initialize the class by ensuring there is a container and datasource.
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
        import_result = self.dl_service.create_manual_import(self.dl_service.container_id,
                                                             self.dl_service.data_source_id, {'test': 'Test Data'})
        assert import_result['value']['id'] is not None
        import_id = import_result['value']['id']

        import_time = self.dl_service.get_latest_import_time()
        assert import_time is not False

        # delete import
        import_delete = self.dl_service.delete_import(self.dl_service.container_id, import_id)
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
        resp = self.dl_service.update_container(self.dl_service.container_id, {
            'name': self.CONTAINER_NAME,
            'description': 'test container updated'
        })
        assert resp['value']['id'] is not None

    def test_batch_update_containers(self):
        resp = self.dl_service.batch_update_containers({
            'name': self.CONTAINER_NAME,
            'description': 'test container updated',
            'id': self.dl_service.container_id
        })

        assert len(resp['value']) > 0

    def test_archive_container(self):
        """Tests the archival of a container.
            Also covers setting a container active and deleting a container."""
        container = self.dl_service.create_container({
            'name': 'archive container',
            'description': 'test container to be archived'
        })
        assert container['value'][0]['id'] is not None
        container_id = container['value'][0]['id']

        # archive container
        resp = self.dl_service.archive_container(container_id)
        assert resp['value'] is True

        # set the container active
        container_active = self.dl_service.set_container_active(container_id)
        assert container_active['value'] is True

        # delete container
        container_delete = self.dl_service.delete_container(container_id)
        assert container_delete['value'] is True

    def test_import_container(self):
        """Uses a test ontology file to create a new container via import.
            Also updates the newly created container via import."""
        resp = self.dl_service.import_container({
            'file_path': 'tests/test.owl',
            'name': 'Test_Import_Container',
            'description': 'Description for my test container',
            'data_versioning_enabled': 'false'
        })
        assert resp['value'] is not None
        container_id = resp['value']

        # update the container via import
        update_resp = self.dl_service.update_import(
            container_id, {
                'file_path': 'tests/test.owl',
                'name': 'Test_Import_Container',
                'description': 'Description updated for my test container',
                'data_versioning_enabled': 'false'
            })
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
        resp = self.dl_service.create_manual_import(self.dl_service.container_id, self.dl_service.data_source_id,
                                                    {'test': 'test import'})
        assert resp['value']['id'] is not None

        # list imports for data source
        list_resp = self.dl_service.list_imports_for_data_source(self.dl_service.container_id,
                                                                 self.dl_service.data_source_id)
        assert len(list_resp['value']) > 0

    def test_list_data_sources(self):
        resp = self.dl_service.list_data_sources(self.dl_service.container_id)
        assert len(resp['value']) > 0

    def test_retrieve_data_source(self):
        resp = self.dl_service.retrieve_data_source(self.dl_service.container_id, self.dl_service.data_source_id)
        assert resp['value']['id'] is not None

    def test_count_unmapped_data(self):
        resp = self.dl_service.count_unmapped_data(self.dl_service.container_id)
        assert resp['isError'] is False

    def test_upload_file(self):
        """Note that the FILESYSTEM_STORAGE_DIRECTORY parameter of Deep Lynx must be set.
            Also retrieves the uploaded file and downloads it."""
        resp = self.dl_service.upload_file(self.dl_service.container_id, self.dl_service.data_source_id,
                                           ['tests/sample.txt'])

        # check for error here and log with useful message to user about DL parameter
        if resp[0]['isError']:
            self.logger.error(resp[0]['error'])
            self.logger.error('Did you set the Deep Lynx FILESYSTEM_STORAGE_DIRECTORY parameter?')

        file_id = resp[0]['value']['id']
        assert file_id is not None

        # retrieve file
        retrieve_resp = self.dl_service.retrieve_file(self.dl_service.container_id, file_id)
        assert retrieve_resp['isError'] is False

        # download file
        download_resp = self.dl_service.download_file(self.dl_service.container_id, file_id)
        assert len(download_resp) > 0

    def test_update_datasource_configuration(self):
        resp = self.dl_service.update_datasource_configuration(self.dl_service.container_id,
                                                               self.dl_service.data_source_id,
                                                               {'name': os.getenv('DATA_SOURCE_NAME') + '_Updated'})

        assert resp['isError'] is False

    def test_set_data_source_inactive(self):
        """Covers both set_data_source_inactive and set_data_source_active"""
        resp = self.dl_service.set_data_source_inactive(self.dl_service.container_id, self.dl_service.data_source_id)

        assert resp['value'] is True

        active_resp = self.dl_service.set_data_source_active(self.dl_service.container_id,
                                                             self.dl_service.data_source_id)

        assert active_resp['value'] is True

    # GRAPH & DATA QUERY

    def test_nodes(self):
        """Covers all aspects of creating, listing, and archiving nodes."""
        # create metatype
        metatype = self.dl_service.create_metatype(self.dl_service.container_id, {
            "name": "Test",
            "description": "A test metatype"
        })
        metatype_id = metatype['value'][0]['id']
        assert metatype_id is not None

        # create node
        node = self.dl_service.create_update_nodes(
            self.dl_service.container_id, {
                "container_id": self.dl_service.container_id,
                "data_source_id": self.dl_service.data_source_id,
                "metatype_id": metatype_id,
                "properties": {
                    "test property": 3
                }
            })
        assert node['isError'] is False

        # list nodes
        list_node = self.dl_service.list_nodes(self.dl_service.container_id)
        assert len(list_node['value']) > 0
        node_id = list_node['value'][0]['id']

        # retrieve node
        retrieve_node = self.dl_service.retrieve_node(self.dl_service.container_id, node_id)
        assert retrieve_node['isError'] is False

        # list nodes by metatype ID
        list_node_metatype = self.dl_service.list_nodes_by_metatype_id(self.dl_service.container_id, metatype_id)
        assert len(list_node_metatype['value']) > 0

        # query the graph to retrieve nodes
        query_graph = self.dl_service.query(self.dl_service.container_id, '{nodes {id metatype{id} archived}}')
        assert len(query_graph['data']['nodes']) > 0

        # archive node
        archive_node = self.dl_service.archive_node(self.dl_service.container_id, node_id)
        assert archive_node['isError'] is False

    def test_edges(self):
        """Covers all aspects of creating, listing, and archiving edges."""
        # create relationship
        relationship = self.dl_service.create_relationship(self.dl_service.container_id, {
            "name": "Test",
            "description": "A test relationship"
        })
        relationship_id = relationship['value'][0]['id']
        assert relationship_id is not None

        # create metatypes and nodes
        metatype = self.dl_service.create_metatype(self.dl_service.container_id, {
            "name": "Test Origin",
            "description": "A test metatype for origin node"
        })
        metatype_id = metatype['value'][0]['id']
        assert metatype_id is not None

        node_1 = self.dl_service.create_update_nodes(
            self.dl_service.container_id, {
                "container_id": self.dl_service.container_id,
                "data_source_id": self.dl_service.data_source_id,
                "metatype_id": metatype_id,
                "properties": {
                    "location": "origin"
                }
            })
        assert node_1['isError'] is False

        node_2 = self.dl_service.create_update_nodes(
            self.dl_service.container_id, {
                "container_id": self.dl_service.container_id,
                "data_source_id": self.dl_service.data_source_id,
                "metatype_id": metatype_id,
                "properties": {
                    "location": "destination"
                }
            })
        assert node_2['isError'] is False

        list_node = self.dl_service.list_nodes(self.dl_service.container_id)
        assert len(list_node['value']) > 1
        # get IDs for the last 2 nodes created
        node_id_1 = list_node['value'][len(list_node['value']) - 2]['id']
        node_id_2 = list_node['value'][len(list_node['value']) - 1]['id']

        # create relationship pair
        relationship_pair = self.dl_service.create_relationship_pair(
            self.dl_service.container_id, {
                "name": "Relationship Pair Test",
                "description": "Relationship Pair Test description",
                "origin_metatype_id": metatype_id,
                "destination_metatype_id": metatype_id,
                "relationship_id": relationship_id,
                "relationship_type": "many:many"
            })
        relationship_pair_id = relationship_pair['value'][0]['id']
        assert relationship_pair_id is not None

        # create edge
        edge = self.dl_service.create_update_edges(
            self.dl_service.container_id, {
                "container_id": self.dl_service.container_id,
                "data_source_id": self.dl_service.data_source_id,
                "origin_node_id": node_id_1,
                "destination_node_id": node_id_2,
                "relationship_pair_id": relationship_pair_id,
                "properties": {}
            })
        assert edge['isError'] is False

        # list edges
        list_edges = self.dl_service.list_edges(self.dl_service.container_id)
        assert len(list_edges['value']) > 0
        edge_id = list_edges['value'][0]['id']

        # retrieve edge
        retrieve_edge = self.dl_service.retrieve_edge(self.dl_service.container_id, edge_id)
        assert retrieve_edge['isError'] is False

        # query the graph to retrieve nodes
        query_graph = self.dl_service.query(self.dl_service.container_id, '{nodes {id metatype{id} archived}}')
        assert len(query_graph['data']['nodes']) > 0

        # archive edge
        archive_edge = self.dl_service.archive_edge(self.dl_service.container_id, edge_id)
        assert archive_edge['isError'] is False

    # IMPORTS

    def test_imports(self):
        """Covers all aspects of creating, listing, and deleting imports."""
        # create import
        import_result = self.dl_service.create_manual_import(self.dl_service.container_id,
                                                             self.dl_service.data_source_id, {'test': 'Test Data'})
        assert import_result['value']['id'] is not None
        import_id = import_result['value']['id']

        # list import data
        list_import = self.dl_service.list_import_data(self.dl_service.container_id, import_id)
        data_id = list_import['value'][0]['id']
        assert data_id is not None

        # retrieve import data
        import_data = self.dl_service.retrieve_import_data(self.dl_service.container_id, import_id, data_id)
        assert import_data['isError'] is False

        # delete import data
        delete_data = self.dl_service.delete_import_data(self.dl_service.container_id, import_id, data_id)
        assert delete_data['isError'] is False

    # EXPORTS - NOT CURRENTLY TESTED

    # def test_exports(self):
    #     # export testing requires an external service
    #     # to which deep lynx will write the data

    #     # create export
    #     data_export = self.dl_service.create_data_export(
    #         self.dl_service.container_id,
    #         {
    #             "adapter": "gremlin",
    #             "config": {
    #                 "traversal_source": "g",
    #                 "graphson_v1": False,
    #                 "user": "",
    #                 "key": "",
    #                 "endpoint": "localhost",
    #                 "port": "8182",
    #                 "path": "/gremlin",
    #                 "writes_per_second": 300
    #             }
    #         }
    #     )
    #     assert data_export['value']['id'] is not None
    #     export_id = data_export['value']['id']

    #     # retrieve data export
    #     export_data = self.dl_service.retrieve_data_export(
    #         self.dl_service.container_id,
    #         export_id
    #     )
    #     assert export_data['isError'] is False

    #     # start data export
    #     start_export = self.dl_service.start_data_export(
    #         self.dl_service.container_id,
    #         export_id
    #     )
    #     assert start_export['isError'] is False

    #     # stop data export
    #     stop_export = self.dl_service.stop_data_export(
    #         self.dl_service.container_id,
    #         export_id
    #     )
    #     assert stop_export['isError'] is False

    #     # delete data export
    #     delete_data = self.dl_service.delete_import_data(
    #         self.dl_service.container_id,
    #         export_id
    #     )
    #     assert delete_data['isError'] is False

    # EVENTS

    def test_events(self):
        """Covers all aspects of creating, listing, and deleting events."""
        # create registered event
        event = self.dl_service.create_registered_event({
            "app_name": "test app",
            "app_url": "http://localhost:8099/test",
            "container_id": self.dl_service.container_id,
            "event_type": "data_source_created"
        })
        event_id = event['value']['id']
        assert event_id is not None

        # list events
        list_events = self.dl_service.list_registered_events()
        assert len(list_events['value']) > 0

        # retrieve event
        retrieve_event = self.dl_service.retrieve_registered_event(event_id)
        assert retrieve_event['isError'] is False

        # update event
        update_event = self.dl_service.update_registered_event(
            event_id, {
                "app_name": "test app",
                "app_url": "http://localhost:8099/test_url",
                "container_id": self.dl_service.container_id,
                "event_type": "data_source_created"
            })
        assert update_event['isError'] is False

        # delete event
        delete_event = self.dl_service.delete_registered_event(event_id)
        assert delete_event['isError'] is False

    # DATA TYPE MAPPINGS

    # USERS

    def test_users(self):
        """Covers listing and retrieving users.
            Limited since Deep Lynx doesn't allow user creation via API."""
        # list users
        list_users = self.dl_service.list_users(self.dl_service.container_id)
        assert list_users['isError'] is False

        # We are unable to create users via API, so very little
        # testing of the User APIs can occur

        # retrieve user
        # retrieve_user = self.dl_service.retrieve_user(self.dl_service.container_id, user_id)
        # assert retrieve_user['isError'] is False

        # # list user roles
        # user_roles = self.dl_service.list_user_roles(self.dl_service.container_id, user_id)
        # assert user_roles['isError'] is False

    # METATYPES

    def test_metatypes(self):
        """Covers all aspects of creating, listing, and archiving metatypes."""
        metatype = self.dl_service.create_metatype(self.dl_service.container_id, {
            "name": "Test Metatype",
            "description": "A test metatype"
        })
        metatype_id = metatype['value'][0]['id']
        assert metatype_id is not None

        # retrieve metatype
        retrieve_metatype = self.dl_service.retrieve_metatype(self.dl_service.container_id, metatype_id)
        assert retrieve_metatype['isError'] is False

        # list metatypes
        list_metatypes = self.dl_service.list_metatypes(self.dl_service.container_id)
        assert len(list_metatypes['value']) > 0

        # update metatype
        update_metatype = self.dl_service.update_metatype(self.dl_service.container_id, metatype_id, {
            "name": "Test Metatype",
            "description": "A test metatype with updated description"
        })
        assert update_metatype['isError'] is False

        # archive metatype
        archive_metatype = self.dl_service.archive_metatype(self.dl_service.container_id, metatype_id)
        assert archive_metatype['isError'] is False

    # METATYPE KEYS

    def test_metatype_keys(self):
        """Covers all aspects of creating, listing, and archiving metatype keys."""
        # create metatype
        metatype = self.dl_service.create_metatype(self.dl_service.container_id, {
            "name": "Test Metatype for Keys",
            "description": "A test metatype for keys"
        })
        metatype_id = metatype['value'][0]['id']
        assert metatype_id is not None

        # create metatype key
        metatype_key = self.dl_service.create_metatype_key(
            self.dl_service.container_id, metatype_id, {
                "name": "Test Key",
                "required": False,
                "property_name": "test key",
                "description": "Test metatype key",
                "data_type": "string",
                "cardinality": 1,
                "validation": {
                    "regex": "",
                    "min": 0,
                    "max": 0
                },
                "unique": True,
                "options": [""],
                "defaultValue": ""
            })
        metatype_key_id = metatype_key['value'][0]['id']
        assert metatype_key_id is not None

        # retrieve metatype key
        retrieve_metatype_key = self.dl_service.retrieve_metatype_key(self.dl_service.container_id, metatype_id,
                                                                      metatype_key_id)
        assert retrieve_metatype_key['isError'] is False

        # list metatype keys
        list_metatype_keys = self.dl_service.list_metatype_keys(self.dl_service.container_id, metatype_id)
        assert len(list_metatype_keys['value']) > 0

        # update metatype key
        update_metatype_key = self.dl_service.update_metatype_key(
            self.dl_service.container_id, metatype_id, metatype_key_id, {
                "name": "Test Key",
                "required": False,
                "property_name": "test key",
                "description": "Test metatype key with updated description",
                "data_type": "string",
                "cardinality": 1,
                "validation": {
                    "regex": "",
                    "min": 0,
                    "max": 0
                },
                "unique": True,
                "options": [""],
                "defaultValue": ""
            })
        assert update_metatype_key['isError'] is False

        # archive metatype key
        archive_metatype_key = self.dl_service.archive_metatype_key(self.dl_service.container_id, metatype_id,
                                                                    metatype_key_id)
        assert archive_metatype_key['isError'] is False

    # METATYPE RELATIONSHIPS

    def test_metatype_relationships(self):
        """Covers all aspects of creating, listing, and archiving metatype relationships."""
        relationship = self.dl_service.create_relationship(self.dl_service.container_id, {
            "name": "Test Relationship",
            "description": "A test metatype relationship"
        })
        relationship_id = relationship['value'][0]['id']
        assert relationship_id is not None

        # retrieve relationship
        retrieve_relationship = self.dl_service.retrieve_relationship(self.dl_service.container_id, relationship_id)
        assert retrieve_relationship['isError'] is False

        # list relationships
        list_relationships = self.dl_service.list_relationships(self.dl_service.container_id)
        assert len(list_relationships['value']) > 0

        # update relationship
        update_relationship = self.dl_service.update_relationship(self.dl_service.container_id, relationship_id, {
            "name": "Test Relationship",
            "description": "A test metatype relationship"
        })
        assert update_relationship['isError'] is False

        # archive relationship
        archive_relationship = self.dl_service.archive_relationship(self.dl_service.container_id, relationship_id)
        assert archive_relationship['isError'] is False

    # METATYPE RELATIONSHIP KEYS

    def test_relationship_keys(self):
        """Covers all aspects of creating, listing, and archiving relationship keys."""
        # create relationship
        relationship = self.dl_service.create_relationship(self.dl_service.container_id, {
            "name": "Test Relationship for Keys",
            "description": "A test relationship for keys"
        })
        relationship_id = relationship['value'][0]['id']
        assert relationship_id is not None

        # create relationship key
        relationship_key = self.dl_service.create_relationship_key(
            self.dl_service.container_id, relationship_id, {
                "name": "Test Key",
                "required": False,
                "property_name": "test key",
                "description": "Test relationship key",
                "data_type": "string",
                "cardinality": 1,
                "validation": {
                    "regex": "",
                    "min": 0,
                    "max": 0
                },
                "unique": True,
                "options": [""],
                "defaultValue": ""
            })
        relationship_key_id = relationship_key['value'][0]['id']
        assert relationship_key_id is not None

        # retrieve relationship key
        retrieve_relationship_key = self.dl_service.retrieve_relationship_key(self.dl_service.container_id,
                                                                              relationship_id, relationship_key_id)
        assert retrieve_relationship_key['isError'] is False

        # list relationship keys
        list_relationship_keys = self.dl_service.list_relationship_keys(self.dl_service.container_id, relationship_id)
        assert len(list_relationship_keys['value']) > 0

        # update relationship key
        update_relationship_key = self.dl_service.update_relationship_key(
            self.dl_service.container_id, relationship_id, relationship_key_id, {
                "name": "Test Key",
                "required": False,
                "property_name": "test key",
                "description": "Test relationship key with updated description",
                "data_type": "string",
                "cardinality": 1,
                "validation": {
                    "regex": "",
                    "min": 0,
                    "max": 0
                },
                "unique": True,
                "options": [""],
                "defaultValue": ""
            })
        assert update_relationship_key['isError'] is False

        # archive relationship key
        archive_relationship_key = self.dl_service.archive_relationship_key(self.dl_service.container_id,
                                                                            relationship_id, relationship_key_id)
        assert archive_relationship_key['isError'] is False

    # METATYPE RELATIONSHIP PAIRS

    def test_relationship_pairs(self):
        """Covers all aspects of creating, listing, and archiving relationship pairs."""
        # create relationship
        relationship = self.dl_service.create_relationship(self.dl_service.container_id, {
            "name": "Test Relationship for Pair",
            "description": "A test metatype relationship for pair"
        })
        relationship_id = relationship['value'][0]['id']
        assert relationship_id is not None

        # create metatypes
        metatype_1 = self.dl_service.create_metatype(self.dl_service.container_id, {
            "name": "Test Metatype for Pair 1",
            "description": "A test metatype for relationship pair"
        })
        metatype_1_id = metatype_1['value'][0]['id']
        assert metatype_1_id is not None

        metatype_2 = self.dl_service.create_metatype(self.dl_service.container_id, {
            "name": "Test Metatype for Pair 2",
            "description": "A test metatype for relationship pair"
        })
        metatype_2_id = metatype_2['value'][0]['id']
        assert metatype_2_id is not None

        # create relationship pair
        relationship_pair = self.dl_service.create_relationship_pair(
            self.dl_service.container_id, {
                "name": "Relationship Pair Test",
                "description": "Relationship Pair Test description",
                "origin_metatype_id": metatype_1_id,
                "destination_metatype_id": metatype_2_id,
                "relationship_id": relationship_id,
                "relationship_type": "many:many"
            })
        relationship_pair_id = relationship_pair['value'][0]['id']
        assert relationship_pair_id is not None

        # retrieve relationship pair
        retrieve_relationship_pair = self.dl_service.retrieve_relationship_pair(self.dl_service.container_id,
                                                                                relationship_pair_id)
        assert retrieve_relationship_pair['isError'] is False

        # list relationship pairs
        list_relationship_pairs = self.dl_service.list_relationship_pairs(self.dl_service.container_id)
        assert len(list_relationship_pairs['value']) > 0

        # update relationship pair
        update_relationship_pair = self.dl_service.update_relationship_pair(
            self.dl_service.container_id, relationship_pair_id, {
                "name": "Relationship Pair Test",
                "description": "Relationship Pair Test description",
                "origin_metatype_id": metatype_1_id,
                "destination_metatype_id": metatype_2_id,
                "relationship_id": relationship_id,
                "relationship_type": "many:many"
            })
        assert update_relationship_pair['isError'] is False

        # archive relationship pair
        archive_relationship_pair = self.dl_service.archive_relationship_pair(self.dl_service.container_id,
                                                                              relationship_pair_id)
        assert archive_relationship_pair['isError'] is False
