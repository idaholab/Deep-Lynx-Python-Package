# deep_lynx.DataSourcesApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_data_source**](DataSourcesApi.md#archive_data_source) | **DELETE** /containers/{container_id}/import/datasources/{data_source_id} | ArchiveDataSource
[**create_data_source**](DataSourcesApi.md#create_data_source) | **POST** /containers/{container_id}/import/datasources | CreateDataSource
[**create_manual_import**](DataSourcesApi.md#create_manual_import) | **POST** /containers/{container_id}/import/datasources/{data_source_id}/imports | CreateManualImport
[**download_file**](DataSourcesApi.md#download_file) | **GET** /containers/{container_id}/files/{file_id}/download | DownloadFile
[**list_data_sources**](DataSourcesApi.md#list_data_sources) | **GET** /containers/{container_id}/import/datasources | ListDataSources
[**list_imports_for_data_source**](DataSourcesApi.md#list_imports_for_data_source) | **GET** /containers/{container_id}/import/datasources/{data_source_id}/imports | ListImportsForDataSource
[**retrieve_data_source**](DataSourcesApi.md#retrieve_data_source) | **GET** /containers/{container_id}/import/datasources/{data_source_id} | RetrieveDataSource
[**retrieve_file**](DataSourcesApi.md#retrieve_file) | **GET** /containers/{container_id}/files/{file_id} | RetrieveFile
[**set_data_source_active**](DataSourcesApi.md#set_data_source_active) | **POST** /containers/{container_id}/import/datasources/{data_source_id}/active | SetDataSourceActive
[**set_data_source_configuration**](DataSourcesApi.md#set_data_source_configuration) | **PUT** /containers/{container_id}/import/datasources/{data_source_id} | SetDataSourceConfiguration
[**set_data_source_inactive**](DataSourcesApi.md#set_data_source_inactive) | **DELETE** /containers/{container_id}/import/datasources/{data_source_id}/active | SetDataSourceInactive
[**upload_file**](DataSourcesApi.md#upload_file) | **POST** /containers/{container_id}/import/datasources/{data_source_id}/files | UploadFile

# **archive_data_source**
> Generic200Response archive_data_source(container_id, data_source_id, archive=archive, force_delete=force_delete, remove_data=remove_data)

ArchiveDataSource

Archive a data source, with options to permanently remove it (and associated data).

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataSourcesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
archive = 'archive_example' # str | Set to true to archive the data source. (optional)
force_delete = 'force_delete_example' # str | Set to true to force deletion of the data source. (optional)
remove_data = 'remove_data_example' # str | Set to true to remove data associated with the data source. (optional)

try:
    # ArchiveDataSource
    api_response = api_instance.archive_data_source(container_id, data_source_id, archive=archive, force_delete=force_delete, remove_data=remove_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->archive_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **archive** | **str**| Set to true to archive the data source. | [optional] 
 **force_delete** | **str**| Set to true to force deletion of the data source. | [optional] 
 **remove_data** | **str**| Set to true to remove data associated with the data source. | [optional] 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_source**
> CreateDataSourcesResponse create_data_source(body, container_id)

CreateDataSource

Create new datasource. Supported data source types are `http`, `standard` (or `manual`), `jazz`, and `aveva`.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataSourcesApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateDataSourceRequest() # CreateDataSourceRequest | 
container_id = 'container_id_example' # str | 

try:
    # CreateDataSource
    api_response = api_instance.create_data_source(body, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->create_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDataSourceRequest**](CreateDataSourceRequest.md)|  | 
 **container_id** | **str**|  | 

### Return type

[**CreateDataSourcesResponse**](CreateDataSourcesResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_manual_import**
> CreateManualImportResponse create_manual_import(body, container_id, data_source_id)

CreateManualImport

Create a manual import.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataSourcesApi(deep_lynx.ApiClient(configuration))
body = NULL # object | 
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 

try:
    # CreateManualImport
    api_response = api_instance.create_manual_import(body, container_id, data_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->create_manual_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 

### Return type

[**CreateManualImportResponse**](CreateManualImportResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> download_file(container_id, file_id)

DownloadFile

Downloads a previously uploaded file.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataSourcesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
file_id = 'file_id_example' # str | 

try:
    # DownloadFile
    api_instance.download_file(container_id, file_id)
except ApiException as e:
    print("Exception when calling DataSourcesApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **file_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_sources**
> ListDataSourcesResponse list_data_sources(container_id)

ListDataSources

List the datasources for the container.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataSourcesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 

try:
    # ListDataSources
    api_response = api_instance.list_data_sources(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->list_data_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 

### Return type

[**ListDataSourcesResponse**](ListDataSourcesResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_imports_for_data_source**
> ListDataSourceImportsResponse list_imports_for_data_source(container_id, data_source_id)

ListImportsForDataSource

List the imports for the datasource.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataSourcesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 

try:
    # ListImportsForDataSource
    api_response = api_instance.list_imports_for_data_source(container_id, data_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->list_imports_for_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 

### Return type

[**ListDataSourceImportsResponse**](ListDataSourceImportsResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_data_source**
> GetDataSourceResponse retrieve_data_source(container_id, data_source_id)

RetrieveDataSource

Retrieve a single data source by ID.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataSourcesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 

try:
    # RetrieveDataSource
    api_response = api_instance.retrieve_data_source(container_id, data_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->retrieve_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 

### Return type

[**GetDataSourceResponse**](GetDataSourceResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_file**
> GetFileInfoResponse retrieve_file(container_id, file_id)

RetrieveFile

Get information about a file by ID.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataSourcesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
file_id = 'file_id_example' # str | 

try:
    # RetrieveFile
    api_response = api_instance.retrieve_file(container_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->retrieve_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **file_id** | **str**|  | 

### Return type

[**GetFileInfoResponse**](GetFileInfoResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_source_active**
> Generic200Response set_data_source_active(container_id, data_source_id)

SetDataSourceActive

Sets a data source active.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataSourcesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 

try:
    # SetDataSourceActive
    api_response = api_instance.set_data_source_active(container_id, data_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->set_data_source_active: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_source_configuration**
> UpdateDataSourceResponse set_data_source_configuration(body, container_id, data_source_id)

SetDataSourceConfiguration

Updates a data source's configuration in storage. Note that this request body's structure must match that of the data source's adapter type.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataSourcesApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateDataSourceConfig() # CreateDataSourceConfig | 
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 

try:
    # SetDataSourceConfiguration
    api_response = api_instance.set_data_source_configuration(body, container_id, data_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->set_data_source_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDataSourceConfig**](CreateDataSourceConfig.md)|  | 
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 

### Return type

[**UpdateDataSourceResponse**](UpdateDataSourceResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_source_inactive**
> Generic200Response set_data_source_inactive(container_id, data_source_id)

SetDataSourceInactive

Sets a data source inactive.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataSourcesApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 

try:
    # SetDataSourceInactive
    api_response = api_instance.set_data_source_inactive(container_id, data_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->set_data_source_inactive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> InlineResponse200 upload_file(content_type, container_id, data_source_id, file=file)

UploadFile

Uploads a file and metadata to Deep Lynx. This endpoint will accept multiple files and multiple metadata properties as form values. If metadata (additional key value pairs) are provided, an import is created for the data source in addition to the file upload. Transformations can be applied to this import to create nodes and edges in the graph with metadata for the uploaded file(s).

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataSourcesApi(deep_lynx.ApiClient(configuration))
content_type = 'content_type_example' # str | 
container_id = 'container_id_example' # str | 
data_source_id = 'data_source_id_example' # str | 
file = 'file_example' # str |  (optional)

try:
    # UploadFile
    api_response = api_instance.upload_file(content_type, container_id, data_source_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | 
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **file** | **str**|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

