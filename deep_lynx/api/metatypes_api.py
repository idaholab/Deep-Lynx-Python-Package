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


class MetatypesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive_metatype(self, container_id, metatype_id, **kwargs):  # noqa: E501
        """Archive Metatype  # noqa: E501

        Archives the metatype. This is preferred over deletion as deletion has a cascading effect on the deleted metatype's keys, relationships, and relationship keys. When in doubt, archive over delete. We'd rather have tombstones than cremating the metatype.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_metatype(container_id, metatype_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str metatype_id: (required)
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.archive_metatype_with_http_info(container_id, metatype_id, **kwargs)  # noqa: E501
        else:
            (data) = self.archive_metatype_with_http_info(container_id, metatype_id, **kwargs)  # noqa: E501
            return data

    def archive_metatype_with_http_info(self, container_id, metatype_id, **kwargs):  # noqa: E501
        """Archive Metatype  # noqa: E501

        Archives the metatype. This is preferred over deletion as deletion has a cascading effect on the deleted metatype's keys, relationships, and relationship keys. When in doubt, archive over delete. We'd rather have tombstones than cremating the metatype.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_metatype_with_http_info(container_id, metatype_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str metatype_id: (required)
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'metatype_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method archive_metatype" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `archive_metatype`")  # noqa: E501
        # verify the required parameter 'metatype_id' is set
        if ('metatype_id' not in params or
                params['metatype_id'] is None):
            raise ValueError("Missing the required parameter `metatype_id` when calling `archive_metatype`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501
        if 'metatype_id' in params:
            path_params['metatype_id'] = params['metatype_id']  # noqa: E501

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
            '/containers/{container_id}/metatypes/{metatype_id}', 'DELETE',
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

    def create_metatype(self, body, container_id, **kwargs):  # noqa: E501
        """Create Metatype  # noqa: E501

        Create a new metatype. Pass in an array for bulk creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_metatype(body, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateMetatypeRequest body: (required)
        :param str container_id: (required)
        :return: CreateMetatypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_metatype_with_http_info(body, container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_metatype_with_http_info(body, container_id, **kwargs)  # noqa: E501
            return data

    def create_metatype_with_http_info(self, body, container_id, **kwargs):  # noqa: E501
        """Create Metatype  # noqa: E501

        Create a new metatype. Pass in an array for bulk creation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_metatype_with_http_info(body, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateMetatypeRequest body: (required)
        :param str container_id: (required)
        :return: CreateMetatypesResponse
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
                    " to method create_metatype" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_metatype`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `create_metatype`")  # noqa: E501

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
            '/containers/{container_id}/metatypes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateMetatypesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_metatypes(self, container_id, **kwargs):  # noqa: E501
        """List Metatypes  # noqa: E501

        List all metatypes that the container has access to.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_metatypes(container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param int limit:
        :param int offset:
        :param str name: Filter metatypes with names that match this pattern
        :param str description: Filter metatypes with descriptions that match this pattern
        :param str count: Set to true to return an integer count of the number of metatypes
        :param str load_keys: Set to false to not return the keys for the selected metatypes (true by default)
        :param str sort_by: Supply the name of a metatype attribute (name, created_at, etc) by which to sort
        :param str sort_desc: Set true to sort descending
        :return: ListMetatypesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_metatypes_with_http_info(container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_metatypes_with_http_info(container_id, **kwargs)  # noqa: E501
            return data

    def list_metatypes_with_http_info(self, container_id, **kwargs):  # noqa: E501
        """List Metatypes  # noqa: E501

        List all metatypes that the container has access to.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_metatypes_with_http_info(container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param int limit:
        :param int offset:
        :param str name: Filter metatypes with names that match this pattern
        :param str description: Filter metatypes with descriptions that match this pattern
        :param str count: Set to true to return an integer count of the number of metatypes
        :param str load_keys: Set to false to not return the keys for the selected metatypes (true by default)
        :param str sort_by: Supply the name of a metatype attribute (name, created_at, etc) by which to sort
        :param str sort_desc: Set true to sort descending
        :return: ListMetatypesResponse
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
                    " to method list_metatypes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `list_metatypes`")  # noqa: E501

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
            '/containers/{container_id}/metatypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListMetatypesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_metaype(self, container_id, metatype_id, **kwargs):  # noqa: E501
        """Retrieve Metatype  # noqa: E501

        Retrieves a single metatype.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_metaype(container_id, metatype_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str metatype_id: (required)
        :return: GetMetatypeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_metaype_with_http_info(container_id, metatype_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_metaype_with_http_info(container_id, metatype_id, **kwargs)  # noqa: E501
            return data

    def retrieve_metaype_with_http_info(self, container_id, metatype_id, **kwargs):  # noqa: E501
        """Retrieve Metatype  # noqa: E501

        Retrieves a single metatype.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_metaype_with_http_info(container_id, metatype_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str metatype_id: (required)
        :return: GetMetatypeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'metatype_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_metaype" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `retrieve_metaype`")  # noqa: E501
        # verify the required parameter 'metatype_id' is set
        if ('metatype_id' not in params or
                params['metatype_id'] is None):
            raise ValueError("Missing the required parameter `metatype_id` when calling `retrieve_metaype`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501
        if 'metatype_id' in params:
            path_params['metatype_id'] = params['metatype_id']  # noqa: E501

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
            '/containers/{container_id}/metatypes/{metatype_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetMetatypeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_metatype(self, body, container_id, metatype_id, **kwargs):  # noqa: E501
        """Update Metatype  # noqa: E501

        Update a single Metatype in storage. Will fail if the updated name has already been taken.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_metatype(body, container_id, metatype_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateMetatypeRequest body: (required)
        :param str container_id: (required)
        :param str metatype_id: (required)
        :return: UpdateMetatypeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_metatype_with_http_info(body, container_id, metatype_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_metatype_with_http_info(body, container_id, metatype_id, **kwargs)  # noqa: E501
            return data

    def update_metatype_with_http_info(self, body, container_id, metatype_id, **kwargs):  # noqa: E501
        """Update Metatype  # noqa: E501

        Update a single Metatype in storage. Will fail if the updated name has already been taken.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_metatype_with_http_info(body, container_id, metatype_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateMetatypeRequest body: (required)
        :param str container_id: (required)
        :param str metatype_id: (required)
        :return: UpdateMetatypeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'container_id', 'metatype_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_metatype" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_metatype`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `update_metatype`")  # noqa: E501
        # verify the required parameter 'metatype_id' is set
        if ('metatype_id' not in params or
                params['metatype_id'] is None):
            raise ValueError("Missing the required parameter `metatype_id` when calling `update_metatype`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501
        if 'metatype_id' in params:
            path_params['metatype_id'] = params['metatype_id']  # noqa: E501

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
            '/containers/{container_id}/metatypes/{metatype_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdateMetatypeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate_metatype_properties(self, container_id, metatype_id, **kwargs):  # noqa: E501
        """Validate Metatype Properties  # noqa: E501

        Returns any errors associated with the intended properties or keys for a metatype or else the data itself if no errors are present.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_metatype_properties(container_id, metatype_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str metatype_id: (required)
        :param ValidateMetatypePropertiesRequest body:
        :return: ValidateMetatypePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.validate_metatype_properties_with_http_info(container_id, metatype_id, **kwargs)  # noqa: E501
        else:
            (data) = self.validate_metatype_properties_with_http_info(container_id, metatype_id, **kwargs)  # noqa: E501
            return data

    def validate_metatype_properties_with_http_info(self, container_id, metatype_id, **kwargs):  # noqa: E501
        """Validate Metatype Properties  # noqa: E501

        Returns any errors associated with the intended properties or keys for a metatype or else the data itself if no errors are present.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_metatype_properties_with_http_info(container_id, metatype_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str metatype_id: (required)
        :param ValidateMetatypePropertiesRequest body:
        :return: ValidateMetatypePropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'metatype_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_metatype_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `validate_metatype_properties`")  # noqa: E501
        # verify the required parameter 'metatype_id' is set
        if ('metatype_id' not in params or
                params['metatype_id'] is None):
            raise ValueError("Missing the required parameter `metatype_id` when calling `validate_metatype_properties`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501
        if 'metatype_id' in params:
            path_params['metatype_id'] = params['metatype_id']  # noqa: E501

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
            '/containers/{container_id}/metatypes/{metatype_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidateMetatypePropertiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
