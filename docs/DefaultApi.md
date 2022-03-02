# deep_lynx.DefaultApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_core_swagger_collection_yaml_paths1containers1_container_id1graphs1nodes1_node_id**](DefaultApi.md#get_core_swagger_collection_yaml_paths1containers1_container_id1graphs1nodes1_node_id) | **GET** /Core.swagger_collection.yaml/paths//containers/{container_id}/graphs/nodes/{node_id} | Nth Node Query

# **get_core_swagger_collection_yaml_paths1containers1_container_id1graphs1nodes1_node_id**
> get_core_swagger_collection_yaml_paths1containers1_container_id1graphs1nodes1_node_id(container_id, node_id)

Nth Node Query

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DefaultApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 

try:
    # Nth Node Query
    api_instance.get_core_swagger_collection_yaml_paths1containers1_container_id1graphs1nodes1_node_id(container_id, node_id)
except ApiException as e:
    print("Exception when calling DefaultApi->get_core_swagger_collection_yaml_paths1containers1_container_id1graphs1nodes1_node_id: %s\n" % e)
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

