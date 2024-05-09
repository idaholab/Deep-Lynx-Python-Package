# deep_lynx.GraphApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_edge**](GraphApi.md#archive_edge) | **DELETE** /containers/{container_id}/graphs/edges/{edge_id} | Archive Edge
[**archive_node**](GraphApi.md#archive_node) | **DELETE** /containers/{container_id}/graphs/nodes/{node_id} | Archive Node
[**attach_edge_file**](GraphApi.md#attach_edge_file) | **PUT** /containers/{container_id}/graphs/edges/{edge_id}/files/{file_id} | Attach Edge File
[**attach_node_file**](GraphApi.md#attach_node_file) | **PUT** /containers/{container_id}/graphs/nodes/{node_id}/files/{file_id} | Attach Node File
[**create_or_update_edges**](GraphApi.md#create_or_update_edges) | **POST** /containers/{container_id}/graphs/edges | Create or Update Edges
[**create_or_update_nodes**](GraphApi.md#create_or_update_nodes) | **POST** /containers/{container_id}/graphs/nodes | Create Or Update Nodes
[**delete_node_file**](GraphApi.md#delete_node_file) | **DELETE** /containers/{container_id}/graphs/nodes/{node_id}/files/{file_id} | Detach Node File
[**detach_node_file**](GraphApi.md#detach_node_file) | **DELETE** /containers/{container_id}/graphs/edges/{edge_id}/files/{file_id} | Detach Node File
[**list_edge_files**](GraphApi.md#list_edge_files) | **GET** /containers/{container_id}/graphs/edges/{edge_id}/files | List Edge Files
[**list_edges**](GraphApi.md#list_edges) | **GET** /containers/{container_id}/graphs/edges | List Edges
[**list_edges_for_node_ids**](GraphApi.md#list_edges_for_node_ids) | **POST** /containers/{container_id}/graphs/nodes/edges | List Edges for Node IDs
[**list_node_files**](GraphApi.md#list_node_files) | **GET** /containers/{container_id}/graphs/nodes/{node_id}/files | List Node Files
[**list_nodes**](GraphApi.md#list_nodes) | **GET** /containers/{container_id}/graphs/nodes | List Nodes
[**list_nodes_by_metatype_id**](GraphApi.md#list_nodes_by_metatype_id) | **GET** /containers/{container_id}/graphs/nodes/metatype/{metatype_id} | List Nodes By Metatype ID
[**retrieve_edge**](GraphApi.md#retrieve_edge) | **GET** /containers/{container_id}/graphs/edges/{edge_id} | Retrieve Edge
[**retrieve_node**](GraphApi.md#retrieve_node) | **GET** /containers/{container_id}/graphs/nodes/{node_id} | Retrieve Node
[**retrieve_nth_nodes**](GraphApi.md#retrieve_nth_nodes) | **GET** /containers/{container_id}/graphs/nodes/{node_id}/graph | Nth Node Query
[**timeseries_data_source_query**](GraphApi.md#timeseries_data_source_query) | **POST** /containers/{container_id}/import/datasources/{data_source_id}/data | Timeseries Data Source Query
[**timeseries_node_query**](GraphApi.md#timeseries_node_query) | **POST** /containers/{container_id}/graphs/nodes/{node_id}/timeseries | Timeseries Node Query

# **archive_edge**
> Generic200Response archive_edge(container_id, edge_id)

Archive Edge

Archives an edge

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
edge_id = 'edge_id_example' # str | 

try:
    # Archive Edge
    api_response = api_instance.archive_edge(container_id, edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->archive_edge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **edge_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_node**
> Generic200Response archive_node(container_id, node_id)

Archive Node

Archives a node

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 

try:
    # Archive Node
    api_response = api_instance.archive_node(container_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->archive_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **node_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_edge_file**
> Generic200Response attach_edge_file(container_id, file_id, edge_id)

Attach Edge File

Attach a file to an edge.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
file_id = 'file_id_example' # str | 
edge_id = 'edge_id_example' # str | 

try:
    # Attach Edge File
    api_response = api_instance.attach_edge_file(container_id, file_id, edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->attach_edge_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **file_id** | **str**|  | 
 **edge_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_node_file**
> Generic200Response attach_node_file(container_id, node_id, file_id)

Attach Node File

Attach a file to a node.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 
file_id = 'file_id_example' # str | 

try:
    # Attach Node File
    api_response = api_instance.attach_node_file(container_id, node_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->attach_node_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **node_id** | **str**|  | 
 **file_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_edges**
> InlineResponse2006 create_or_update_edges(body, container_id)

Create or Update Edges

This endpoint will attempt to create a connection between two nodes. You can either pass in the node's DeepLynx IDs, or the node's original id, metatype id, and data source id to create these edges.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateOrUpdateEdgesRequest() # CreateOrUpdateEdgesRequest | 
container_id = 'container_id_example' # str | 

try:
    # Create or Update Edges
    api_response = api_instance.create_or_update_edges(body, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->create_or_update_edges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateEdgesRequest**](CreateOrUpdateEdgesRequest.md)|  | 
 **container_id** | **str**|  | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_nodes**
> InlineResponse2003 create_or_update_nodes(body, container_id)

Create Or Update Nodes

This endpoint will either create new nodes or update nodes if one with the same original_id is passed.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateOrUpdateNodesRequest() # CreateOrUpdateNodesRequest | 
container_id = 'container_id_example' # str | 

try:
    # Create Or Update Nodes
    api_response = api_instance.create_or_update_nodes(body, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->create_or_update_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateNodesRequest**](CreateOrUpdateNodesRequest.md)|  | 
 **container_id** | **str**|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_file**
> Generic200Response delete_node_file(container_id, node_id, file_id)

Detach Node File

Detach file from node

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 
file_id = 'file_id_example' # str | 

try:
    # Detach Node File
    api_response = api_instance.delete_node_file(container_id, node_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->delete_node_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **node_id** | **str**|  | 
 **file_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_node_file**
> Generic200Response detach_node_file(container_id, file_id, edge_id)

Detach Node File

Detach file from an edge.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
file_id = 'file_id_example' # str | 
edge_id = 'edge_id_example' # str | 

try:
    # Detach Node File
    api_response = api_instance.detach_node_file(container_id, file_id, edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->detach_node_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **file_id** | **str**|  | 
 **edge_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edge_files**
> ListEdgeFiles list_edge_files(container_id, edge_id)

List Edge Files

Lists all attached files for edge.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
edge_id = 'edge_id_example' # str | 

try:
    # List Edge Files
    api_response = api_instance.list_edge_files(container_id, edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->list_edge_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **edge_id** | **str**|  | 

### Return type

[**ListEdgeFiles**](ListEdgeFiles.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edges**
> ListEdgesResponse list_edges(container_id, limit=limit, offset=offset, origin_id=origin_id, destination_id=destination_id, relationship_pair_id=relationship_pair_id, relationship_pair_name=relationship_pair_name, history=history)

List Edges

List Edges from storage

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
origin_id = 'origin_id_example' # str |  (optional)
destination_id = 'destination_id_example' # str |  (optional)
relationship_pair_id = 'relationship_pair_id_example' # str |  (optional)
relationship_pair_name = 'relationship_pair_name_example' # str |  (optional)
history = true # bool |  (optional)

try:
    # List Edges
    api_response = api_instance.list_edges(container_id, limit=limit, offset=offset, origin_id=origin_id, destination_id=destination_id, relationship_pair_id=relationship_pair_id, relationship_pair_name=relationship_pair_name, history=history)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->list_edges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **origin_id** | **str**|  | [optional] 
 **destination_id** | **str**|  | [optional] 
 **relationship_pair_id** | **str**|  | [optional] 
 **relationship_pair_name** | **str**|  | [optional] 
 **history** | **bool**|  | [optional] 

### Return type

[**ListEdgesResponse**](ListEdgesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edges_for_node_ids**
> ListEdgesForNodeIDsResponse list_edges_for_node_ids(container_id, body=body)

List Edges for Node IDs

Takes an array of node IDs and returns the given edges for those nodes

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
body = deep_lynx.NodesEdgesBody() # NodesEdgesBody |  (optional)

try:
    # List Edges for Node IDs
    api_response = api_instance.list_edges_for_node_ids(container_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->list_edges_for_node_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **body** | [**NodesEdgesBody**](NodesEdgesBody.md)|  | [optional] 

### Return type

[**ListEdgesForNodeIDsResponse**](ListEdgesForNodeIDsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_files**
> ListNodeFiles list_node_files(container_id, node_id)

List Node Files

Lists all attached files for node.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 

try:
    # List Node Files
    api_response = api_instance.list_node_files(container_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->list_node_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **node_id** | **str**|  | 

### Return type

[**ListNodeFiles**](ListNodeFiles.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nodes**
> ListNodesResponse list_nodes(container_id, limit=limit, offset=offset, transformation_id=transformation_id, metatype_id=metatype_id, data_source_id=data_source_id, history=history)

List Nodes

List nodes

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
transformation_id = 'transformation_id_example' # str | Return only nodes for the selected type transformation (optional)
metatype_id = 'metatype_id_example' # str | Return only nodes for the selected metatype (optional)
data_source_id = 'data_source_id_example' # str | Return only nodes for the selected datasource (optional)
history = true # bool | Return historical data for all selected nodes (optional)

try:
    # List Nodes
    api_response = api_instance.list_nodes(container_id, limit=limit, offset=offset, transformation_id=transformation_id, metatype_id=metatype_id, data_source_id=data_source_id, history=history)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->list_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **transformation_id** | **str**| Return only nodes for the selected type transformation | [optional] 
 **metatype_id** | **str**| Return only nodes for the selected metatype | [optional] 
 **data_source_id** | **str**| Return only nodes for the selected datasource | [optional] 
 **history** | **bool**| Return historical data for all selected nodes | [optional] 

### Return type

[**ListNodesResponse**](ListNodesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nodes_by_metatype_id**
> ListNodesByMetatypeResponse list_nodes_by_metatype_id(container_id, metatype_id, limit=limit, offset=offset)

List Nodes By Metatype ID

List Nodes, filter by MetatypeID

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
metatype_id = 'metatype_id_example' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)

try:
    # List Nodes By Metatype ID
    api_response = api_instance.list_nodes_by_metatype_id(container_id, metatype_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->list_nodes_by_metatype_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **metatype_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**ListNodesByMetatypeResponse**](ListNodesByMetatypeResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_edge**
> GetEdgeResponse retrieve_edge(container_id, edge_id, history=history)

Retrieve Edge

Retrieve a single edge

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
edge_id = 'edge_id_example' # str | 
history = true # bool |  (optional)

try:
    # Retrieve Edge
    api_response = api_instance.retrieve_edge(container_id, edge_id, history=history)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->retrieve_edge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **edge_id** | **str**|  | 
 **history** | **bool**|  | [optional] 

### Return type

[**GetEdgeResponse**](GetEdgeResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_node**
> GetNodeResponse retrieve_node(container_id, node_id, history=history)

Retrieve Node

Retrieve a single node from storage.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 
history = true # bool |  (optional)

try:
    # Retrieve Node
    api_response = api_instance.retrieve_node(container_id, node_id, history=history)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->retrieve_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **node_id** | **str**|  | 
 **history** | **bool**|  | [optional] 

### Return type

[**GetNodeResponse**](GetNodeResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_nth_nodes**
> InlineResponse2004 retrieve_nth_nodes(container_id, node_id, depth=depth)

Nth Node Query

Retrieve n layers of node-edge relationships given a depth n and an origin node id.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 
depth = '10' # str | Number of layers deep to query. Defaults to 10. (optional) (default to 10)

try:
    # Nth Node Query
    api_response = api_instance.retrieve_nth_nodes(container_id, node_id, depth=depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->retrieve_nth_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **node_id** | **str**|  | 
 **depth** | **str**| Number of layers deep to query. Defaults to 10. | [optional] [default to 10]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
body = NULL # object | 
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 

try:
    # Timeseries Data Source Query
    api_response = api_instance.timeseries_data_source_query(body, container_id, data_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->timeseries_data_source_query: %s\n" % e)
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
api_instance = deep_lynx.GraphApi(deep_lynx.ApiClient(configuration))
body = NULL # object | 
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 

try:
    # Timeseries Node Query
    api_response = api_instance.timeseries_node_query(body, container_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->timeseries_node_query: %s\n" % e)
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

