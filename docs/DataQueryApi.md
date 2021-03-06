# deep_lynx.DataQueryApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_query**](DataQueryApi.md#data_query) | **POST** /containers/{container_id}/data | Query Data
[**query_graph**](DataQueryApi.md#query_graph) | **POST** /containers/{container_id}/query | Query Graph (Deprecated)

# **data_query**
> InlineResponse200 data_query(body, container_id)

Query Data

Query data from your container using GraphQL. You can learn more here - https://gitlab.software.inl.gov/b650/Deep-Lynx/-/wikis/Querying-Data-With-GraphQL

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
    # Query Data
    api_response = api_instance.data_query(body, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataQueryApi->data_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **container_id** | **str**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_graph**
> InlineResponse200 query_graph(body, container_id)

Query Graph (Deprecated)

Query the graph of the specified container using GraphQL. GraphQL queries may be formatted as json or plain text.  This has been deprecated in favor of the `/containers/{container_id}/data` endpoint.

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

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

