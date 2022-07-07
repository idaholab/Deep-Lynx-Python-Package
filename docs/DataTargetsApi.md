# deep_lynx.DataTargetsApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_data_target**](DataTargetsApi.md#archive_data_target) | **DELETE** /containers/{container_id}/export/datatargets/{data_target_id} | Archive Data Target
[**create_data_target**](DataTargetsApi.md#create_data_target) | **POST** /containers/{container_id}/export/datatargets | Create Data Target
[**list_dat_targets**](DataTargetsApi.md#list_dat_targets) | **GET** /containers/{container_id}/export/datatargets | List Data Targets
[**retrieve_data_target**](DataTargetsApi.md#retrieve_data_target) | **GET** /containers/{container_id}/export/datatargets/{data_target_id} | Retrieve Data Target
[**set_data_target_active**](DataTargetsApi.md#set_data_target_active) | **POST** /containers/{container_id}/export/datatargets/{data_target_id}/active | Set Data Target Active
[**set_data_target_configuration**](DataTargetsApi.md#set_data_target_configuration) | **PUT** /containers/{container_id}/export/datatargets/{data_target_id} | Set Data Target Configuration
[**set_data_target_inactive**](DataTargetsApi.md#set_data_target_inactive) | **DELETE** /containers/{container_id}/export/datatargets/{data_target_id}/active | Set Data Target Inactive

# **archive_data_target**
> Generic200Response archive_data_target(container_id, data_target_id, archive=archive, force_delete=force_delete)

Archive Data Target

Archive a data target, with options to permanently remove it.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTargetsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_target_id = 'data_target_id_example' # str | 
archive = 'archive_example' # str | Set to true to archive the data target. (optional)
force_delete = 'force_delete_example' # str | Set to true to force deletion of the data target. (optional)

try:
    # Archive Data Target
    api_response = api_instance.archive_data_target(container_id, data_target_id, archive=archive, force_delete=force_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTargetsApi->archive_data_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_target_id** | **str**|  | 
 **archive** | **str**| Set to true to archive the data target. | [optional] 
 **force_delete** | **str**| Set to true to force deletion of the data target. | [optional] 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_target**
> CreateDataTargetsResponse create_data_target(container_id, body=body)

Create Data Target

Create new datatarget. Supported data target types are `http` and `standard`.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTargetsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
body = deep_lynx.CreateDataTargetRequest() # CreateDataTargetRequest |  (optional)

try:
    # Create Data Target
    api_response = api_instance.create_data_target(container_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTargetsApi->create_data_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **body** | [**CreateDataTargetRequest**](CreateDataTargetRequest.md)|  | [optional] 

### Return type

[**CreateDataTargetsResponse**](CreateDataTargetsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dat_targets**
> ListDataTargetsResponse list_dat_targets(container_id)

List Data Targets

List the datatargets for the container.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTargetsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 

try:
    # List Data Targets
    api_response = api_instance.list_dat_targets(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTargetsApi->list_dat_targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 

### Return type

[**ListDataTargetsResponse**](ListDataTargetsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_data_target**
> GetDataTargetResponse retrieve_data_target(container_id, data_target_id)

Retrieve Data Target

Retrieve a single data target by ID.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTargetsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_target_id = 'data_target_id_example' # str | 

try:
    # Retrieve Data Target
    api_response = api_instance.retrieve_data_target(container_id, data_target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTargetsApi->retrieve_data_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_target_id** | **str**|  | 

### Return type

[**GetDataTargetResponse**](GetDataTargetResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_target_active**
> Generic200Response set_data_target_active(container_id, data_target_id)

Set Data Target Active

Sets a data target active.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTargetsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_target_id = 'data_target_id_example' # str | 

try:
    # Set Data Target Active
    api_response = api_instance.set_data_target_active(container_id, data_target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTargetsApi->set_data_target_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_target_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_target_configuration**
> UpdateDataTargetResponse set_data_target_configuration(body, container_id, data_target_id)

Set Data Target Configuration

Updates a data target's configuration in storage. Note that this request body's structure must match that of the data target's adapter type.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTargetsApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateDataTargetConfig() # CreateDataTargetConfig | 
container_id = 'container_id_example' # str | 
data_target_id = 'data_target_id_example' # str | 

try:
    # Set Data Target Configuration
    api_response = api_instance.set_data_target_configuration(body, container_id, data_target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTargetsApi->set_data_target_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDataTargetConfig**](CreateDataTargetConfig.md)|  | 
 **container_id** | **str**|  | 
 **data_target_id** | **str**|  | 

### Return type

[**UpdateDataTargetResponse**](UpdateDataTargetResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_target_inactive**
> Generic200Response set_data_target_inactive(container_id, data_target_id)

Set Data Target Inactive

Sets a data target inactive.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTargetsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_target_id = 'data_target_id_example' # str | 

try:
    # Set Data Target Inactive
    api_response = api_instance.set_data_target_inactive(container_id, data_target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTargetsApi->set_data_target_inactive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_target_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

