# deep_lynx.ContainersApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_container**](ContainersApi.md#archive_container) | **DELETE** /containers/{container_id} | ArchiveContainer
[**container_batch_update**](ContainersApi.md#container_batch_update) | **PUT** /containers | ContainerBatchUpdate
[**create_container**](ContainersApi.md#create_container) | **POST** /containers | CreateContainer
[**import_container**](ContainersApi.md#import_container) | **POST** /containers/import | ImportContainer
[**list_containers**](ContainersApi.md#list_containers) | **GET** /containers | ListContainers
[**repair_container_permissions**](ContainersApi.md#repair_container_permissions) | **POST** /containers/{container_id}/permissions | RepairContainerPermissions
[**retrieve_container**](ContainersApi.md#retrieve_container) | **GET** /containers/{container_id} | RetrieveContainer
[**set_container_active**](ContainersApi.md#set_container_active) | **POST** /containers/{container_id}/active | SetContainerActive
[**update_container**](ContainersApi.md#update_container) | **PUT** /containers/{container_id} | UpdateContainer
[**update_container_import**](ContainersApi.md#update_container_import) | **PUT** /containers/import/{container_id} | UpdateContainerImport

# **archive_container**
> Generic200Response archive_container(container_id, permanent=permanent)

ArchiveContainer

Archives a Container. This is preferred over deletion as deletion has a cascading effect on the deleted type's keys, relationships, and relationship keys. When in doubt, archive over delete. We'd rather have tombstones than cremating the type.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ContainersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
permanent = true # bool | If true, permanently deletes the container (optional)

try:
    # ArchiveContainer
    api_response = api_instance.archive_container(container_id, permanent=permanent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->archive_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **permanent** | **bool**| If true, permanently deletes the container | [optional] 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **container_batch_update**
> BatchUpdateContainerResponse container_batch_update(body)

ContainerBatchUpdate

Accepts an array of container objects - will attempt to update all of them in a single transaction. If the update fails, none of them will go through.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ContainersApi(deep_lynx.ApiClient(configuration))
body = [deep_lynx.BatchContainerUpdateRequest()] # list[BatchContainerUpdateRequest] | 

try:
    # ContainerBatchUpdate
    api_response = api_instance.container_batch_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->container_batch_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[BatchContainerUpdateRequest]**](BatchContainerUpdateRequest.md)|  | 

### Return type

[**BatchUpdateContainerResponse**](BatchUpdateContainerResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_container**
> CreateContainerResponse create_container(body)

CreateContainer

Creates a new container object. Containers are the root level object and are considered to contain both the ontology(in form of Metatypes, Metatype Keys, and MetatypeRelationships) as well as the data stored under that ontology.  Endpoint will accept both a single container request object, or an array of container request objects

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ContainersApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateContainerRequest() # CreateContainerRequest | 

try:
    # CreateContainer
    api_response = api_instance.create_container(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->create_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateContainerRequest**](CreateContainerRequest.md)|  | 

### Return type

[**CreateContainerResponse**](CreateContainerResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_container**
> ContainerImportResponse import_container(content_type, name=name, description=description, data_versioning_enabled=data_versioning_enabled, path=path, file=file, dryrun=dryrun)

ImportContainer

An optional query param `dryrun` may be included with a value of `true` in order to return a HTML formatted string explaining the name and description of the container along with the number of metatypes, metatype relationships, and metatype keys to be created. This request uses a form-data body. If the ontology to be imported is being referenced via url, provide the url via a `path` field. Otherwise a local file may be provided. A file takes precedence over a `path` value if both are provided.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ContainersApi(deep_lynx.ApiClient(configuration))
content_type = 'content_type_example' # str | 
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
data_versioning_enabled = true # bool |  (optional)
path = 'path_example' # str |  (optional)
file = 'file_example' # str |  (optional)
dryrun = true # bool | If true returns a description of the container that will be created and its contents. (optional)

try:
    # ImportContainer
    api_response = api_instance.import_container(content_type, name=name, description=description, data_versioning_enabled=data_versioning_enabled, path=path, file=file, dryrun=dryrun)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->import_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **data_versioning_enabled** | **bool**|  | [optional] 
 **path** | **str**|  | [optional] 
 **file** | **str**|  | [optional] 
 **dryrun** | **bool**| If true returns a description of the container that will be created and its contents. | [optional] 

### Return type

[**ContainerImportResponse**](ContainerImportResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_containers**
> ListContainerResponse list_containers()

ListContainers

List all containers.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ContainersApi(deep_lynx.ApiClient(configuration))

try:
    # ListContainers
    api_response = api_instance.list_containers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->list_containers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListContainerResponse**](ListContainerResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repair_container_permissions**
> Generic200Response repair_container_permissions(container_id)

RepairContainerPermissions

Repairs a container's permission set

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ContainersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 

try:
    # RepairContainerPermissions
    api_response = api_instance.repair_container_permissions(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->repair_container_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_container**
> GetContainerResponse retrieve_container(container_id)

RetrieveContainer

Retrieve container by ID.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ContainersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 

try:
    # RetrieveContainer
    api_response = api_instance.retrieve_container(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->retrieve_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 

### Return type

[**GetContainerResponse**](GetContainerResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_container_active**
> Generic200Response set_container_active(container_id)

SetContainerActive

Unarchives a Container. This is the only way to update this value of a container via API.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ContainersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 

try:
    # SetContainerActive
    api_response = api_instance.set_container_active(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->set_container_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_container**
> UpdateContainerResponse update_container(body, container_id)

UpdateContainer

Updates the container. This will fail if a container already exists with the proposed updated name.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ContainersApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.UpdateContainerRequest() # UpdateContainerRequest | 
container_id = 'container_id_example' # str | 

try:
    # UpdateContainer
    api_response = api_instance.update_container(body, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->update_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateContainerRequest**](UpdateContainerRequest.md)|  | 
 **container_id** | **str**|  | 

### Return type

[**UpdateContainerResponse**](UpdateContainerResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_container_import**
> ContainerImportUpdateResponse update_container_import(content_type, container_id, name=name, description=description, data_versioning_enabled=data_versioning_enabled, path=path, file=file)

UpdateContainerImport

Updates an existing container via an ontology file.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ContainersApi(deep_lynx.ApiClient(configuration))
content_type = 'content_type_example' # str | 
container_id = 'container_id_example' # str | 
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
data_versioning_enabled = true # bool |  (optional)
path = 'path_example' # str |  (optional)
file = 'file_example' # str |  (optional)

try:
    # UpdateContainerImport
    api_response = api_instance.update_container_import(content_type, container_id, name=name, description=description, data_versioning_enabled=data_versioning_enabled, path=path, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->update_container_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | 
 **container_id** | **str**|  | 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **data_versioning_enabled** | **bool**|  | [optional] 
 **path** | **str**|  | [optional] 
 **file** | **str**|  | [optional] 

### Return type

[**ContainerImportUpdateResponse**](ContainerImportUpdateResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

