# deep_lynx.EventsApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_registered_event**](EventsApi.md#create_registered_event) | **POST** /events | CreateRegisteredEvent
[**delete_registered_event**](EventsApi.md#delete_registered_event) | **DELETE** /events/{event_id} | DeleteRegisteredEvent
[**list_registered_events**](EventsApi.md#list_registered_events) | **GET** /events | ListRegisteredEvents
[**retrieve_registered_event**](EventsApi.md#retrieve_registered_event) | **GET** /events/{event_id} | RetrieveRegisteredEvent
[**update_registered_event**](EventsApi.md#update_registered_event) | **PUT** /events/{event_id} | UpdateRegisteredEvent

# **create_registered_event**
> CreateEventResponse create_registered_event(body)

CreateRegisteredEvent

Create new registered event. An `app_name`, `app_url`, and `event_type` must be provided. Either a `container_id` or `data_source_id` must also be provided.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateRegisteredEventRequest() # CreateRegisteredEventRequest | 

try:
    # CreateRegisteredEvent
    api_response = api_instance.create_registered_event(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->create_registered_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRegisteredEventRequest**](CreateRegisteredEventRequest.md)|  | 

### Return type

[**CreateEventResponse**](CreateEventResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registered_event**
> Generic200Response delete_registered_event(event_id)

DeleteRegisteredEvent

Delete a registered event.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))
event_id = 'event_id_example' # str | 

try:
    # DeleteRegisteredEvent
    api_response = api_instance.delete_registered_event(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->delete_registered_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_registered_events**
> ListEventsResponse list_registered_events()

ListRegisteredEvents

Lists all registered events

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
    # ListRegisteredEvents
    api_response = api_instance.list_registered_events()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->list_registered_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListEventsResponse**](ListEventsResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_registered_event**
> GetEventResponse retrieve_registered_event(event_id)

RetrieveRegisteredEvent

Retrieve a registered event

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))
event_id = 'event_id_example' # str | 

try:
    # RetrieveRegisteredEvent
    api_response = api_instance.retrieve_registered_event(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->retrieve_registered_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

[**GetEventResponse**](GetEventResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_registered_event**
> Generic200Response update_registered_event(event_id, body=body, active=active)

UpdateRegisteredEvent

Update a registered event. If the `active` query paramter is provided with a value of true or false, the event will be activated/deactivated.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.EventsApi(deep_lynx.ApiClient(configuration))
event_id = 'event_id_example' # str | 
body = deep_lynx.UpdateRegisteredEventRequest() # UpdateRegisteredEventRequest |  (optional)
active = true # bool |  (optional)

try:
    # UpdateRegisteredEvent
    api_response = api_instance.update_registered_event(event_id, body=body, active=active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->update_registered_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 
 **body** | [**UpdateRegisteredEventRequest**](UpdateRegisteredEventRequest.md)|  | [optional] 
 **active** | **bool**|  | [optional] 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

