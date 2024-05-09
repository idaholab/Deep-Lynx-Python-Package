# deep_lynx.DataQueryApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_query**](DataQueryApi.md#data_query) | **POST** /containers/{container_id}/data | Query Data
[**query_graph**](DataQueryApi.md#query_graph) | **POST** /containers/{container_id}/query | Query Graph (Deprecated)

# **data_query**
> InlineResponse2002 data_query(body, container_id, raw_metadata_enabled=raw_metadata_enabled, point_in_time=point_in_time)

Query Data

Query data from your container using GraphQL. You can learn more here - https://github.com/idaholab/Deep-Lynx/wiki/Querying-Data-With-GraphQL

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataQueryApi(deep_lynx.ApiClient(configuration))
body = NULL # object | 
container_id = 'container_id_example' # str | 
raw_metadata_enabled = false # bool |  (optional) (default to false)
point_in_time = 'point_in_time_example' # str |  (optional)

try:
    # Query Data
    api_response = api_instance.data_query(body, container_id, raw_metadata_enabled=raw_metadata_enabled, point_in_time=point_in_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataQueryApi->data_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **container_id** | **str**|  | 
 **raw_metadata_enabled** | **bool**|  | [optional] [default to false]
 **point_in_time** | **str**|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, text/plain, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_graph**
> InlineResponse2002 query_graph(body, container_id)

Query Graph (Deprecated)

Query the graph of the specified container using GraphQL. GraphQL queries may be formatted as json or plain text. This has been deprecated in favor of the `/containers/{container_id}/data` endpoint.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataQueryApi(deep_lynx.ApiClient(configuration))
body = NULL # object | 
container_id = 'container_id_example' # str | 

try:
    # Query Graph (Deprecated)
    api_response = api_instance.query_graph(body, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataQueryApi->query_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **container_id** | **str**|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

