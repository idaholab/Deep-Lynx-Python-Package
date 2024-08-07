# coding: utf-8

"""
    DeepLynx

    The construction of megaprojects has consistently demonstrated challenges for project managers in regard to meeting cost, schedule, and performance requirements. Megaproject construction challenges are common place within megaprojects with many active projects in the United States failing to meet cost and schedule efforts by significant margins. Currently, engineering teams operate in siloed tools and disparate teams where connections across design, procurement, and construction systems are translated manually or over brittle point-to-point integrations. The manual nature of data exchange increases the risk of silent errors in the reactor design, with each silent error cascading across the design. These cascading errors lead to uncontrollable risk during construction, resulting in significant delays and cost overruns. DeepLynx allows for an integrated platform during design and operations of mega projects. The DeepLynx Core API delivers a few main features. 1. Provides a set of methods and endpoints for manipulating data in an object oriented database. This allows us to store complex datatypes as records and then to compile them into actual, modifiable objects at run-time. Users can store taxonomies or ontologies in a readable format. 2. Provides methods for storing and retrieving data in a graph database. This data is structured and validated against the aformentioned object oriented database before storage.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import deep_lynx
from deep_lynx.api.data_type_mappings_api import DataTypeMappingsApi  # noqa: E501
from deep_lynx.rest import ApiException


class TestDataTypeMappingsApi(unittest.TestCase):
    """DataTypeMappingsApi unit test stubs"""

    def setUp(self):
        self.api = DataTypeMappingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_copy_transformations(self):
        """Test case for copy_transformations

        """
        pass

    def test_create_transformation(self):
        """Test case for create_transformation

        Create Data Type Mapping's Transformations  # noqa: E501
        """
        pass

    def test_delete_data_type_mapping(self):
        """Test case for delete_data_type_mapping

        Delete Data Type Mapping  # noqa: E501
        """
        pass

    def test_delete_transformation(self):
        """Test case for delete_transformation

        Delete Data Type Mapping's Transformations  # noqa: E501
        """
        pass

    def test_export_type_mappings(self):
        """Test case for export_type_mappings

        Export Type Mappings  # noqa: E501
        """
        pass

    def test_import_data_type_mappings(self):
        """Test case for import_data_type_mappings

        Import Data Type Mappings  # noqa: E501
        """
        pass

    def test_list_data_type_mappings(self):
        """Test case for list_data_type_mappings

        List Data Type Mappings  # noqa: E501
        """
        pass

    def test_list_transformations(self):
        """Test case for list_transformations

        List Data Type Mapping's Transformations  # noqa: E501
        """
        pass

    def test_retrieve_data_type_mapping(self):
        """Test case for retrieve_data_type_mapping

        Retrieve Data Type Mapping  # noqa: E501
        """
        pass

    def test_update_data_type_mapping(self):
        """Test case for update_data_type_mapping

        Update Data Type Mapping  # noqa: E501
        """
        pass

    def test_update_transformation(self):
        """Test case for update_transformation

        Update Data Type Mapping's Transformations  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
