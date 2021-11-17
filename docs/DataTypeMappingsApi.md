# deep_lynx.DataTypeMappingsApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transformation**](DataTypeMappingsApi.md#create_transformation) | **POST** /containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id}/transformations | Create Data Type Mapping&#x27;s Transformations
[**delete_data_type_mapping**](DataTypeMappingsApi.md#delete_data_type_mapping) | **DELETE** /containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id} | Delete Data Type Mapping
[**delete_transformation**](DataTypeMappingsApi.md#delete_transformation) | **DELETE** /containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id}/transformations/{transformation_id} | Delete Data Type Mapping&#x27;s Transformations
[**export_type_mappings**](DataTypeMappingsApi.md#export_type_mappings) | **POST** /containers/{container_id}/import/datasources/{data_source_id}/mappings/export | Export Type Mappings
[**import_data_type_mappings**](DataTypeMappingsApi.md#import_data_type_mappings) | **POST** /containers/{container_id}/import/datasources/{data_source_id}/mappings/import | Import Data Type Mappings
[**list_data_type_mappings**](DataTypeMappingsApi.md#list_data_type_mappings) | **GET** /containers/{container_id}/import/datasources/{data_source_id}/mappings | List Data Type Mappings
[**list_transformations**](DataTypeMappingsApi.md#list_transformations) | **GET** /containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id}/transformations | List Data Type Mapping&#x27;s Transformations
[**retrieve_data_type_mapping**](DataTypeMappingsApi.md#retrieve_data_type_mapping) | **GET** /containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id} | Retrieve Data Type Mapping
[**update_data_type_mapping**](DataTypeMappingsApi.md#update_data_type_mapping) | **PUT** /containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id} | Update Data Type Mapping
[**update_transformation**](DataTypeMappingsApi.md#update_transformation) | **PUT** /containers/{container_id}/import/datasources/{data_source_id}/mappings/{mapping_id}/transformations/{transformation_id} | Update Data Type Mapping&#x27;s Transformations

# **create_transformation**
> CreateTransformationResponse create_transformation(body, container_id, data_source_id, mapping_id)

Create Data Type Mapping's Transformations

Create a transformation for the type mapping.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTypeMappingsApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateTypeMappingTransformationsRequest() # CreateTypeMappingTransformationsRequest | 
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
mapping_id = 'mapping_id_example' # str | 

try:
    # Create Data Type Mapping's Transformations
    api_response = api_instance.create_transformation(body, container_id, data_source_id, mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypeMappingsApi->create_transformation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTypeMappingTransformationsRequest**](CreateTypeMappingTransformationsRequest.md)|  | 
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **mapping_id** | **str**|  | 

### Return type

[**CreateTransformationResponse**](CreateTransformationResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_type_mapping**
> Generic200Response delete_data_type_mapping(container_id, data_source_id, mapping_id)

Delete Data Type Mapping

Permanently remove data type mapping.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTypeMappingsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
mapping_id = 'mapping_id_example' # str | 

try:
    # Delete Data Type Mapping
    api_response = api_instance.delete_data_type_mapping(container_id, data_source_id, mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypeMappingsApi->delete_data_type_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **mapping_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transformation**
> Generic200Response delete_transformation(container_id, data_source_id, mapping_id, transformation_id)

Delete Data Type Mapping's Transformations

Delete a transformation.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTypeMappingsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
mapping_id = 'mapping_id_example' # str | 
transformation_id = 'transformation_id_example' # str | 

try:
    # Delete Data Type Mapping's Transformations
    api_response = api_instance.delete_transformation(container_id, data_source_id, mapping_id, transformation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypeMappingsApi->delete_transformation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **mapping_id** | **str**|  | 
 **transformation_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_type_mappings**
> list[TypeMapping] export_type_mappings(container_id, data_source_id, body=body)

Export Type Mappings

Export type mappings for a datasource. Providing a JSON body is optional. If provided, the mapping_ids may be specified to indicate certain type mapping IDs to return. Additionally, a target data source may be provided to which the mappings will be copied.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTypeMappingsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
body = deep_lynx.TypeMappingExportPayload() # TypeMappingExportPayload |  (optional)

try:
    # Export Type Mappings
    api_response = api_instance.export_type_mappings(container_id, data_source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypeMappingsApi->export_type_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **body** | [**TypeMappingExportPayload**](TypeMappingExportPayload.md)|  | [optional] 

### Return type

[**list[TypeMapping]**](TypeMapping.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_data_type_mappings**
> ImportDataTypeMappingResponse import_data_type_mappings(container_id, data_source_id, body=body)

Import Data Type Mappings

Import type mappings for a datasource. Accepts either a JSON body or actual JSON file. The payload should be an array of type mapping classes, previously generated using the export route.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTypeMappingsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
body = NULL # list[object] |  (optional)

try:
    # Import Data Type Mappings
    api_response = api_instance.import_data_type_mappings(container_id, data_source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypeMappingsApi->import_data_type_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **body** | [**list[object]**](object.md)|  | [optional] 

### Return type

[**ImportDataTypeMappingResponse**](ImportDataTypeMappingResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_type_mappings**
> ListDataTypeMappingResponse list_data_type_mappings(container_id, data_source_id, limit=limit, offset=offset, needs_transformations=needs_transformations, count=count, sort_by=sort_by, sort_desc=sort_desc, resulting_metatype_name=resulting_metatype_name, resulting_metatype_relationship_name=resulting_metatype_relationship_name)

List Data Type Mappings

Lists data type mappings for the data source

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTypeMappingsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
needs_transformations = true # bool | boolean indicating if the return should consist of only mappings that need transformations (optional)
count = true # bool | boolean indicating if the return value should be a count only (optional)
sort_by = 'sort_by_example' # str | column to sort results by (optional)
sort_desc = true # bool | boolean indicating if results should be in descending order (optional)
resulting_metatype_name = 'resulting_metatype_name_example' # str | if supplied, filters returned transformations by those that produce the resulting metatype (optional)
resulting_metatype_relationship_name = 'resulting_metatype_relationship_name_example' # str | if supplied, filters returned transformations by those that produce the resulting metatype relationship (optional)

try:
    # List Data Type Mappings
    api_response = api_instance.list_data_type_mappings(container_id, data_source_id, limit=limit, offset=offset, needs_transformations=needs_transformations, count=count, sort_by=sort_by, sort_desc=sort_desc, resulting_metatype_name=resulting_metatype_name, resulting_metatype_relationship_name=resulting_metatype_relationship_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypeMappingsApi->list_data_type_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **needs_transformations** | **bool**| boolean indicating if the return should consist of only mappings that need transformations | [optional] 
 **count** | **bool**| boolean indicating if the return value should be a count only | [optional] 
 **sort_by** | **str**| column to sort results by | [optional] 
 **sort_desc** | **bool**| boolean indicating if results should be in descending order | [optional] 
 **resulting_metatype_name** | **str**| if supplied, filters returned transformations by those that produce the resulting metatype | [optional] 
 **resulting_metatype_relationship_name** | **str**| if supplied, filters returned transformations by those that produce the resulting metatype relationship | [optional] 

### Return type

[**ListDataTypeMappingResponse**](ListDataTypeMappingResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transformations**
> ListTransformationResponse list_transformations(container_id, data_source_id, mapping_id)

List Data Type Mapping's Transformations

List transformations for a type mapping from storage.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTypeMappingsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
mapping_id = 'mapping_id_example' # str | 

try:
    # List Data Type Mapping's Transformations
    api_response = api_instance.list_transformations(container_id, data_source_id, mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypeMappingsApi->list_transformations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **mapping_id** | **str**|  | 

### Return type

[**ListTransformationResponse**](ListTransformationResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_data_type_mapping**
> GetDataTypeMappingResponse retrieve_data_type_mapping(container_id, data_source_id, mapping_id)

Retrieve Data Type Mapping

Retrieve a data type mapping

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTypeMappingsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
mapping_id = 'mapping_id_example' # str | 

try:
    # Retrieve Data Type Mapping
    api_response = api_instance.retrieve_data_type_mapping(container_id, data_source_id, mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypeMappingsApi->retrieve_data_type_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **mapping_id** | **str**|  | 

### Return type

[**GetDataTypeMappingResponse**](GetDataTypeMappingResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_type_mapping**
> UpdateDataTypeMappingResponse update_data_type_mapping(container_id, data_source_id, mapping_id, body=body)

Update Data Type Mapping

Updates a data type mapping.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTypeMappingsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
mapping_id = 'mapping_id_example' # str | 
body = deep_lynx.TypeMapping() # TypeMapping |  (optional)

try:
    # Update Data Type Mapping
    api_response = api_instance.update_data_type_mapping(container_id, data_source_id, mapping_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypeMappingsApi->update_data_type_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **mapping_id** | **str**|  | 
 **body** | [**TypeMapping**](TypeMapping.md)|  | [optional] 

### Return type

[**UpdateDataTypeMappingResponse**](UpdateDataTypeMappingResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transformation**
> UpdateTransformationResponse update_transformation(body, container_id, data_source_id, mapping_id, transformation_id)

Update Data Type Mapping's Transformations

Update a transformation.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataTypeMappingsApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateTypeMappingTransformationsRequest() # CreateTypeMappingTransformationsRequest | 
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
mapping_id = 'mapping_id_example' # str | 
transformation_id = 'transformation_id_example' # str | 

try:
    # Update Data Type Mapping's Transformations
    api_response = api_instance.update_transformation(body, container_id, data_source_id, mapping_id, transformation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataTypeMappingsApi->update_transformation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTypeMappingTransformationsRequest**](CreateTypeMappingTransformationsRequest.md)|  | 
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **mapping_id** | **str**|  | 
 **transformation_id** | **str**|  | 

### Return type

[**UpdateTransformationResponse**](UpdateTransformationResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

