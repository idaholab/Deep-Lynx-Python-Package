# deep_lynx.GraphApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_edge**](GraphApi.md#archive_edge) | **DELETE** /containers/{container_id}/graphs/edges/{edge_id} | ArchiveEdge
[**archive_node**](GraphApi.md#archive_node) | **DELETE** /containers/{container_id}/graphs/nodes/{node_id} | ArchiveNode
[**attach_edge_file**](GraphApi.md#attach_edge_file) | **PUT** /containers/{container_id}/graphs/edges/{edge_id}/files/{file_id} | AttachEdgeFile
[**attach_node_file**](GraphApi.md#attach_node_file) | **PUT** /containers/{container_id}/graphs/nodes/{node_id}/files/{file_id} | AttachNodeFile
[**create_or_update_edges**](GraphApi.md#create_or_update_edges) | **POST** /containers/{container_id}/graphs/edges | CreateOrUpdateEdges
[**create_or_update_nodes**](GraphApi.md#create_or_update_nodes) | **POST** /containers/{container_id}/graphs/nodes | CreateOrUpdateNodes
[**delete_node_file**](GraphApi.md#delete_node_file) | **DELETE** /containers/{container_id}/graphs/nodes/{node_id}/files/{file_id} | DeleteNodeFile
[**detach_node_file**](GraphApi.md#detach_node_file) | **DELETE** /containers/{container_id}/graphs/edges/{edge_id}/files/{file_id} | DetachNodeFile
[**list_edge_files**](GraphApi.md#list_edge_files) | **GET** /containers/{container_id}/graphs/edges/{edge_id}/files | ListEdgeFiles
[**list_edges**](GraphApi.md#list_edges) | **GET** /containers/{container_id}/graphs/edges | ListEdges
[**list_node_files**](GraphApi.md#list_node_files) | **GET** /containers/{container_id}/graphs/nodes/{node_id}/files | ListNodeFiles
[**list_nodes**](GraphApi.md#list_nodes) | **GET** /containers/{container_id}/graphs/nodes | ListNodes
[**list_nodesby_metatype_id**](GraphApi.md#list_nodesby_metatype_id) | **GET** /containers/{container_id}/graphs/nodes/metatype/{metatype_id} | ListNodesbyMetatypeID
[**retrieve_edge**](GraphApi.md#retrieve_edge) | **GET** /containers/{container_id}/graphs/edges/{edge_id} | RetrieveEdge
[**retrieve_node**](GraphApi.md#retrieve_node) | **GET** /containers/{container_id}/graphs/nodes/{node_id} | RetrieveNode

# **archive_edge**
> Generic200Response archive_edge(container_id, edge_id)

ArchiveEdge

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
    # ArchiveEdge
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_node**
> Generic200Response archive_node(container_id, node_id)

ArchiveNode

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
    # ArchiveNode
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_edge_file**
> Generic200Response attach_edge_file(container_id, file_id, edge_id)

AttachEdgeFile

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
    # AttachEdgeFile
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_node_file**
> Generic200Response attach_node_file(container_id, node_id, file_id)

AttachNodeFile

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
    # AttachNodeFile
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_edges**
> Generic200Response create_or_update_edges(container_id, body=body)

CreateOrUpdateEdges

This endpoint will either create new edges or update edges if a `modified_at` property with a valid DateTime is passed.

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
body = deep_lynx.CreateOrUpdateEdgesRequest() # CreateOrUpdateEdgesRequest |  (optional)

try:
    # CreateOrUpdateEdges
    api_response = api_instance.create_or_update_edges(container_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->create_or_update_edges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **body** | [**CreateOrUpdateEdgesRequest**](CreateOrUpdateEdgesRequest.md)|  | [optional] 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_nodes**
> Generic200Response create_or_update_nodes(body, container_id)

CreateOrUpdateNodes

This endpoint will either create new nodes or update nodes if a `modified_at` property with a valid DateTime is passed.

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
    # CreateOrUpdateNodes
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

[**Generic200Response**](Generic200Response.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node_file**
> Generic200Response delete_node_file(container_id, node_id, file_id)

DeleteNodeFile

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
    # DeleteNodeFile
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_node_file**
> Generic200Response detach_node_file(container_id, file_id, edge_id)

DetachNodeFile

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
    # DetachNodeFile
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edge_files**
> ListEdgeFiles list_edge_files(container_id, edge_id)

ListEdgeFiles

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
    # ListEdgeFiles
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_edges**
> ListEdgesResponse list_edges(container_id, limit=limit, offset=offset, origin_id=origin_id, destination_id=destination_id, relationship_pair_id=relationship_pair_id, relationship_pair_name=relationship_pair_name)

ListEdges

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

try:
    # ListEdges
    api_response = api_instance.list_edges(container_id, limit=limit, offset=offset, origin_id=origin_id, destination_id=destination_id, relationship_pair_id=relationship_pair_id, relationship_pair_name=relationship_pair_name)
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

### Return type

[**ListEdgesResponse**](ListEdgesResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_node_files**
> ListNodeFiles list_node_files(container_id, node_id)

ListNodeFiles

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
    # ListNodeFiles
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nodes**
> ListNodesResponse list_nodes(container_id, limit=limit, offset=offset, transformation_id=transformation_id, metatype_id=metatype_id)

ListNodes

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

try:
    # ListNodes
    api_response = api_instance.list_nodes(container_id, limit=limit, offset=offset, transformation_id=transformation_id, metatype_id=metatype_id)
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

### Return type

[**ListNodesResponse**](ListNodesResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nodesby_metatype_id**
> ListNodesResponse list_nodesby_metatype_id(container_id, metatype_id, limit=limit, offset=offset)

ListNodesbyMetatypeID

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
    # ListNodesbyMetatypeID
    api_response = api_instance.list_nodesby_metatype_id(container_id, metatype_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->list_nodesby_metatype_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **metatype_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**ListNodesResponse**](ListNodesResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_edge**
> GetEdgeResponse retrieve_edge(container_id, edge_id)

RetrieveEdge

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

try:
    # RetrieveEdge
    api_response = api_instance.retrieve_edge(container_id, edge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->retrieve_edge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **edge_id** | **str**|  | 

### Return type

[**GetEdgeResponse**](GetEdgeResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_node**
> GetNodeResponse retrieve_node(container_id, node_id)

RetrieveNode

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

try:
    # RetrieveNode
    api_response = api_instance.retrieve_node(container_id, node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GraphApi->retrieve_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **node_id** | **str**|  | 

### Return type

[**GetNodeResponse**](GetNodeResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

