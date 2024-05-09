# coding: utf-8

from __future__ import absolute_import
from os import getenv
from dotenv import load_dotenv

import unittest
from deep_lynx.configuration import Configuration
from deep_lynx.models.create_container_request import CreateContainerRequest
from deep_lynx.models.create_container_response import CreateContainerResponse
from deep_lynx.models.create_data_source_request import CreateDataSourceRequest
from deep_lynx.models.token_exchange_request import TokenExchangeRequest

import swagger_client
import deep_lynx
from swagger_client.models.create_manual_import import CreateManualImport  # noqa: E501
from swagger_client.rest import ApiException


class TestCore(unittest.TestCase):
    """CreateManualImport unit test stubs"""

    # API Setup
    configuration = Configuration()
    configuration.host = 'http://localhost:8090'
    apiClient = deep_lynx.ApiClient(configuration)

    containerApi = deep_lynx.ContainersApi(apiClient)
    containerId = ''

    def setUp(self):
        load_dotenv()
        if getenv('API_KEY') is None or getenv('API_SECRET') is None:
            print("""Please supply API key and secret.
Have you copied the .env-sample and created .env?
Skipping all tests in test_create_manual_import.py""")
            raise unittest.SkipTest("""Please supply API key and secret.
                Have you copied the .env-sample and created .env?
                Skipping all tests in test_create_manual_import.py""")

        if getenv('API_KEY') == '' or getenv('API_SECRET') == '':
            print("""Please supply API key and secret.
Skipping all tests in test_create_manual_import.py""")
            raise unittest.SkipTest("""Please supply API key and secret.
                Skipping all tests in test_create_manual_import.py""")
        pass

    def tearDown(self):
        if self.containerId != '':
            self.containerApi.archive_container(self.containerId, permanent=True)
            print('Successfully removed test container')
        pass

    def testCreateManualImport(self):
        """Test CreateManualImport"""
        # Verify API keys have been provided
        apiKey = getenv('API_KEY')
        apiSecret = getenv('API_SECRET')

        # Authenticate
        authApi = deep_lynx.AuthenticationApi(self.apiClient)

        token = authApi.retrieve_o_auth_token(x_api_key=apiKey, x_api_secret=apiSecret, x_api_expiry='1h')
        self.assertIsNotNone(token)

        # Add token to headers
        self.apiClient.set_default_header('Authorization', 'Bearer {}'.format(token))

        containers = self.containerApi.list_containers()
        self.assertIsNotNone(containers)

        container = self.containerApi.create_container(CreateContainerRequest(
            'sdk_test', 'Test container description', False
        ))
        self.assertIsNotNone(container.value[0].id)
        self.containerId = container.value[0].id

        # Create Data Source
        datasourcesApi = deep_lynx.DataSourcesApi(self.apiClient)

        datasource = datasourcesApi.create_data_source(CreateDataSourceRequest(
            'sdk_test_source', 'standard', True
        ), self.containerId)
        self.assertIsNotNone(datasource.value.id)
        datasourceId = datasource.value.id

        # Upload File
        file_result = datasourcesApi.upload_file(
            container_id = self.containerId,
            data_source_id = datasourceId,
            file = '.gitignore',
            async_req = False
        )
        self.assertIsNotNone(file_result['value'])

        # Create Manual Import
        import_result = datasourcesApi.create_manual_import(
            {'test': 'test import'},
            self.containerId,
            datasourceId,
            async_req = False
        )
        self.assertIsNotNone(import_result.value)

        pass


if __name__ == '__main__':
    unittest.main()
