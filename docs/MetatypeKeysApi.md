# deep_lynx.MetatypeKeysApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_metatype_key**](MetatypeKeysApi.md#archive_metatype_key) | **DELETE** /containers/{container_id}/metatypes/{metatype_id}/keys/{key_id} | Archive Metatype Key
[**create_metatype_key**](MetatypeKeysApi.md#create_metatype_key) | **POST** /containers/{container_id}/metatypes/{metatype_id}/keys | Create Metatype Key
[**list_metatypes_keys**](MetatypeKeysApi.md#list_metatypes_keys) | **GET** /containers/{container_id}/metatypes/{metatype_id}/keys | List Metatype&#x27;s Keys
[**retrieve_metatype_key**](MetatypeKeysApi.md#retrieve_metatype_key) | **GET** /containers/{container_id}/metatypes/{metatype_id}/keys/{key_id} | Retrieve Metatype Key
[**update_metatype_key**](MetatypeKeysApi.md#update_metatype_key) | **PUT** /containers/{container_id}/metatypes/{metatype_id}/keys/{key_id} | Update Metatype Key

# **archive_metatype_key**
> Generic200Response archive_metatype_key(container_id, metatype_id, key_id)

Archive Metatype Key

Archiving the metatype key prevents any new types from implementing the key. It *does not remove key/value pairs on existing types*. We highly recommend you archive type keys instead of deleting them so that previous data is not affected.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeKeysApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
metatype_id = 'metatype_id_example' # str | 
key_id = 'key_id_example' # str | 

try:
    # Archive Metatype Key
    api_response = api_instance.archive_metatype_key(container_id, metatype_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeKeysApi->archive_metatype_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **metatype_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metatype_key**
> CreateMetatypeKeysResponse create_metatype_key(body, container_id, metatype_id)

Create Metatype Key

Creates a new key for a metatype. Keys consist of a unique key name (unique to the metatype only), key type, default values, and allowed values. Of those, only the first two are required. The `dataType` field accepts only one of the following values: number, string, date, boolean, enumeration, file. The fields `defaultValue` and `options` will only accept an array of the following types: string, boolean, number, float. Pass in an array for bulk creation. Currently the validation and cardinality functionality of keys are NOT checked at data insertion.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeKeysApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateMetatypeKeyRequest() # CreateMetatypeKeyRequest | 
container_id = 'container_id_example' # str | 
metatype_id = 'metatype_id_example' # str | 

try:
    # Create Metatype Key
    api_response = api_instance.create_metatype_key(body, container_id, metatype_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeKeysApi->create_metatype_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMetatypeKeyRequest**](CreateMetatypeKeyRequest.md)|  | 
 **container_id** | **str**|  | 
 **metatype_id** | **str**|  | 

### Return type

[**CreateMetatypeKeysResponse**](CreateMetatypeKeysResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metatypes_keys**
> ListMetatypeKeysResponse list_metatypes_keys(container_id, metatype_id)

List Metatype's Keys

Lists all currently valid and available keys for the metatype.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeKeysApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
metatype_id = 'metatype_id_example' # str | 

try:
    # List Metatype's Keys
    api_response = api_instance.list_metatypes_keys(container_id, metatype_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeKeysApi->list_metatypes_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **metatype_id** | **str**|  | 

### Return type

[**ListMetatypeKeysResponse**](ListMetatypeKeysResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_metatype_key**
> GetMetatypeKeyResponse retrieve_metatype_key(container_id, metatype_id, key_id)

Retrieve Metatype Key

Retrieve the specified key for the metatype.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeKeysApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
metatype_id = 'metatype_id_example' # str | 
key_id = 'key_id_example' # str | 

try:
    # Retrieve Metatype Key
    api_response = api_instance.retrieve_metatype_key(container_id, metatype_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeKeysApi->retrieve_metatype_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **metatype_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

[**GetMetatypeKeyResponse**](GetMetatypeKeyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metatype_key**
> UpdateMetatypeKeyResponse update_metatype_key(body, container_id, metatype_id, key_id)

Update Metatype Key

Updates a single key for a metatype.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeKeysApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.MetatypeKey() # MetatypeKey | 
container_id = 'container_id_example' # str | 
metatype_id = 'metatype_id_example' # str | 
key_id = 'key_id_example' # str | 

try:
    # Update Metatype Key
    api_response = api_instance.update_metatype_key(body, container_id, metatype_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeKeysApi->update_metatype_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetatypeKey**](MetatypeKey.md)|  | 
 **container_id** | **str**|  | 
 **metatype_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

[**UpdateMetatypeKeyResponse**](UpdateMetatypeKeyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

