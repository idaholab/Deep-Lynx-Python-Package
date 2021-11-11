# deep_lynx.ImportsApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_data_to_import**](ImportsApi.md#add_data_to_import) | **POST** /containers/{container_id}/datasources/{data_source_id}/imports/{import_id}/data | AddDataToImport
[**create_import**](ImportsApi.md#create_import) | **POST** /containers/{container_id}/datasources/{data_source_id}/imports | CreateImport
[**delete_import**](ImportsApi.md#delete_import) | **DELETE** /containers/{container_id}/import/imports/{import_id} | DeleteImport
[**delete_import_data**](ImportsApi.md#delete_import_data) | **DELETE** /containers/{container_id}/import/imports/{import_id}/data/{data_id} | DeleteImportData
[**list_imports_data**](ImportsApi.md#list_imports_data) | **GET** /containers/{container_id}/import/imports/{import_id}/data | ListImportsData
[**retrieve_import_data**](ImportsApi.md#retrieve_import_data) | **GET** /containers/{container_id}/import/imports/{import_id}/data/{data_id} | RetrieveImportData
[**update_import_data**](ImportsApi.md#update_import_data) | **PUT** /containers/{container_id}/import/imports/{import_id}/data/{data_id} | UpdateImportData

# **add_data_to_import**
> AddDataToImportResponse add_data_to_import(content_type, container_id, import_id, data_source_id, file=file)

AddDataToImport

Adds data to an existing import. Accepts an array of JSON objects or a file in JSON or CSV format.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ImportsApi(deep_lynx.ApiClient(configuration))
content_type = 'content_type_example' # str | 
container_id = 'container_id_example' # str | 
import_id = 'import_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # AddDataToImport
    api_response = api_instance.add_data_to_import(content_type, container_id, import_id, data_source_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportsApi->add_data_to_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | 
 **container_id** | **str**|  | 
 **import_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**AddDataToImportResponse**](AddDataToImportResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_import**
> CreateImportResponse create_import(container_id, data_source_id, body=body)

CreateImport

Creates a new import.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ImportsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
body = deep_lynx.ContainersDatasourcesImportsRequest() # ContainersDatasourcesImportsRequest |  (optional)

try:
    # CreateImport
    api_response = api_instance.create_import(container_id, data_source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportsApi->create_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **body** | [**ContainersDatasourcesImportsRequest**](ContainersDatasourcesImportsRequest.md)|  | [optional] 

### Return type

[**CreateImportResponse**](CreateImportResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_import**
> delete_import(container_id, import_id)

DeleteImport

Delete import will delete an import ONLY IF the import has not been processed.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ImportsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
import_id = 'import_id_example' # str | 

try:
    # DeleteImport
    api_instance.delete_import(container_id, import_id)
except ApiException as e:
    print("Exception when calling ImportsApi->delete_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **import_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_import_data**
> Generic200Response delete_import_data(container_id, import_id, data_id)

DeleteImportData

Delete a single piece of data from an import.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ImportsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
import_id = 'import_id_example' # str | 
data_id = 56 # int | 

try:
    # DeleteImportData
    api_response = api_instance.delete_import_data(container_id, import_id, data_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportsApi->delete_import_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **import_id** | **str**|  | 
 **data_id** | **int**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_imports_data**
> ListImportDataResponse list_imports_data(container_id, import_id, count=count, limit=limit, offset=offset, sort_by=sort_by, sort_desc=sort_desc)

ListImportsData

List the data for an import.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ImportsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
import_id = 'import_id_example' # str | 
count = 'count_example' # str | boolean indicating if the return value should be a count only (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | column to sort results by (optional)
sort_desc = true # bool | boolean indicating if results should be in descending order (optional)

try:
    # ListImportsData
    api_response = api_instance.list_imports_data(container_id, import_id, count=count, limit=limit, offset=offset, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportsApi->list_imports_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **import_id** | **str**|  | 
 **count** | **str**| boolean indicating if the return value should be a count only | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**| column to sort results by | [optional] 
 **sort_desc** | **bool**| boolean indicating if results should be in descending order | [optional] 

### Return type

[**ListImportDataResponse**](ListImportDataResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_import_data**
> GetImportDataResponse retrieve_import_data(container_id, import_id, data_id)

RetrieveImportData

Retrieve a single piece of data from an import.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ImportsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
import_id = 'import_id_example' # str | 
data_id = 56 # int | 

try:
    # RetrieveImportData
    api_response = api_instance.retrieve_import_data(container_id, import_id, data_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportsApi->retrieve_import_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **import_id** | **str**|  | 
 **data_id** | **int**|  | 

### Return type

[**GetImportDataResponse**](GetImportDataResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_import_data**
> UpdateImportDataResponse update_import_data(container_id, import_id, data_id, body=body)

UpdateImportData

Update the data of an existing import.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ImportsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
import_id = 'import_id_example' # str | 
data_id = 56 # int | 
body = deep_lynx.DataStaging() # DataStaging |  (optional)

try:
    # UpdateImportData
    api_response = api_instance.update_import_data(container_id, import_id, data_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportsApi->update_import_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **import_id** | **str**|  | 
 **data_id** | **int**|  | 
 **body** | [**DataStaging**](DataStaging.md)|  | [optional] 

### Return type

[**UpdateImportDataResponse**](UpdateImportDataResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

