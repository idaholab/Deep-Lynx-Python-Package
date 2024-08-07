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


class DataTargetsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive_data_target(self, container_id, data_target_id, **kwargs):  # noqa: E501
        """Archive Data Target  # noqa: E501

        Archive a data target, with options to permanently remove it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_data_target(container_id, data_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str data_target_id: (required)
        :param str archive: Set to true to archive the data target.
        :param str force_delete: Set to true to force deletion of the data target.
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.archive_data_target_with_http_info(container_id, data_target_id, **kwargs)  # noqa: E501
        else:
            (data) = self.archive_data_target_with_http_info(container_id, data_target_id, **kwargs)  # noqa: E501
            return data

    def archive_data_target_with_http_info(self, container_id, data_target_id, **kwargs):  # noqa: E501
        """Archive Data Target  # noqa: E501

        Archive a data target, with options to permanently remove it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_data_target_with_http_info(container_id, data_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str data_target_id: (required)
        :param str archive: Set to true to archive the data target.
        :param str force_delete: Set to true to force deletion of the data target.
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'data_target_id', 'archive', 'force_delete']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method archive_data_target" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `archive_data_target`")  # noqa: E501
        # verify the required parameter 'data_target_id' is set
        if ('data_target_id' not in params or
                params['data_target_id'] is None):
            raise ValueError("Missing the required parameter `data_target_id` when calling `archive_data_target`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501
        if 'data_target_id' in params:
            path_params['data_target_id'] = params['data_target_id']  # noqa: E501

        query_params = []
        if 'archive' in params:
            query_params.append(('archive', params['archive']))  # noqa: E501
        if 'force_delete' in params:
            query_params.append(('forceDelete', params['force_delete']))  # noqa: E501

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
            '/containers/{container_id}/export/datatargets/{data_target_id}', 'DELETE',
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

    def create_data_target(self, container_id, **kwargs):  # noqa: E501
        """Create Data Target  # noqa: E501

        Create new datatarget. Supported data target types are `http` and `standard`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_data_target(container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param CreateDataTargetRequest body:
        :return: CreateDataTargetsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_data_target_with_http_info(container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_data_target_with_http_info(container_id, **kwargs)  # noqa: E501
            return data

    def create_data_target_with_http_info(self, container_id, **kwargs):  # noqa: E501
        """Create Data Target  # noqa: E501

        Create new datatarget. Supported data target types are `http` and `standard`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_data_target_with_http_info(container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param CreateDataTargetRequest body:
        :return: CreateDataTargetsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_data_target" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `create_data_target`")  # noqa: E501

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
            '/containers/{container_id}/export/datatargets', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateDataTargetsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_dat_targets(self, container_id, **kwargs):  # noqa: E501
        """List Data Targets  # noqa: E501

        List the datatargets for the container.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_dat_targets(container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :return: ListDataTargetsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_dat_targets_with_http_info(container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_dat_targets_with_http_info(container_id, **kwargs)  # noqa: E501
            return data

    def list_dat_targets_with_http_info(self, container_id, **kwargs):  # noqa: E501
        """List Data Targets  # noqa: E501

        List the datatargets for the container.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_dat_targets_with_http_info(container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :return: ListDataTargetsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_dat_targets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `list_dat_targets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501

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
            '/containers/{container_id}/export/datatargets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListDataTargetsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_data_target(self, container_id, data_target_id, **kwargs):  # noqa: E501
        """Retrieve Data Target  # noqa: E501

        Retrieve a single data target by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_data_target(container_id, data_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str data_target_id: (required)
        :return: GetDataTargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_data_target_with_http_info(container_id, data_target_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_data_target_with_http_info(container_id, data_target_id, **kwargs)  # noqa: E501
            return data

    def retrieve_data_target_with_http_info(self, container_id, data_target_id, **kwargs):  # noqa: E501
        """Retrieve Data Target  # noqa: E501

        Retrieve a single data target by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_data_target_with_http_info(container_id, data_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str data_target_id: (required)
        :return: GetDataTargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'data_target_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_data_target" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `retrieve_data_target`")  # noqa: E501
        # verify the required parameter 'data_target_id' is set
        if ('data_target_id' not in params or
                params['data_target_id'] is None):
            raise ValueError("Missing the required parameter `data_target_id` when calling `retrieve_data_target`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501
        if 'data_target_id' in params:
            path_params['data_target_id'] = params['data_target_id']  # noqa: E501

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
            '/containers/{container_id}/export/datatargets/{data_target_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetDataTargetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_data_target_active(self, container_id, data_target_id, **kwargs):  # noqa: E501
        """Set Data Target Active  # noqa: E501

        Sets a data target active.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_data_target_active(container_id, data_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str data_target_id: (required)
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_data_target_active_with_http_info(container_id, data_target_id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_data_target_active_with_http_info(container_id, data_target_id, **kwargs)  # noqa: E501
            return data

    def set_data_target_active_with_http_info(self, container_id, data_target_id, **kwargs):  # noqa: E501
        """Set Data Target Active  # noqa: E501

        Sets a data target active.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_data_target_active_with_http_info(container_id, data_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str data_target_id: (required)
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'data_target_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_data_target_active" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `set_data_target_active`")  # noqa: E501
        # verify the required parameter 'data_target_id' is set
        if ('data_target_id' not in params or
                params['data_target_id'] is None):
            raise ValueError("Missing the required parameter `data_target_id` when calling `set_data_target_active`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501
        if 'data_target_id' in params:
            path_params['data_target_id'] = params['data_target_id']  # noqa: E501

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
            '/containers/{container_id}/export/datatargets/{data_target_id}/active', 'POST',
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

    def set_data_target_configuration(self, body, container_id, data_target_id, **kwargs):  # noqa: E501
        """Set Data Target Configuration  # noqa: E501

        Updates a data target's configuration in storage. Note that this request body's structure must match that of the data target's adapter type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_data_target_configuration(body, container_id, data_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateDataTargetConfig body: (required)
        :param str container_id: (required)
        :param str data_target_id: (required)
        :return: UpdateDataTargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_data_target_configuration_with_http_info(body, container_id, data_target_id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_data_target_configuration_with_http_info(body, container_id, data_target_id, **kwargs)  # noqa: E501
            return data

    def set_data_target_configuration_with_http_info(self, body, container_id, data_target_id, **kwargs):  # noqa: E501
        """Set Data Target Configuration  # noqa: E501

        Updates a data target's configuration in storage. Note that this request body's structure must match that of the data target's adapter type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_data_target_configuration_with_http_info(body, container_id, data_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateDataTargetConfig body: (required)
        :param str container_id: (required)
        :param str data_target_id: (required)
        :return: UpdateDataTargetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'container_id', 'data_target_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_data_target_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `set_data_target_configuration`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `set_data_target_configuration`")  # noqa: E501
        # verify the required parameter 'data_target_id' is set
        if ('data_target_id' not in params or
                params['data_target_id'] is None):
            raise ValueError("Missing the required parameter `data_target_id` when calling `set_data_target_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501
        if 'data_target_id' in params:
            path_params['data_target_id'] = params['data_target_id']  # noqa: E501

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
            '/containers/{container_id}/export/datatargets/{data_target_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpdateDataTargetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_data_target_inactive(self, container_id, data_target_id, **kwargs):  # noqa: E501
        """Set Data Target Inactive  # noqa: E501

        Sets a data target inactive.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_data_target_inactive(container_id, data_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str data_target_id: (required)
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_data_target_inactive_with_http_info(container_id, data_target_id, **kwargs)  # noqa: E501
        else:
            (data) = self.set_data_target_inactive_with_http_info(container_id, data_target_id, **kwargs)  # noqa: E501
            return data

    def set_data_target_inactive_with_http_info(self, container_id, data_target_id, **kwargs):  # noqa: E501
        """Set Data Target Inactive  # noqa: E501

        Sets a data target inactive.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_data_target_inactive_with_http_info(container_id, data_target_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str container_id: (required)
        :param str data_target_id: (required)
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['container_id', 'data_target_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_data_target_inactive" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `set_data_target_inactive`")  # noqa: E501
        # verify the required parameter 'data_target_id' is set
        if ('data_target_id' not in params or
                params['data_target_id'] is None):
            raise ValueError("Missing the required parameter `data_target_id` when calling `set_data_target_inactive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'container_id' in params:
            path_params['container_id'] = params['container_id']  # noqa: E501
        if 'data_target_id' in params:
            path_params['data_target_id'] = params['data_target_id']  # noqa: E501

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
            '/containers/{container_id}/export/datatargets/{data_target_id}/active', 'DELETE',
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
