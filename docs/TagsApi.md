# deep_lynx.TagsApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_webgl_file**](TagsApi.md#delete_webgl_file) | **DELETE** /containers/{container_id}/graphs/webgl/files/{file_id} | Delete WebGL File
[**detach_tag_from_edge**](TagsApi.md#detach_tag_from_edge) | **DELETE** /containers/{container_id}/graphs/tags/{tag_id}/edges/{edge_id} | Detach Tag From Edge
[**detach_tag_from_file**](TagsApi.md#detach_tag_from_file) | **DELETE** /containers/{container_id}/graphs/tags/{tag_id}/files/{file_id} | Detach Tag From File
[**detach_tag_from_node**](TagsApi.md#detach_tag_from_node) | **DELETE** /containers/{container_id}/graphs/tags/{tag_id}/nodes/{node_id} | Detach Tag From Node
[**get_containers_container_id_graphs_tags_edges_edge_id**](TagsApi.md#get_containers_container_id_graphs_tags_edges_edge_id) | **GET** /containers/{container_id}/graphs/tags/edges/{edge_id} | List Tags for Edge
[**get_containers_container_id_graphs_tags_files_file_id**](TagsApi.md#get_containers_container_id_graphs_tags_files_file_id) | **GET** /containers/{container_id}/graphs/tags/files/{file_id} | List Tags for File
[**get_containers_container_id_graphs_tags_nodes_node_id**](TagsApi.md#get_containers_container_id_graphs_tags_nodes_node_id) | **GET** /containers/{container_id}/graphs/tags/nodes/{node_id} | List Tags for Node
[**get_containers_container_id_graphs_tags_nodes_tag_id**](TagsApi.md#get_containers_container_id_graphs_tags_nodes_tag_id) | **GET** /containers/{container_id}/graphs/tags/{tag_id}/nodes | List Nodes with Tag
[**get_containers_container_id_graphs_tags_tag_id_edges**](TagsApi.md#get_containers_container_id_graphs_tags_tag_id_edges) | **GET** /containers/{container_id}/graphs/tags/{tag_id}/edges | List Edges with Tag
[**get_containers_container_id_graphs_tags_tag_id_files**](TagsApi.md#get_containers_container_id_graphs_tags_tag_id_files) | **GET** /containers/{container_id}/graphs/tags/{tag_id}/files | List Files with Tag
[**list_tags**](TagsApi.md#list_tags) | **GET** /containers/{container_id}/graphs/tags | List Tags
[**list_webgl**](TagsApi.md#list_webgl) | **GET** /containers/{container_id}/graphs/webgl | List WebGL
[**post_tags**](TagsApi.md#post_tags) | **POST** /containers/{container_id}/graphs/tags | Create Tag
[**put_containers_container_id_graphs_tags_nodes_node_id**](TagsApi.md#put_containers_container_id_graphs_tags_nodes_node_id) | **PUT** /containers/{container_id}/graphs/tags/{tag_id}/nodes/{node_id} | Tag Node
[**put_containers_container_id_graphs_tags_tag_id**](TagsApi.md#put_containers_container_id_graphs_tags_tag_id) | **PUT** /containers/{container_id}/graphs/tags/{tag_id} | Update Tag
[**put_containers_container_id_graphs_tags_tag_id_edges_edge_id**](TagsApi.md#put_containers_container_id_graphs_tags_tag_id_edges_edge_id) | **PUT** /containers/{container_id}/graphs/tags/{tag_id}/edges/{edge_id} | Tag Edge
[**put_containers_container_id_graphs_tags_tag_id_files_file_id**](TagsApi.md#put_containers_container_id_graphs_tags_tag_id_files_file_id) | **PUT** /containers/{container_id}/graphs/tags/{tag_id}/files/{file_id} | Tag File
[**update_webgl_files**](TagsApi.md#update_webgl_files) | **GET** /containers/{container_id}/graphs/webgl/files/{file_id} | Update WebGL Files
[**upload_webgl**](TagsApi.md#upload_webgl) | **POST** /containers/{container_id}/graphs/webgl | Upload WebGL

# **delete_webgl_file**
> delete_webgl_file(container_id, file_id)

Delete WebGL File

Deletes a WebGL file.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
file_id = 'file_id_example' # str | 

try:
    # Delete WebGL File
    api_instance.delete_webgl_file(container_id, file_id)
except ApiException as e:
    print("Exception when calling TagsApi->delete_webgl_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **file_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_tag_from_edge**
> detach_tag_from_edge(container_id, edge_id, tag_id)

Detach Tag From Edge

Removes the connection between a tag and an edge

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
edge_id = 'edge_id_example' # str | 
tag_id = 'tag_id_example' # str | 

try:
    # Detach Tag From Edge
    api_instance.detach_tag_from_edge(container_id, edge_id, tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->detach_tag_from_edge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **edge_id** | **str**|  | 
 **tag_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_tag_from_file**
> detach_tag_from_file(container_id, file_id, tag_id)

Detach Tag From File

Removes the connection between a tag and a file

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
file_id = 'file_id_example' # str | 
tag_id = 'tag_id_example' # str | 

try:
    # Detach Tag From File
    api_instance.detach_tag_from_file(container_id, file_id, tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->detach_tag_from_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **file_id** | **str**|  | 
 **tag_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_tag_from_node**
> detach_tag_from_node(container_id, node_id, tag_id)

Detach Tag From Node

Removes the connection between a tag and a node

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 
tag_id = 'tag_id_example' # str | 

try:
    # Detach Tag From Node
    api_instance.detach_tag_from_node(container_id, node_id, tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->detach_tag_from_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **node_id** | **str**|  | 
 **tag_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_containers_container_id_graphs_tags_edges_edge_id**
> get_containers_container_id_graphs_tags_edges_edge_id(container_id, edge_id)

List Tags for Edge

List all Tags for an Edge

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
edge_id = 'edge_id_example' # str | 

try:
    # List Tags for Edge
    api_instance.get_containers_container_id_graphs_tags_edges_edge_id(container_id, edge_id)
except ApiException as e:
    print("Exception when calling TagsApi->get_containers_container_id_graphs_tags_edges_edge_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **edge_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_containers_container_id_graphs_tags_files_file_id**
> get_containers_container_id_graphs_tags_files_file_id(container_id, file_id)

List Tags for File

List all Tags for a File

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
file_id = 'file_id_example' # str | 

try:
    # List Tags for File
    api_instance.get_containers_container_id_graphs_tags_files_file_id(container_id, file_id)
except ApiException as e:
    print("Exception when calling TagsApi->get_containers_container_id_graphs_tags_files_file_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **file_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_containers_container_id_graphs_tags_nodes_node_id**
> get_containers_container_id_graphs_tags_nodes_node_id(container_id, node_id)

List Tags for Node

List all Tags on a Node

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 

try:
    # List Tags for Node
    api_instance.get_containers_container_id_graphs_tags_nodes_node_id(container_id, node_id)
except ApiException as e:
    print("Exception when calling TagsApi->get_containers_container_id_graphs_tags_nodes_node_id: %s\n" % e)
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

# **get_containers_container_id_graphs_tags_nodes_tag_id**
> get_containers_container_id_graphs_tags_nodes_tag_id(container_id, tag_id)

List Nodes with Tag

List all Nodes with a Tag

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
tag_id = 'tag_id_example' # str | 

try:
    # List Nodes with Tag
    api_instance.get_containers_container_id_graphs_tags_nodes_tag_id(container_id, tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->get_containers_container_id_graphs_tags_nodes_tag_id: %s\n" % e)
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

# **get_containers_container_id_graphs_tags_tag_id_edges**
> get_containers_container_id_graphs_tags_tag_id_edges(container_id, tag_id)

List Edges with Tag

List all Edges with Tag

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
tag_id = 'tag_id_example' # str | 

try:
    # List Edges with Tag
    api_instance.get_containers_container_id_graphs_tags_tag_id_edges(container_id, tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->get_containers_container_id_graphs_tags_tag_id_edges: %s\n" % e)
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

# **get_containers_container_id_graphs_tags_tag_id_files**
> get_containers_container_id_graphs_tags_tag_id_files(container_id, tag_id)

List Files with Tag

List all Files with Tag

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
tag_id = 'tag_id_example' # str | 

try:
    # List Files with Tag
    api_instance.get_containers_container_id_graphs_tags_tag_id_files(container_id, tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->get_containers_container_id_graphs_tags_tag_id_files: %s\n" % e)
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

# **list_tags**
> list_tags(container_id)

List Tags

List all tags for a container

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 

try:
    # List Tags
    api_instance.list_tags(container_id)
except ApiException as e:
    print("Exception when calling TagsApi->list_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webgl**
> list_webgl(container_id)

List WebGL

Lists all WebGL files and tags for a container.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 

try:
    # List WebGL
    api_instance.list_webgl(container_id)
except ApiException as e:
    print("Exception when calling TagsApi->list_webgl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tags**
> post_tags(container_id, body=body)

Create Tag

Create a Tag

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
body = deep_lynx.GraphsTagsBody() # GraphsTagsBody |  (optional)

try:
    # Create Tag
    api_instance.post_tags(container_id, body=body)
except ApiException as e:
    print("Exception when calling TagsApi->post_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **body** | [**GraphsTagsBody**](GraphsTagsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_containers_container_id_graphs_tags_nodes_node_id**
> put_containers_container_id_graphs_tags_nodes_node_id(container_id, node_id, tag_id)

Tag Node

Attach Tag to Node

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
node_id = 'node_id_example' # str | 
tag_id = 'tag_id_example' # str | 

try:
    # Tag Node
    api_instance.put_containers_container_id_graphs_tags_nodes_node_id(container_id, node_id, tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->put_containers_container_id_graphs_tags_nodes_node_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **node_id** | **str**|  | 
 **tag_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_containers_container_id_graphs_tags_tag_id**
> put_containers_container_id_graphs_tags_tag_id(container_id, tag_id, body=body)

Update Tag

Update a tag

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
tag_id = 'tag_id_example' # str | 
body = deep_lynx.TagsTagIdBody() # TagsTagIdBody |  (optional)

try:
    # Update Tag
    api_instance.put_containers_container_id_graphs_tags_tag_id(container_id, tag_id, body=body)
except ApiException as e:
    print("Exception when calling TagsApi->put_containers_container_id_graphs_tags_tag_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **tag_id** | **str**|  | 
 **body** | [**TagsTagIdBody**](TagsTagIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_containers_container_id_graphs_tags_tag_id_edges_edge_id**
> put_containers_container_id_graphs_tags_tag_id_edges_edge_id(container_id, edge_id, tag_id)

Tag Edge

Tag an Edge

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
edge_id = 'edge_id_example' # str | 
tag_id = 'tag_id_example' # str | 

try:
    # Tag Edge
    api_instance.put_containers_container_id_graphs_tags_tag_id_edges_edge_id(container_id, edge_id, tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->put_containers_container_id_graphs_tags_tag_id_edges_edge_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **edge_id** | **str**|  | 
 **tag_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_containers_container_id_graphs_tags_tag_id_files_file_id**
> put_containers_container_id_graphs_tags_tag_id_files_file_id(container_id, file_id, tag_id)

Tag File

Tag a File

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
file_id = 'file_id_example' # str | 
tag_id = 'tag_id_example' # str | 

try:
    # Tag File
    api_instance.put_containers_container_id_graphs_tags_tag_id_files_file_id(container_id, file_id, tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->put_containers_container_id_graphs_tags_tag_id_files_file_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **file_id** | **str**|  | 
 **tag_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webgl_files**
> update_webgl_files(container_id, file_id)

Update WebGL Files

Updates WebGL files.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
file_id = 'file_id_example' # str | 

try:
    # Update WebGL Files
    api_instance.update_webgl_files(container_id, file_id)
except ApiException as e:
    print("Exception when calling TagsApi->update_webgl_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **file_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_webgl**
> upload_webgl(container_id, file=file, tag=tag)

Upload WebGL

Upload a WebGL build. The tag will be created if it doesn't exist, and the file will be uploaded. The tag is then associated with the file. The tag will automatically have {'webgl': true} added to its metadata field

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TagsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
file = NULL # object |  (optional)
tag = 'tag_example' # str | Tag name (optional)

try:
    # Upload WebGL
    api_instance.upload_webgl(container_id, file=file, tag=tag)
except ApiException as e:
    print("Exception when calling TagsApi->upload_webgl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **file** | [**object**](.md)|  | [optional] 
 **tag** | **str**| Tag name | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

