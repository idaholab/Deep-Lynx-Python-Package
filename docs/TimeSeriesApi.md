# deep_lynx.TimeSeriesApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeseries_node_query**](TimeSeriesApi.md#timeseries_node_query) | **POST** /containers/{container_id}/graphs/nodes/{node_id}/timeseries | Timeseries Node Query

# **timeseries_node_query**
> timeseries_node_query(container_id, node_id)

Timeseries Node Query

This is an endpoint that accepts a GraphQL query and returns the results of that query. Primarily used for working with time series data on nodes.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TimeSeriesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 

try:
    # Timeseries Node Query
    api_instance.timeseries_node_query(container_id, node_id)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->timeseries_node_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **node_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

