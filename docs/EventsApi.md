# deep_lynx.EventsApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event**](EventsApi.md#create_event) | **POST** /events | Create Event
[**create_event_action**](EventsApi.md#create_event_action) | **POST** /event_actions | Create Event Action
[**delete_event_action**](EventsApi.md#delete_event_action) | **DELETE** /event_actions/{action_id} | Delete Event Action
[**list_event_action_statuses**](EventsApi.md#list_event_action_statuses) | **GET** /event_action_status | List Event Action Statuses
[**list_event_actions**](EventsApi.md#list_event_actions) | **GET** /event_actions | List Event Actions
[**retrieve_event_action**](EventsApi.md#retrieve_event_action) | **GET** /event_actions/{action_id} | Retrieve Event Action
[**retrieve_event_action_status**](EventsApi.md#retrieve_event_action_status) | **GET** /event_action_status/{status_id} | Retrieve Event Action Status
[**update_event_action**](EventsApi.md#update_event_action) | **PUT** /event_actions/{action_id} | Update Event Action
[**update_event_action_status**](EventsApi.md#update_event_action_status) | **PUT** /event_action_status/{status_id} | Update Event Action Status

# **create_event**
> CreateEventResponse create_event(body)

Create Event

Create new event

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateEventRequest() # CreateEventRequest | 

try:
    # Create Event
    api_response = api_instance.create_event(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->create_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEventRequest**](CreateEventRequest.md)|  | 

### Return type

[**CreateEventResponse**](CreateEventResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_action**
> CreateEventActionResponse create_event_action(body)

Create Event Action

Create an event action

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateEventActionRequest() # CreateEventActionRequest | 

try:
    # Create Event Action
    api_response = api_instance.create_event_action(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->create_event_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateEventActionRequest**](CreateEventActionRequest.md)|  | 

### Return type

[**CreateEventActionResponse**](CreateEventActionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_action**
> Generic200Response delete_event_action(action_id)

Delete Event Action

Delete an event action

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))
action_id = 'action_id_example' # str | 

try:
    # Delete Event Action
    api_response = api_instance.delete_event_action(action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->delete_event_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_action_statuses**
> ListEventActionStatusResponse list_event_action_statuses(event_id=event_id)

List Event Action Statuses

List all event action statuses

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))
event_id = 'event_id_example' # str | Filter returned statuses by the event ID (optional)

try:
    # List Event Action Statuses
    api_response = api_instance.list_event_action_statuses(event_id=event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->list_event_action_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**| Filter returned statuses by the event ID | [optional] 

### Return type

[**ListEventActionStatusResponse**](ListEventActionStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_actions**
> ListEventActionResponse list_event_actions()

List Event Actions

Lists all event actions

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))

try:
    # List Event Actions
    api_response = api_instance.list_event_actions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->list_event_actions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListEventActionResponse**](ListEventActionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_event_action**
> GetEventActionResponse retrieve_event_action(action_id)

Retrieve Event Action

Retrieve an event action

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))
action_id = 'action_id_example' # str | 

try:
    # Retrieve Event Action
    api_response = api_instance.retrieve_event_action(action_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->retrieve_event_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **str**|  | 

### Return type

[**GetEventActionResponse**](GetEventActionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_event_action_status**
> GetEventActionStatusResponse retrieve_event_action_status(status_id)

Retrieve Event Action Status

Retrieve an event action status

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))
status_id = 'status_id_example' # str | 

try:
    # Retrieve Event Action Status
    api_response = api_instance.retrieve_event_action_status(status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->retrieve_event_action_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **str**|  | 

### Return type

[**GetEventActionStatusResponse**](GetEventActionStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_action**
> UpdateEventActionResponse update_event_action(action_id, body=body, active=active)

Update Event Action

Update an event action

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))
action_id = 'action_id_example' # str | 
body = deep_lynx.CreateEventActionRequest() # CreateEventActionRequest |  (optional)
active = true # bool | Sets the event action active or inactive (optional)

try:
    # Update Event Action
    api_response = api_instance.update_event_action(action_id, body=body, active=active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->update_event_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_id** | **str**|  | 
 **body** | [**CreateEventActionRequest**](CreateEventActionRequest.md)|  | [optional] 
 **active** | **bool**| Sets the event action active or inactive | [optional] 

### Return type

[**UpdateEventActionResponse**](UpdateEventActionResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_action_status**
> UpdateEventActionStatusResponse update_event_action_status(status_id, body=body)

Update Event Action Status

Update an event action status

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))
status_id = 'status_id_example' # str | 
body = deep_lynx.UpdateEventActionStatusRequest() # UpdateEventActionStatusRequest |  (optional)

try:
    # Update Event Action Status
    api_response = api_instance.update_event_action_status(status_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->update_event_action_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **str**|  | 
 **body** | [**UpdateEventActionStatusRequest**](UpdateEventActionStatusRequest.md)|  | [optional] 

### Return type

[**UpdateEventActionStatusResponse**](UpdateEventActionStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

