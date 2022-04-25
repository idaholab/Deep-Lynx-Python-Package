# coding: utf-8

"""
    Deep Lynx

    The construction of megaprojects has consistently demonstrated challenges for project managers in regard to meeting cost, schedule, and performance requirements. Megaproject construction challenges are common place within megaprojects with many active projects in the United States failing to meet cost and schedule efforts by significant margins. Currently, engineering teams operate in siloed tools and disparate teams where connections across design, procurement, and construction systems are translated manually or over brittle point-to-point integrations. The manual nature of data exchange increases the risk of silent errors in the reactor design, with each silent error cascading across the design. These cascading errors lead to uncontrollable risk during construction, resulting in significant delays and cost overruns. Deep Lynx allows for an integrated platform during design and operations of mega projects.  The Deep Lynx Core API delivers a few main features.  1. Provides a set of methods and endpoints for manipulating data in an object oriented database. This allows us to store complex datatypes as records and then to compile them into actual, modifiable objects at run-time. Users can store taxonomies or ontologies in a readable format.  2. Provides methods for storing and retrieving data in a graph database. This data is structured and validated against the aformentioned object oriented database before storage.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deep_lynx.api_client import ApiClient


class DataQueryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def data_query(self, body, container_id, **kwargs):  # noqa: E501
        """Query Data  # noqa: E501

        Query data from your container using GraphQL. You can learn more here - https://gitlab.software.inl.gov/b650/Deep-Lynx/-/wikis/Querying-Data-With-GraphQL  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_query(body, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param str container_id: (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_query_with_http_info(body, container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.data_query_with_http_info(body, container_id, **kwargs)  # noqa: E501
            return data

    def data_query_with_http_info(self, body, container_id, **kwargs):  # noqa: E501
        """Query Data  # noqa: E501

        Query data from your container using GraphQL. You can learn more here - https://gitlab.software.inl.gov/b650/Deep-Lynx/-/wikis/Querying-Data-With-GraphQL  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_query_with_http_info(body, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param str container_id: (required)
        :return: InlineResponse200
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
                    " to method data_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `data_query`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `data_query`")  # noqa: E501

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
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/containers/{container_id}/data', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_query(self, body, container_id, **kwargs):  # noqa: E501
        """Query Data  # noqa: E501

        Query data from your container using GraphQL. You can learn more here - https://gitlab.software.inl.gov/b650/Deep-Lynx/-/wikis/Querying-Data-With-GraphQL  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_query(body, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param str container_id: (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_query_with_http_info(body, container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.data_query_with_http_info(body, container_id, **kwargs)  # noqa: E501
            return data

    def data_query_with_http_info(self, body, container_id, **kwargs):  # noqa: E501
        """Query Data  # noqa: E501

        Query data from your container using GraphQL. You can learn more here - https://gitlab.software.inl.gov/b650/Deep-Lynx/-/wikis/Querying-Data-With-GraphQL  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_query_with_http_info(body, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param str container_id: (required)
        :return: InlineResponse200
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
                    " to method data_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `data_query`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `data_query`")  # noqa: E501

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
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/containers/{container_id}/data', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_graph(self, body, container_id, **kwargs):  # noqa: E501
        """Query Graph (Deprecated)  # noqa: E501

        Query the graph of the specified container using GraphQL. GraphQL queries may be formatted as json or plain text.  This has been deprecated in favor of the `/containers/{container_id}/data` endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_graph(body, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param str container_id: (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_graph_with_http_info(body, container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.query_graph_with_http_info(body, container_id, **kwargs)  # noqa: E501
            return data

    def query_graph_with_http_info(self, body, container_id, **kwargs):  # noqa: E501
        """Query Graph (Deprecated)  # noqa: E501

        Query the graph of the specified container using GraphQL. GraphQL queries may be formatted as json or plain text.  This has been deprecated in favor of the `/containers/{container_id}/data` endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_graph_with_http_info(body, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param str container_id: (required)
        :return: InlineResponse200
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
                    " to method query_graph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `query_graph`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `query_graph`")  # noqa: E501

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
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/containers/{container_id}/query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_graph(self, body, container_id, **kwargs):  # noqa: E501
        """Query Graph (Deprecated)  # noqa: E501

        Query the graph of the specified container using GraphQL. GraphQL queries may be formatted as json or plain text.  This has been deprecated in favor of the `/containers/{container_id}/data` endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_graph(body, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param str container_id: (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_graph_with_http_info(body, container_id, **kwargs)  # noqa: E501
        else:
            (data) = self.query_graph_with_http_info(body, container_id, **kwargs)  # noqa: E501
            return data

    def query_graph_with_http_info(self, body, container_id, **kwargs):  # noqa: E501
        """Query Graph (Deprecated)  # noqa: E501

        Query the graph of the specified container using GraphQL. GraphQL queries may be formatted as json or plain text.  This has been deprecated in favor of the `/containers/{container_id}/data` endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_graph_with_http_info(body, container_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: (required)
        :param str container_id: (required)
        :return: InlineResponse200
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
                    " to method query_graph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `query_graph`")  # noqa: E501
        # verify the required parameter 'container_id' is set
        if ('container_id' not in params or
                params['container_id'] is None):
            raise ValueError("Missing the required parameter `container_id` when calling `query_graph`")  # noqa: E501

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
            ['application/json', 'text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/containers/{container_id}/query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
