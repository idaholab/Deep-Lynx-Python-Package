# deep_lynx.MetatypeRelationshipKeysApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_metatype_relationship_key**](MetatypeRelationshipKeysApi.md#archive_metatype_relationship_key) | **DELETE** /containers/{container_id}/metatype_relationships/{relationship_id}/keys/{key_id} | ArchiveMetatypeRelationshipKey
[**create_metatype_relationship_key**](MetatypeRelationshipKeysApi.md#create_metatype_relationship_key) | **POST** /containers/{container_id}/metatype_relationships/{relationship_id}/keys | CreateMetatypeRelationshipKey
[**list_metatype_relationship_keys**](MetatypeRelationshipKeysApi.md#list_metatype_relationship_keys) | **GET** /containers/{container_id}/metatype_relationships/{relationship_id}/keys | ListMetatypeRelationshipKeys
[**retrieve_metatype_relationship_key**](MetatypeRelationshipKeysApi.md#retrieve_metatype_relationship_key) | **GET** /containers/{container_id}/metatype_relationships/{relationship_id}/keys/{key_id} | RetrieveMetatypeRelationshipKey
[**update_metatype_relationship_key**](MetatypeRelationshipKeysApi.md#update_metatype_relationship_key) | **PUT** /containers/{container_id}/metatype_relationships/{relationship_id}/keys/{key_id} | UpdateMetatypeRelationshipKey

# **archive_metatype_relationship_key**
> Generic200Response archive_metatype_relationship_key(container_id, relationship_id, key_id)

ArchiveMetatypeRelationshipKey

Archives a Metatype Relationship Key.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipKeysApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
relationship_id = 'relationship_id_example' # str | 
key_id = 'key_id_example' # str | 

try:
    # ArchiveMetatypeRelationshipKey
    api_response = api_instance.archive_metatype_relationship_key(container_id, relationship_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipKeysApi->archive_metatype_relationship_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **relationship_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metatype_relationship_key**
> CreateMetatypeRelationshipKeysResponse create_metatype_relationship_key(body, container_id, relationship_id)

CreateMetatypeRelationshipKey

Creates a new key for a metatype relationship. Keys consist of a unique key name (unique to the metatype relationship), key type, default values, and allowed values. Of those, only the first two are required.  The `dataType` field accepts only one of the following values: number, string, date, boolean, enumeration, file.   The fields `defaultValue` and `options` will only accept an array of the following types: string, boolean, number, float.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipKeysApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.NewMetatypeRelationshipKeyRequest() # NewMetatypeRelationshipKeyRequest | 
container_id = 'container_id_example' # str | 
relationship_id = 'relationship_id_example' # str | 

try:
    # CreateMetatypeRelationshipKey
    api_response = api_instance.create_metatype_relationship_key(body, container_id, relationship_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipKeysApi->create_metatype_relationship_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NewMetatypeRelationshipKeyRequest**](NewMetatypeRelationshipKeyRequest.md)|  | 
 **container_id** | **str**|  | 
 **relationship_id** | **str**|  | 

### Return type

[**CreateMetatypeRelationshipKeysResponse**](CreateMetatypeRelationshipKeysResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metatype_relationship_keys**
> ListMetatypeRelationshipKeysResponse list_metatype_relationship_keys(container_id, relationship_id)

ListMetatypeRelationshipKeys

Retrieves all keys for a Metatype Relationship.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipKeysApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
relationship_id = 'relationship_id_example' # str | 

try:
    # ListMetatypeRelationshipKeys
    api_response = api_instance.list_metatype_relationship_keys(container_id, relationship_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipKeysApi->list_metatype_relationship_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **relationship_id** | **str**|  | 

### Return type

[**ListMetatypeRelationshipKeysResponse**](ListMetatypeRelationshipKeysResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_metatype_relationship_key**
> GetMetatypeRelationshipKeyResponse retrieve_metatype_relationship_key(container_id, relationship_id, key_id)

RetrieveMetatypeRelationshipKey

Retrieve a single key for a Metatype Relationship by id.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipKeysApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
relationship_id = 'relationship_id_example' # str | 
key_id = 'key_id_example' # str | 

try:
    # RetrieveMetatypeRelationshipKey
    api_response = api_instance.retrieve_metatype_relationship_key(container_id, relationship_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipKeysApi->retrieve_metatype_relationship_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **relationship_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

[**GetMetatypeRelationshipKeyResponse**](GetMetatypeRelationshipKeyResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metatype_relationship_key**
> UpdateMetatypeRelationshipKeyResponse update_metatype_relationship_key(body, container_id, relationship_id, key_id)

UpdateMetatypeRelationshipKey

Updates a Metatype Relationship key. The update must follow the same format as creation.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipKeysApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.RelationshipKey() # RelationshipKey | 
container_id = 'container_id_example' # str | 
relationship_id = 'relationship_id_example' # str | 
key_id = 'key_id_example' # str | 

try:
    # UpdateMetatypeRelationshipKey
    api_response = api_instance.update_metatype_relationship_key(body, container_id, relationship_id, key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipKeysApi->update_metatype_relationship_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RelationshipKey**](RelationshipKey.md)|  | 
 **container_id** | **str**|  | 
 **relationship_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

[**UpdateMetatypeRelationshipKeyResponse**](UpdateMetatypeRelationshipKeyResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

