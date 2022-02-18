# deep_lynx.ContainersApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledge_container_alert**](ContainersApi.md#acknowledge_container_alert) | **POST** /containers/{container_id}/alerts/{alert_id} | Acknowledge Container Alert
[**approve_ontology_version**](ContainersApi.md#approve_ontology_version) | **PUT** /containers/{container_id}/ontology/versions/{ontology_version_id}/approve | Approve Ontology Version
[**archive_container**](ContainersApi.md#archive_container) | **DELETE** /containers/{container_id} | Archive Container
[**container_batch_update**](ContainersApi.md#container_batch_update) | **PUT** /containers | Container Batch Update
[**create_container**](ContainersApi.md#create_container) | **POST** /containers | Create Container
[**import_container**](ContainersApi.md#import_container) | **POST** /containers/import | Import Container
[**list_container_alerts**](ContainersApi.md#list_container_alerts) | **GET** /containers/{container_id}/alerts | List Container Alerts
[**list_containers**](ContainersApi.md#list_containers) | **GET** /containers | List Containers
[**list_ontology_versions**](ContainersApi.md#list_ontology_versions) | **GET** /containers/{container_id}/ontology/versions | List Ontology Versions
[**publish_ontology_version**](ContainersApi.md#publish_ontology_version) | **POST** /containers/{container_id}/ontology/versions/{ontology_version_id}/publish | Publish Ontology Version
[**reject_ontology_version_approval**](ContainersApi.md#reject_ontology_version_approval) | **DELETE** /containers/{container_id}/ontology/versions/{ontology_version_id}/approve | Reject Ontology Version Approval
[**repair_container_permissions**](ContainersApi.md#repair_container_permissions) | **POST** /containers/{container_id}/permissions | Repair Container Permissions
[**retrieve_container**](ContainersApi.md#retrieve_container) | **GET** /containers/{container_id} | Retrieve Container
[**retrieve_ontology_version**](ContainersApi.md#retrieve_ontology_version) | **GET** /containers/{container_id}/ontology/versions/{version_id} | Retrieve Ontology Version
[**rollback_ontology_version**](ContainersApi.md#rollback_ontology_version) | **POST** /containers/{container_id}/ontology/versions/{version_id}/rollback | Rollback Ontology Version
[**send_ontology_version_for_approval**](ContainersApi.md#send_ontology_version_for_approval) | **POST** /containers/{container_id}/ontology/versions/{ontology_version_id}/approve | Send Ontology Version for Approval
[**set_container_active**](ContainersApi.md#set_container_active) | **POST** /containers/{container_id}/active | Set Container Active
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

# **approve_ontology_version**
> approve_ontology_version(container_id, ontology_version_id)

Approve Ontology Version

Approves an ontology version

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
ontology_version_id = 'ontology_version_id_example' # str | 

try:
    # Approve Ontology Version
    api_instance.approve_ontology_version(container_id, ontology_version_id)
except ApiException as e:
    print("Exception when calling ContainersApi->approve_ontology_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **ontology_version_id** | **str**|  | 

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
> InlineResponse2001 list_ontology_versions(container_id)

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

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_ontology_version**
> publish_ontology_version(container_id, ontology_version_id)

Publish Ontology Version

Publishes an ontology version

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
ontology_version_id = 'ontology_version_id_example' # str | 

try:
    # Publish Ontology Version
    api_instance.publish_ontology_version(container_id, ontology_version_id)
except ApiException as e:
    print("Exception when calling ContainersApi->publish_ontology_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **ontology_version_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_ontology_version_approval**
> reject_ontology_version_approval(container_id, ontology_version_id)

Reject Ontology Version Approval

Rejects an ontology version (either in a pending status or after it has been approved).

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
ontology_version_id = 'ontology_version_id_example' # str | 

try:
    # Reject Ontology Version Approval
    api_instance.reject_ontology_version_approval(container_id, ontology_version_id)
except ApiException as e:
    print("Exception when calling ContainersApi->reject_ontology_version_approval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **ontology_version_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

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

# **retrieve_ontology_version**
> InlineResponse2002 retrieve_ontology_version(container_id, version_id)

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

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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

# **send_ontology_version_for_approval**
> send_ontology_version_for_approval(container_id, ontology_version_id)

Send Ontology Version for Approval

Sends an ontology version to be approved by a container admin

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
ontology_version_id = 'ontology_version_id_example' # str | 

try:
    # Send Ontology Version for Approval
    api_instance.send_ontology_version_for_approval(container_id, ontology_version_id)
except ApiException as e:
    print("Exception when calling ContainersApi->send_ontology_version_for_approval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **ontology_version_id** | **str**|  | 

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

