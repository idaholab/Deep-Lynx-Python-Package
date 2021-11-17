# deep_lynx.ContainersApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_container**](ContainersApi.md#archive_container) | **DELETE** /containers/{container_id} | Archive Container
[**container_batch_update**](ContainersApi.md#container_batch_update) | **PUT** /containers | Container Batch Update
[**create_container**](ContainersApi.md#create_container) | **POST** /containers | Create Container
[**import_container**](ContainersApi.md#import_container) | **POST** /containers/import | Import Container
[**list_containers**](ContainersApi.md#list_containers) | **GET** /containers | List Containers
[**repair_container_permissions**](ContainersApi.md#repair_container_permissions) | **POST** /containers/{container_id}/permissions | Repair Container Permissions
[**retrieve_container**](ContainersApi.md#retrieve_container) | **GET** /containers/{container_id} | Retrieve Container
[**set_container_active**](ContainersApi.md#set_container_active) | **POST** /containers/{container_id}/active | Set Container Active
[**update_container**](ContainersApi.md#update_container) | **PUT** /containers/{container_id} | Update Container
[**update_container_import**](ContainersApi.md#update_container_import) | **PUT** /containers/import/{container_id} | Update Container Import

# **archive_container**
> Generic200Response archive_container(container_id, permanent=permanent)

Archive Container

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
    # Archive Container
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **container_batch_update**
> BatchUpdateContainerResponse container_batch_update(body)

Container Batch Update

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
body = [deep_lynx.BatchContainerUpdateRequestInner()] # list[BatchContainerUpdateRequestInner] | 

try:
    # Container Batch Update
    api_response = api_instance.container_batch_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->container_batch_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[BatchContainerUpdateRequestInner]**](BatchContainerUpdateRequestInner.md)|  | 

### Return type

[**BatchUpdateContainerResponse**](BatchUpdateContainerResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_container**
> CreateContainerResponse create_container(body)

Create Container

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
    # Create Container
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_container**
> ContainerImportResponse import_container(name, description, data_versioning_enabled, path, file, dryrun=dryrun)

Import Container

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
name = 'name_example' # str | 
description = 'description_example' # str | 
data_versioning_enabled = true # bool | 
path = 'path_example' # str | 
file = 'file_example' # str | 
dryrun = true # bool | If true returns a description of the container that will be created and its contents. (optional)

try:
    # Import Container
    api_response = api_instance.import_container(name, description, data_versioning_enabled, path, file, dryrun=dryrun)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->import_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **description** | **str**|  | 
 **data_versioning_enabled** | **bool**|  | 
 **path** | **str**|  | 
 **file** | **str**|  | 
 **dryrun** | **bool**| If true returns a description of the container that will be created and its contents. | [optional] 

### Return type

[**ContainerImportResponse**](ContainerImportResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_containers**
> ListContainerResponse list_containers()

List Containers

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
    # List Containers
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repair_container_permissions**
> Generic200Response repair_container_permissions(container_id)

Repair Container Permissions

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
    # Repair Container Permissions
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_container**
> GetContainerResponse retrieve_container(container_id)

Retrieve Container

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
    # Retrieve Container
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_container_active**
> Generic200Response set_container_active(container_id)

Set Container Active

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
    # Set Container Active
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_container**
> UpdateContainerResponse update_container(body, container_id)

Update Container

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
    # Update Container
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_container_import**
> ContainerImportUpdateResponse update_container_import(name, description, data_versioning_enabled, path, file, container_id)

Update Container Import

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
name = 'name_example' # str | 
description = 'description_example' # str | 
data_versioning_enabled = true # bool | 
path = 'path_example' # str | 
file = 'file_example' # str | 
container_id = 'container_id_example' # str | 

try:
    # Update Container Import
    api_response = api_instance.update_container_import(name, description, data_versioning_enabled, path, file, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->update_container_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **description** | **str**|  | 
 **data_versioning_enabled** | **bool**|  | 
 **path** | **str**|  | 
 **file** | **str**|  | 
 **container_id** | **str**|  | 

### Return type

[**ContainerImportUpdateResponse**](ContainerImportUpdateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

