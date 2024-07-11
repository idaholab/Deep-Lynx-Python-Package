# deep_lynx.ImportsApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_data_to_import**](ImportsApi.md#add_data_to_import) | **POST** /containers/{container_id}/datasources/{data_source_id}/imports/{import_id}/data | Add Data to Import
[**create_import**](ImportsApi.md#create_import) | **POST** /containers/{container_id}/datasources/{data_source_id}/imports | Create Import
[**delete_file**](ImportsApi.md#delete_file) | **DELETE** /containers/:container_id/import/datasources/:data_source_id/files/:file_id | Delete File
[**delete_import**](ImportsApi.md#delete_import) | **DELETE** /containers/{container_id}/import/imports/{import_id} | Delete Import
[**delete_import_data**](ImportsApi.md#delete_import_data) | **DELETE** /containers/{container_id}/import/imports/{import_id}/data/{data_id} | Delete Import Data
[**list_imports_data**](ImportsApi.md#list_imports_data) | **GET** /containers/{container_id}/import/imports/{import_id}/data | List Import&#x27;s Data
[**put_containers_container_id_import_datasources_datasource_id_files_file_id**](ImportsApi.md#put_containers_container_id_import_datasources_datasource_id_files_file_id) | **PUT** /containers/:container_id/import/datasources/:data_source_id/files/:file_id | Update files
[**retrieve_import_data**](ImportsApi.md#retrieve_import_data) | **GET** /containers/{container_id}/import/imports/{import_id}/data/{data_id} | Retrieve Import Data
[**update_import_data**](ImportsApi.md#update_import_data) | **PUT** /containers/{container_id}/import/imports/{import_id}/data/{data_id} | Update Import Data

# **add_data_to_import**
> AddDataToImportResponse add_data_to_import(container_id, import_id, data_source_id, body=body)

Add Data to Import

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
container_id = 'container_id_example' # str | 
import_id = 'import_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
body = NULL # list[object] |  (optional)

try:
    # Add Data to Import
    api_response = api_instance.add_data_to_import(container_id, import_id, data_source_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportsApi->add_data_to_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **import_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **body** | [**list[object]**](object.md)|  | [optional] 

### Return type

[**AddDataToImportResponse**](AddDataToImportResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_import**
> CreateImportResponse create_import(container_id, data_source_id, body=body)

Create Import

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
body = deep_lynx.DataSourceIdImportsBody1() # DataSourceIdImportsBody1 |  (optional)

try:
    # Create Import
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
 **body** | [**DataSourceIdImportsBody1**](DataSourceIdImportsBody1.md)|  | [optional] 

### Return type

[**CreateImportResponse**](CreateImportResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file()

Delete File

Delete a file

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ImportsApi(deep_lynx.ApiClient(configuration))

try:
    # Delete File
    api_instance.delete_file()
except ApiException as e:
    print("Exception when calling ImportsApi->delete_file: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_import**
> delete_import(container_id, import_id)

Delete Import

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
    # Delete Import
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_import_data**
> Generic200Response delete_import_data(container_id, import_id, data_id)

Delete Import Data

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
    # Delete Import Data
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_imports_data**
> ListImportDataResponse list_imports_data(container_id, import_id, count=count, limit=limit, offset=offset, sort_by=sort_by, sort_desc=sort_desc)

List Import's Data

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
    # List Import's Data
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_containers_container_id_import_datasources_datasource_id_files_file_id**
> put_containers_container_id_import_datasources_datasource_id_files_file_id(body=body, authorization=authorization)

Update files

Update a file

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.ImportsApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.FilesFileIdBody() # FilesFileIdBody | Key/value pair where the key is named 'file' and the file is any file.
Optionally, any metadata can be added (optional)
authorization = 'authorization_example' # str | Bearer token (optional)

try:
    # Update files
    api_instance.put_containers_container_id_import_datasources_datasource_id_files_file_id(body=body, authorization=authorization)
except ApiException as e:
    print("Exception when calling ImportsApi->put_containers_container_id_import_datasources_datasource_id_files_file_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FilesFileIdBody**](FilesFileIdBody.md)| Key/value pair where the key is named &#x27;file&#x27; and the file is any file.
Optionally, any metadata can be added | [optional] 
 **authorization** | **str**| Bearer token | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_import_data**
> GetImportDataResponse retrieve_import_data(container_id, import_id, data_id)

Retrieve Import Data

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
    # Retrieve Import Data
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_import_data**
> UpdateImportDataResponse update_import_data(container_id, import_id, data_id, body=body)

Update Import Data

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
    # Update Import Data
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

