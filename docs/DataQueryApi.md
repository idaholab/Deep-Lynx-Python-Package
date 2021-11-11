# deep_lynx.DataQueryApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_graph**](DataQueryApi.md#query_graph) | **POST** /containers/{container_id}/query | QueryGraph

# **query_graph**
> ContainersQueryResponse query_graph(body, container_id)

QueryGraph

Query the graph of the specified container using GraphQL. GraphQL queries may be formatted as json or plain text.

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
    # QueryGraph
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

[**ContainersQueryResponse**](ContainersQueryResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

