# coding: utf-8

"""
    DeepLynx

    The construction of megaprojects has consistently demonstrated challenges for project managers in regard to meeting cost, schedule, and performance requirements. Megaproject construction challenges are common place within megaprojects with many active projects in the United States failing to meet cost and schedule efforts by significant margins. Currently, engineering teams operate in siloed tools and disparate teams where connections across design, procurement, and construction systems are translated manually or over brittle point-to-point integrations. The manual nature of data exchange increases the risk of silent errors in the reactor design, with each silent error cascading across the design. These cascading errors lead to uncontrollable risk during construction, resulting in significant delays and cost overruns. DeepLynx allows for an integrated platform during design and operations of mega projects. The DeepLynx Core API delivers a few main features. 1. Provides a set of methods and endpoints for manipulating data in an object oriented database. This allows us to store complex datatypes as records and then to compile them into actual, modifiable objects at run-time. Users can store taxonomies or ontologies in a readable format. 2. Provides methods for storing and retrieving data in a graph database. This data is structured and validated against the aformentioned object oriented database before storage.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deep_lynx.api_client import ApiClient


class MetatypeRelationshipsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive_metatype_relationship(self, container_id, relationship_id, **kwargs):  # noqa: E501
        """Archive Metatype Relationship  # noqa: E501

        Archive the metatype relationship.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_metatype_relationship(container_id, relationship_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str relationship_id: (required)
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.archive_metatype_relationship_with_http_info(container_id, relationship_id, **kwargs)  # noqa: E501
        else:
            (data) = self.archive_metatype_relationship_with_http_info(container_id, relationship_id, **kwargs)  # noqa: E501
            return data

    def archive_metatype_relationship_with_http_info(self, container_id, relationship_id, **kwargs):  # noqa: E501
        """Archive Metatype Relationship  # noqa: E501

        Archive the metatype relationship.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_metatype_relationship_with_http_info(container_id, relationship_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str relationship_id: (required)
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'relationship_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method archive_metatype_relationship" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `archive_metatype_relationship`")  # noqa: E501
        # verify the required parameter 'relationship_id' is set
        if ('relationship_id' not in params or
                params['relationship_id'] is None):
            raise ValueError("Missing the required parameter `relationship_id` when calling `archive_metatype_relationship`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501
        if 'relationship_id' in params:
            path_params['relationship_id'] = params['relationship_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/containers/{container_id}/metatype_relationships/{relationship_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Generic200Response',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_metatype_relationship(self, body, container_id, **kwargs):  # noqa: E501
        """Create Metatype Relationship  # noqa: E501

        Create a new metatype relationship. Describes the connection that could exist between two metatypes and acts as a vehicle for relationship specific keys. Pass in an array for bulk creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_metatype_relationship(body, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateMetatypeRelationshipRequest body: (required)
        :param str container_id: (required)
        :return: CreateMetatypeRelationshipsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_metatype_relationship_with_http_info(body, container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_metatype_relationship_with_http_info(body, container_id, **kwargs)  # noqa: E501
            return data

    def create_metatype_relationship_with_http_info(self, body, container_id, **kwargs):  # noqa: E501
        """Create Metatype Relationship  # noqa: E501

        Create a new metatype relationship. Describes the connection that could exist between two metatypes and acts as a vehicle for relationship specific keys. Pass in an array for bulk creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_metatype_relationship_with_http_info(body, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateMetatypeRelationshipRequest body: (required)
        :param str container_id: (required)
        :return: CreateMetatypeRelationshipsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'container_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_metatype_relationship" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_metatype_relationship`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `create_metatype_relationship`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/containers/{container_id}/metatype_relationships', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateMetatypeRelationshipsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_metatype_relationships(self, container_id, **kwargs):  # noqa: E501
        """List Metatype Relationships  # noqa: E501

        List metatype relationships. Describes the connection between two metatypes and acts as a vehicle for relationship specific keys.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_metatype_relationships(container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param int limit:
        :param int offset:
        :param str name: Filter metatype relationships with names that match this pattern
        :param str description: Filter metatype relationships with descriptions that match this pattern
        :param str count: Set to true to return an integer count of the number of metatype relationships
        :param str load_keys: Set to false to not return the keys for the selected metatype relationships (true by default)
        :param str sort_by: Supply the name of a metatype relationship attribute (name, created_at, etc) by which to sort
        :param str sort_desc: Set true to sort descending
        :return: ListMetatypeRelationshipsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_metatype_relationships_with_http_info(container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_metatype_relationships_with_http_info(container_id, **kwargs)  # noqa: E501
            return data

    def list_metatype_relationships_with_http_info(self, container_id, **kwargs):  # noqa: E501
        """List Metatype Relationships  # noqa: E501

        List metatype relationships. Describes the connection between two metatypes and acts as a vehicle for relationship specific keys.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_metatype_relationships_with_http_info(container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param int limit:
        :param int offset:
        :param str name: Filter metatype relationships with names that match this pattern
        :param str description: Filter metatype relationships with descriptions that match this pattern
        :param str count: Set to true to return an integer count of the number of metatype relationships
        :param str load_keys: Set to false to not return the keys for the selected metatype relationships (true by default)
        :param str sort_by: Supply the name of a metatype relationship attribute (name, created_at, etc) by which to sort
        :param str sort_desc: Set true to sort descending
        :return: ListMetatypeRelationshipsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'limit', 'offset', 'name', 'description', 'count', 'load_keys', 'sort_by', 'sort_desc']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_metatype_relationships" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `list_metatype_relationships`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'description' in params:
            query_params.append(('description', params['description']))  # noqa: E501
        if 'count' in params:
            query_params.append(('count', params['count']))  # noqa: E501
        if 'load_keys' in params:
            query_params.append(('loadKeys', params['load_keys']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))  # noqa: E501
        if 'sort_desc' in params:
            query_params.append(('sortDesc', params['sort_desc']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/containers/{container_id}/metatype_relationships', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListMetatypeRelationshipsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_metatype_relationship(self, container_id, relationship_id, **kwargs):  # noqa: E501
        """Retrieve Metatype Relationship  # noqa: E501

        Retrieve a single Metatype Relationship.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_metatype_relationship(container_id, relationship_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str relationship_id: (required)
        :return: GetMetatypeRelationshipResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_metatype_relationship_with_http_info(container_id, relationship_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_metatype_relationship_with_http_info(container_id, relationship_id, **kwargs)  # noqa: E501
            return data

    def retrieve_metatype_relationship_with_http_info(self, container_id, relationship_id, **kwargs):  # noqa: E501
        """Retrieve Metatype Relationship  # noqa: E501

        Retrieve a single Metatype Relationship.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_metatype_relationship_with_http_info(container_id, relationship_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str relationship_id: (required)
        :return: GetMetatypeRelationshipResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'relationship_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_metatype_relationship" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `retrieve_metatype_relationship`")  # noqa: E501
        # verify the required parameter 'relationship_id' is set
        if ('relationship_id' not in params or
                params['relationship_id'] is None):
            raise ValueError("Missing the required parameter `relationship_id` when calling `retrieve_metatype_relationship`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501
        if 'relationship_id' in params:
            path_params['relationship_id'] = params['relationship_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/containers/{container_id}/metatype_relationships/{relationship_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetMetatypeRelationshipResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_metatype_relationship(self, body, container_id, relationship_id, **kwargs):  # noqa: E501
        """Update Metatype Relationship  # noqa: E501

        Updates the specified metatype relationship.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_metatype_relationship(body, container_id, relationship_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateMetatypeRelationshipRequest body: (required)
        :param str container_id: (required)
        :param str relationship_id: (required)
        :return: UpdateMetatypeRelationshipResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_metatype_relationship_with_http_info(body, container_id, relationship_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_metatype_relationship_with_http_info(body, container_id, relationship_id, **kwargs)  # noqa: E501
            return data

    def update_metatype_relationship_with_http_info(self, body, container_id, relationship_id, **kwargs):  # noqa: E501
        """Update Metatype Relationship  # noqa: E501

        Updates the specified metatype relationship.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_metatype_relationship_with_http_info(body, container_id, relationship_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateMetatypeRelationshipRequest body: (required)
        :param str container_id: (required)
        :param str relationship_id: (required)
        :return: UpdateMetatypeRelationshipResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'container_id', 'relationship_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_metatype_relationship" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_metatype_relationship`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `update_metatype_relationship`")  # noqa: E501
        # verify the required parameter 'relationship_id' is set
        if ('relationship_id' not in params or
                params['relationship_id'] is None):
            raise ValueError("Missing the required parameter `relationship_id` when calling `update_metatype_relationship`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501
        if 'relationship_id' in params:
            path_params['relationship_id'] = params['relationship_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/containers/{container_id}/metatype_relationships/{relationship_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdateMetatypeRelationshipResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
