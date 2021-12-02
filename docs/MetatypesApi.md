# deep_lynx.MetatypesApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_metatype**](MetatypesApi.md#archive_metatype) | **DELETE** /containers/{container_id}/metatypes/{metatype_id} | Archive Metatype
[**create_metatype**](MetatypesApi.md#create_metatype) | **POST** /containers/{container_id}/metatypes | Create Metatype
[**list_metatypes**](MetatypesApi.md#list_metatypes) | **GET** /containers/{container_id}/metatypes | List Metatypes
[**retrieve_metaype**](MetatypesApi.md#retrieve_metaype) | **GET** /containers/{container_id}/metatypes/{metatype_id} | Retrieve Metatype
[**update_metatype**](MetatypesApi.md#update_metatype) | **PUT** /containers/{container_id}/metatypes/{metatype_id} | Update Metatype
[**validate_metatype_properties**](MetatypesApi.md#validate_metatype_properties) | **POST** /containers/{container_id}/metatypes/{metatype_id} | Validate Metatype Properties

# **archive_metatype**
> Generic200Response archive_metatype(container_id, metatype_id)

Archive Metatype

Archives the metatype. This is preferred over deletion as deletion has a cascading effect on the deleted metatype's keys, relationships, and relationship keys. When in doubt, archive over delete. We'd rather have tombstones than cremating the metatype.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
metatype_id = 'metatype_id_example' # str | 

try:
    # Archive Metatype
    api_response = api_instance.archive_metatype(container_id, metatype_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypesApi->archive_metatype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **metatype_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metatype**
> CreateMetatypesResponse create_metatype(body, container_id)

Create Metatype

Create a new metatype. Pass in an array for bulk creation.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypesApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateMetatypeRequest() # CreateMetatypeRequest | 
container_id = 'container_id_example' # str | 

try:
    # Create Metatype
    api_response = api_instance.create_metatype(body, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypesApi->create_metatype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMetatypeRequest**](CreateMetatypeRequest.md)|  | 
 **container_id** | **str**|  | 

### Return type

[**CreateMetatypesResponse**](CreateMetatypesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metatypes**
> ListMetatypesResponse list_metatypes(container_id, limit=limit, offset=offset, name=name, description=description, count=count, load_keys=load_keys, sort_by=sort_by, sort_desc=sort_desc)

List Metatypes

List all metatypes that the container has access to. 

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
name = 'name_example' # str | Filter metatypes with names that match this pattern (optional)
description = 'description_example' # str | Filter metatypes with descriptions that match this pattern (optional)
count = 'count_example' # str | Set to true to return an integer count of the number of metatypes (optional)
load_keys = 'load_keys_example' # str | Set to false to not return the keys for the selected metatypes (true by default) (optional)
sort_by = 'sort_by_example' # str | Supply the name of a metatype attribute (name, created_at, etc) by which to sort (optional)
sort_desc = 'sort_desc_example' # str | Set true to sort descending (optional)

try:
    # List Metatypes
    api_response = api_instance.list_metatypes(container_id, limit=limit, offset=offset, name=name, description=description, count=count, load_keys=load_keys, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypesApi->list_metatypes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **name** | **str**| Filter metatypes with names that match this pattern | [optional] 
 **description** | **str**| Filter metatypes with descriptions that match this pattern | [optional] 
 **count** | **str**| Set to true to return an integer count of the number of metatypes | [optional] 
 **load_keys** | **str**| Set to false to not return the keys for the selected metatypes (true by default) | [optional] 
 **sort_by** | **str**| Supply the name of a metatype attribute (name, created_at, etc) by which to sort | [optional] 
 **sort_desc** | **str**| Set true to sort descending | [optional] 

### Return type

[**ListMetatypesResponse**](ListMetatypesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_metaype**
> GetMetatypeResponse retrieve_metaype(container_id, metatype_id)

Retrieve Metatype

Retrieves a single metatype.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
metatype_id = 'metatype_id_example' # str | 

try:
    # Retrieve Metatype
    api_response = api_instance.retrieve_metaype(container_id, metatype_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypesApi->retrieve_metaype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **metatype_id** | **str**|  | 

### Return type

[**GetMetatypeResponse**](GetMetatypeResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metatype**
> UpdateMetatypeResponse update_metatype(body, container_id, metatype_id)

Update Metatype

Update a single Metatype in storage. Will fail if the updated name has already been taken.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypesApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.UpdateMetatypeRequest() # UpdateMetatypeRequest | 
container_id = 'container_id_example' # str | 
metatype_id = 'metatype_id_example' # str | 

try:
    # Update Metatype
    api_response = api_instance.update_metatype(body, container_id, metatype_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypesApi->update_metatype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateMetatypeRequest**](UpdateMetatypeRequest.md)|  | 
 **container_id** | **str**|  | 
 **metatype_id** | **str**|  | 

### Return type

[**UpdateMetatypeResponse**](UpdateMetatypeResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_metatype_properties**
> ValidateMetatypePropertiesResponse validate_metatype_properties(container_id, metatype_id, body=body)

Validate Metatype Properties

Returns any errors associated with the intended properties or keys for a metatype or else the data itself if no errors are present.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
metatype_id = 'metatype_id_example' # str | 
body = NULL # object |  (optional)

try:
    # Validate Metatype Properties
    api_response = api_instance.validate_metatype_properties(container_id, metatype_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypesApi->validate_metatype_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **metatype_id** | **str**|  | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**ValidateMetatypePropertiesResponse**](ValidateMetatypePropertiesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

