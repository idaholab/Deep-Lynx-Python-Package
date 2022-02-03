# deep_lynx.ContainersApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_container_alert**](ContainersApi.md#acknowledge_container_alert) | **POST** /containers/{container_id}/alerts/{alert_id} | Acknowledge Container Alert
[**apply_changelist**](ContainersApi.md#apply_changelist) | **GET** /containers/{container_id}/ontology/changelists/{changelistID}/apply | Apply Changelist
[**approve_changelist**](ContainersApi.md#approve_changelist) | **POST** /containers/{container_id}/ontology/changelists/{changelist_id}/approve | Approve Changelist
[**archive_container**](ContainersApi.md#archive_container) | **DELETE** /containers/{container_id} | Archive Container
[**container_batch_update**](ContainersApi.md#container_batch_update) | **PUT** /containers | Container Batch Update
[**create_container**](ContainersApi.md#create_container) | **POST** /containers | Create Container
[**create_new_changelist**](ContainersApi.md#create_new_changelist) | **POST** /containers/{container_id}/ontology/changelists | Create New Changelist
[**delete_changelist**](ContainersApi.md#delete_changelist) | **DELETE** /containers/{container_id}/ontology/changelists/{changelist_id} | Delete Changelist
[**import_container**](ContainersApi.md#import_container) | **POST** /containers/import | Import Container
[**list_changelist_approvals**](ContainersApi.md#list_changelist_approvals) | **GET** /containers/{container_id}/ontology/changelists/{changelist_id}/approve | List Approvals for Changelist
[**list_changelists**](ContainersApi.md#list_changelists) | **GET** /containers/{container_id}/ontology/changelists | List Changelists
[**list_container_alerts**](ContainersApi.md#list_container_alerts) | **GET** /containers/{container_id}/alerts | List Container Alerts
[**list_containers**](ContainersApi.md#list_containers) | **GET** /containers | List Containers
[**list_ontology_versions**](ContainersApi.md#list_ontology_versions) | **GET** /containers/{container_id}/ontology/versions | List Ontology Versions
[**repair_container_permissions**](ContainersApi.md#repair_container_permissions) | **POST** /containers/{container_id}/permissions | Repair Container Permissions
[**retrieve_changelist**](ContainersApi.md#retrieve_changelist) | **GET** /containers/{container_id}/ontology/changelists/{changelist_id} | Retrieve Changelist
[**retrieve_container**](ContainersApi.md#retrieve_container) | **GET** /containers/{container_id} | Retrieve Container
[**retrieve_ontology_version**](ContainersApi.md#retrieve_ontology_version) | **GET** /containers/{container_id}/ontology/versions/{version_id} | Retrieve Ontology Version
[**revoke_changelist_approval**](ContainersApi.md#revoke_changelist_approval) | **DELETE** /containers/{container_id}/ontology/changelists/{changelist_id}/approve | Revoke Changelist Approval
[**rollback_ontology_version**](ContainersApi.md#rollback_ontology_version) | **POST** /containers/{container_id}/ontology/versions/{version_id}/rollback | Rollback Ontology Version
[**set_container_active**](ContainersApi.md#set_container_active) | **POST** /containers/{container_id}/active | Set Container Active
[**update_changelist**](ContainersApi.md#update_changelist) | **PUT** /containers/{container_id}/ontology/changelists/{changelist_id} | Update Changelist
[**update_container**](ContainersApi.md#update_container) | **PUT** /containers/{container_id} | Update Container
[**update_container_import**](ContainersApi.md#update_container_import) | **PUT** /containers/import/{container_id} | Update Container Import

# **acknowledge_container_alert**
> acknowledge_container_alert(container_id, alert_id)

Acknowledge Container Alert

Post with no body to acknowledge an alert and remove it from the active alerts list.

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
alert_id = 'alert_id_example' # str | 

try:
    # Acknowledge Container Alert
    api_instance.acknowledge_container_alert(container_id, alert_id)
except ApiException as e:
    print("Exception when calling ContainersApi->acknowledge_container_alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **alert_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_changelist**
> apply_changelist(container_id, changelist_id)

Apply Changelist

Applies changelist to the ontology, creates a new ontology version.

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
changelist_id = 'changelist_id_example' # str | 

try:
    # Apply Changelist
    api_instance.apply_changelist(container_id, changelist_id)
except ApiException as e:
    print("Exception when calling ContainersApi->apply_changelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **changelist_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_changelist**
> approve_changelist(container_id, changelist_id)

Approve Changelist

Approves a changelist

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
changelist_id = 'changelist_id_example' # str | 

try:
    # Approve Changelist
    api_instance.approve_changelist(container_id, changelist_id)
except ApiException as e:
    print("Exception when calling ContainersApi->approve_changelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **changelist_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **create_new_changelist**
> InlineResponse2001 create_new_changelist(container_id, body=body)

Create New Changelist

Create a new changelist.

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
body = deep_lynx.OntologyChangelistsBody() # OntologyChangelistsBody |  (optional)

try:
    # Create New Changelist
    api_response = api_instance.create_new_changelist(container_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->create_new_changelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **body** | [**OntologyChangelistsBody**](OntologyChangelistsBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_changelist**
> delete_changelist(container_id, changelist_id)

Delete Changelist

Deletes a changelist

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
changelist_id = 'changelist_id_example' # str | 

try:
    # Delete Changelist
    api_instance.delete_changelist(container_id, changelist_id)
except ApiException as e:
    print("Exception when calling ContainersApi->delete_changelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **changelist_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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

# **list_changelist_approvals**
> InlineResponse2002 list_changelist_approvals(container_id, changelist_id)

List Approvals for Changelist

Approves a changelist for application. Note: you must still apply changelist after approval, this does not apply changelist.

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
changelist_id = 'changelist_id_example' # str | 

try:
    # List Approvals for Changelist
    api_response = api_instance.list_changelist_approvals(container_id, changelist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->list_changelist_approvals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **changelist_id** | **str**|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_changelists**
> ListChangelistResponse list_changelists(container_id)

List Changelists

List all changelists for a container. Will eventually support filters.

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
    # List Changelists
    api_response = api_instance.list_changelists(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->list_changelists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 

### Return type

[**ListChangelistResponse**](ListChangelistResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_container_alerts**
> list_container_alerts(container_id)

List Container Alerts

List all active alerts for a container by ID.

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
    # List Container Alerts
    api_instance.list_container_alerts(container_id)
except ApiException as e:
    print("Exception when calling ContainersApi->list_container_alerts: %s\n" % e)
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

# **list_ontology_versions**
> InlineResponse2003 list_ontology_versions(container_id)

List Ontology Versions

Lists all versions of the ontology for a container.

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
    # List Ontology Versions
    api_response = api_instance.list_ontology_versions(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->list_ontology_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

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

# **retrieve_changelist**
> RetrieveChangelistResponse retrieve_changelist(container_id, changelist_id)

Retrieve Changelist

Retrieve a changelist by id.

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
changelist_id = 'changelist_id_example' # str | 

try:
    # Retrieve Changelist
    api_response = api_instance.retrieve_changelist(container_id, changelist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->retrieve_changelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **changelist_id** | **str**|  | 

### Return type

[**RetrieveChangelistResponse**](RetrieveChangelistResponse.md)

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

# **retrieve_ontology_version**
> InlineResponse2004 retrieve_ontology_version(container_id, version_id)

Retrieve Ontology Version

Retreives details on a single ontology version.

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
version_id = 'version_id_example' # str | 

try:
    # Retrieve Ontology Version
    api_response = api_instance.retrieve_ontology_version(container_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->retrieve_ontology_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **version_id** | **str**|  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_changelist_approval**
> revoke_changelist_approval(container_id, changelist_id)

Revoke Changelist Approval

Removes all approvals for changelist.

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
changelist_id = 'changelist_id_example' # str | 

try:
    # Revoke Changelist Approval
    api_instance.revoke_changelist_approval(container_id, changelist_id)
except ApiException as e:
    print("Exception when calling ContainersApi->revoke_changelist_approval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **changelist_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_ontology_version**
> rollback_ontology_version(container_id, version_id)

Rollback Ontology Version

Rolls back the ontology to the selected version.

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
version_id = 'version_id_example' # str | 

try:
    # Rollback Ontology Version
    api_instance.rollback_ontology_version(container_id, version_id)
except ApiException as e:
    print("Exception when calling ContainersApi->rollback_ontology_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **version_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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

# **update_changelist**
> InlineResponse2001 update_changelist(container_id, changelist_id, body=body)

Update Changelist

Update a changelist.

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
changelist_id = 'changelist_id_example' # str | 
body = deep_lynx.ChangelistsChangelistIdBody() # ChangelistsChangelistIdBody |  (optional)

try:
    # Update Changelist
    api_response = api_instance.update_changelist(container_id, changelist_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->update_changelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **changelist_id** | **str**|  | 
 **body** | [**ChangelistsChangelistIdBody**](ChangelistsChangelistIdBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
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

