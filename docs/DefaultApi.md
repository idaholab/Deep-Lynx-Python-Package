# deep_lynx.DefaultApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_containers_container_id_graphs_tags_tag_id_edges**](DefaultApi.md#delete_containers_container_id_graphs_tags_tag_id_edges) | **DELETE** /containers/{container_id}/graphs/tags/{tag_id}/edges | Bulk Detach Tag from Edges
[**delete_containers_container_id_graphs_tags_tag_id_nodes**](DefaultApi.md#delete_containers_container_id_graphs_tags_tag_id_nodes) | **DELETE** /containers/{container_id}/graphs/tags/{tag_id}/nodes | Bulk Detach Tag from Nodes
[**list_ts_for_node**](DefaultApi.md#list_ts_for_node) | **GET** /containers/{container_id}/graphs/nodes/{node_id}/timeseries | List Timeseries Sources for Node
[**post_containers_container_id_data_source_templates**](DefaultApi.md#post_containers_container_id_data_source_templates) | **POST** /containers/{container_id}/data_source_templates | Save Data Source Templates
[**put_containers_container_id_graphs_tags_tag_id_edges**](DefaultApi.md#put_containers_container_id_graphs_tags_tag_id_edges) | **PUT** /containers/{container_id}/graphs/tags/{tag_id}/edges | Bulk Add Tag to Edge
[**put_containers_container_id_graphs_tags_tag_id_nodes**](DefaultApi.md#put_containers_container_id_graphs_tags_tag_id_nodes) | **PUT** /containers/{container_id}/graphs/tags/{tag_id}/nodes | Bulk Add Tag to Nodes

# **delete_containers_container_id_graphs_tags_tag_id_edges**
> delete_containers_container_id_graphs_tags_tag_id_edges(container_id, tag_id)

Bulk Detach Tag from Edges

Detach Tag from Multiple Edges

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
tag_id = 'tag_id_example' # str | 

try:
    # Bulk Detach Tag from Edges
    api_instance.delete_containers_container_id_graphs_tags_tag_id_edges(container_id, tag_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_containers_container_id_graphs_tags_tag_id_edges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **tag_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_containers_container_id_graphs_tags_tag_id_nodes**
> delete_containers_container_id_graphs_tags_tag_id_nodes(container_id, tag_id)

Bulk Detach Tag from Nodes

Detach Tag from Multiple Nodes

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
tag_id = 'tag_id_example' # str | 

try:
    # Bulk Detach Tag from Nodes
    api_instance.delete_containers_container_id_graphs_tags_tag_id_nodes(container_id, tag_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_containers_container_id_graphs_tags_tag_id_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **tag_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ts_for_node**
> InlineResponse2005 list_ts_for_node(container_id, node_id)

List Timeseries Sources for Node

Returns a dictionary of source names and source IDs for each source attached to the given node.

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
    # List Timeseries Sources for Node
    api_response = api_instance.list_ts_for_node(container_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_ts_for_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **node_id** | **str**|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_containers_container_id_data_source_templates**
> InlineResponse2001 post_containers_container_id_data_source_templates(container_id, body=body)

Save Data Source Templates

Add a new Data Source Template to the container or create a new Data Source Template.

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
body = [deep_lynx.ContainerIdDataSourceTemplatesBody()] # list[ContainerIdDataSourceTemplatesBody] |  (optional)

try:
    # Save Data Source Templates
    api_response = api_instance.post_containers_container_id_data_source_templates(container_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_containers_container_id_data_source_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **body** | [**list[ContainerIdDataSourceTemplatesBody]**](ContainerIdDataSourceTemplatesBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_containers_container_id_graphs_tags_tag_id_edges**
> put_containers_container_id_graphs_tags_tag_id_edges(container_id, tag_id, body=body)

Bulk Add Tag to Edge

Add Tag to Multiple Edges

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
tag_id = 'tag_id_example' # str | 
body = deep_lynx.TagIdEdgesBody() # TagIdEdgesBody |  (optional)

try:
    # Bulk Add Tag to Edge
    api_instance.put_containers_container_id_graphs_tags_tag_id_edges(container_id, tag_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->put_containers_container_id_graphs_tags_tag_id_edges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **tag_id** | **str**|  | 
 **body** | [**TagIdEdgesBody**](TagIdEdgesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_containers_container_id_graphs_tags_tag_id_nodes**
> put_containers_container_id_graphs_tags_tag_id_nodes(container_id, tag_id, body=body)

Bulk Add Tag to Nodes

Add Tag to Multiple Nodes

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
tag_id = 'tag_id_example' # str | 
body = deep_lynx.TagIdNodesBody() # TagIdNodesBody |  (optional)

try:
    # Bulk Add Tag to Nodes
    api_instance.put_containers_container_id_graphs_tags_tag_id_nodes(container_id, tag_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->put_containers_container_id_graphs_tags_tag_id_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **tag_id** | **str**|  | 
 **body** | [**TagIdNodesBody**](TagIdNodesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

