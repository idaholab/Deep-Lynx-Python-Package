# deep_lynx.TimeSeriesApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeseries_data_source_query**](TimeSeriesApi.md#timeseries_data_source_query) | **POST** /containers/{container_id}/import/datasources/{data_source_id}/data | Timeseries Data Source Query
[**timeseries_node_query**](TimeSeriesApi.md#timeseries_node_query) | **POST** /containers/{container_id}/graphs/nodes/{node_id}/timeseries | Timeseries Node Query

# **timeseries_data_source_query**
> InlineResponse2002 timeseries_data_source_query(body, container_id, data_source_id)

Timeseries Data Source Query

This is an endpoint that accepts a GraphQL query and returns the results of that query. Primarily used for working with time series data without requiring attachment to a node.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TimeSeriesApi(deep_lynx.ApiClient(configuration))
body = NULL # object | 
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 

try:
    # Timeseries Data Source Query
    api_response = api_instance.timeseries_data_source_query(body, container_id, data_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->timeseries_data_source_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, text/plain, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **timeseries_node_query**
> InlineResponse2002 timeseries_node_query(body, container_id, node_id)

Timeseries Node Query

This is an endpoint that accepts a GraphQL query and returns the results of that query. Primarily used for working with time series data that is attached to a specific node.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TimeSeriesApi(deep_lynx.ApiClient(configuration))
body = NULL # object | 
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 

try:
    # Timeseries Node Query
    api_response = api_instance.timeseries_node_query(body, container_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeSeriesApi->timeseries_node_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **container_id** | **str**|  | 
 **node_id** | **str**|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, text/plain, application/xml
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

