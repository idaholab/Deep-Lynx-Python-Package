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

from swagger_client.api_client import ApiClient


class EventsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_registered_event(self, body, **kwargs):  # noqa: E501
        """CreateRegisteredEvent  # noqa: E501

        Create new registered event. An `app_name`, `app_url`, and `event_type` must be provided. Either a `container_id` or `data_source_id` must also be provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_registered_event(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRegisteredEventRequest body: (required)
        :return: CreateEventResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_registered_event_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_registered_event_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_registered_event_with_http_info(self, body, **kwargs):  # noqa: E501
        """CreateRegisteredEvent  # noqa: E501

        Create new registered event. An `app_name`, `app_url`, and `event_type` must be provided. Either a `container_id` or `data_source_id` must also be provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_registered_event_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRegisteredEventRequest body: (required)
        :return: CreateEventResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_registered_event" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_registered_event`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
        auth_settings = ['httpBearer']  # noqa: E501

        return self.api_client.call_api(
            '/events', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateEventResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_registered_event(self, event_id, **kwargs):  # noqa: E501
        """DeleteRegisteredEvent  # noqa: E501

        Delete a registered event.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_registered_event(event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_id: (required)
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_registered_event_with_http_info(event_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_registered_event_with_http_info(event_id, **kwargs)  # noqa: E501
            return data

    def delete_registered_event_with_http_info(self, event_id, **kwargs):  # noqa: E501
        """DeleteRegisteredEvent  # noqa: E501

        Delete a registered event.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_registered_event_with_http_info(event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_id: (required)
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_registered_event" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_id' is set
        if ('event_id' not in params or
                params['event_id'] is None):
            raise ValueError("Missing the required parameter `event_id` when calling `delete_registered_event`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_id' in params:
            path_params['event_id'] = params['event_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['httpBearer']  # noqa: E501

        return self.api_client.call_api(
            '/events/{event_id}', 'DELETE',
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

    def list_registered_events(self, **kwargs):  # noqa: E501
        """ListRegisteredEvents  # noqa: E501

        Lists all registered events  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_registered_events(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListEventsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_registered_events_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_registered_events_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_registered_events_with_http_info(self, **kwargs):  # noqa: E501
        """ListRegisteredEvents  # noqa: E501

        Lists all registered events  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_registered_events_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListEventsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_registered_events" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['httpBearer']  # noqa: E501

        return self.api_client.call_api(
            '/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListEventsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_registered_event(self, event_id, **kwargs):  # noqa: E501
        """RetrieveRegisteredEvent  # noqa: E501

        Retrieve a registered event  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_registered_event(event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_id: (required)
        :return: GetEventResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_registered_event_with_http_info(event_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_registered_event_with_http_info(event_id, **kwargs)  # noqa: E501
            return data

    def retrieve_registered_event_with_http_info(self, event_id, **kwargs):  # noqa: E501
        """RetrieveRegisteredEvent  # noqa: E501

        Retrieve a registered event  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_registered_event_with_http_info(event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_id: (required)
        :return: GetEventResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_registered_event" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_id' is set
        if ('event_id' not in params or
                params['event_id'] is None):
            raise ValueError("Missing the required parameter `event_id` when calling `retrieve_registered_event`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_id' in params:
            path_params['event_id'] = params['event_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['httpBearer']  # noqa: E501

        return self.api_client.call_api(
            '/events/{event_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetEventResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_registered_event(self, event_id, **kwargs):  # noqa: E501
        """UpdateRegisteredEvent  # noqa: E501

        Update a registered event. If the `active` query paramter is provided with a value of true or false, the event will be activated/deactivated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_registered_event(event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_id: (required)
        :param UpdateRegisteredEventRequest body:
        :param bool active:
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_registered_event_with_http_info(event_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_registered_event_with_http_info(event_id, **kwargs)  # noqa: E501
            return data

    def update_registered_event_with_http_info(self, event_id, **kwargs):  # noqa: E501
        """UpdateRegisteredEvent  # noqa: E501

        Update a registered event. If the `active` query paramter is provided with a value of true or false, the event will be activated/deactivated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_registered_event_with_http_info(event_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str event_id: (required)
        :param UpdateRegisteredEventRequest body:
        :param bool active:
        :return: Generic200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_id', 'body', 'active']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_registered_event" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_id' is set
        if ('event_id' not in params or
                params['event_id'] is None):
            raise ValueError("Missing the required parameter `event_id` when calling `update_registered_event`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'event_id' in params:
            path_params['event_id'] = params['event_id']  # noqa: E501

        query_params = []
        if 'active' in params:
            query_params.append(('active', params['active']))  # noqa: E501

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
        auth_settings = ['httpBearer']  # noqa: E501

        return self.api_client.call_api(
            '/events/{event_id}', 'PUT',
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
