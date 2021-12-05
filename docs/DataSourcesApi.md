# deep_lynx.DataSourcesApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_data_source**](DataSourcesApi.md#archive_data_source) | **DELETE** /containers/{container_id}/import/datasources/{data_source_id} | Archive Data Source
[**create_data_source**](DataSourcesApi.md#create_data_source) | **POST** /containers/{container_id}/import/datasources | Create Data Source
[**create_manual_import**](DataSourcesApi.md#create_manual_import) | **POST** /containers/{container_id}/import/datasources/{data_source_id}/imports | Create Manual Import
[**download_file**](DataSourcesApi.md#download_file) | **GET** /containers/{container_id}/files/{file_id}/download | Download File
[**list_data_sources**](DataSourcesApi.md#list_data_sources) | **GET** /containers/{container_id}/import/datasources | List Data Sources
[**list_imports_for_data_source**](DataSourcesApi.md#list_imports_for_data_source) | **GET** /containers/{container_id}/import/datasources/{data_source_id}/imports | List Imports for Data Source
[**retrieve_data_source**](DataSourcesApi.md#retrieve_data_source) | **GET** /containers/{container_id}/import/datasources/{data_source_id} | Retrieve Data Source
[**retrieve_file**](DataSourcesApi.md#retrieve_file) | **GET** /containers/{container_id}/files/{file_id} | Retrieve File
[**set_data_source_active**](DataSourcesApi.md#set_data_source_active) | **POST** /containers/{container_id}/import/datasources/{data_source_id}/active | Set Data Source Active
[**set_data_source_configuration**](DataSourcesApi.md#set_data_source_configuration) | **PUT** /containers/{container_id}/import/datasources/{data_source_id} | Set Data Source Configuration
[**set_data_source_inactive**](DataSourcesApi.md#set_data_source_inactive) | **DELETE** /containers/{container_id}/import/datasources/{data_source_id}/active | Set Data Source Inactive
[**upload_file**](DataSourcesApi.md#upload_file) | **POST** /containers/{container_id}/import/datasources/{data_source_id}/files | Upload File

# **archive_data_source**
> Generic200Response archive_data_source(container_id, data_source_id, archive=archive, force_delete=force_delete, remove_data=remove_data)

Archive Data Source

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
    # Archive Data Source
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_source**
> CreateDataSourcesResponse create_data_source(body, container_id)

Create Data Source

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
    # Create Data Source
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_manual_import**
> CreateManualImportResponse create_manual_import(body, container_id, data_source_id)

Create Manual Import

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
    # Create Manual Import
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> download_file(container_id, file_id)

Download File

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
    # Download File
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_sources**
> ListDataSourcesResponse list_data_sources(container_id)

List Data Sources

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
    # List Data Sources
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_imports_for_data_source**
> ListDataSourceImportsResponse list_imports_for_data_source(container_id, data_source_id)

List Imports for Data Source

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
    # List Imports for Data Source
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_data_source**
> GetDataSourceResponse retrieve_data_source(container_id, data_source_id)

Retrieve Data Source

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
    # Retrieve Data Source
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_file**
> GetFileInfoResponse retrieve_file(container_id, file_id)

Retrieve File

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
    # Retrieve File
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_source_active**
> Generic200Response set_data_source_active(container_id, data_source_id)

Set Data Source Active

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
    # Set Data Source Active
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_source_configuration**
> UpdateDataSourceResponse set_data_source_configuration(body, container_id, data_source_id)

Set Data Source Configuration

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
    # Set Data Source Configuration
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_source_inactive**
> Generic200Response set_data_source_inactive(container_id, data_source_id)

Set Data Source Inactive

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
    # Set Data Source Inactive
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

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> UploadFileResponse upload_file(container_id, data_source_id, file=file, import_id=import_id)

Upload File

Uploads a file and it's metadata to Deep Lynx. All additional fields on the multipart form will be processed and added as metadata to the file upload itself.   If you include a file field and call that \"metadata\" - you can include a normal metadata upload as either a json, csv, or xml file. This data will be processed like a normal import and the files attached to the processed data. Once Deep Lynx generates nodes and edges from that data, any files attached will automatically be attached to the resulting nodes/edges as well.  NOTE: The metadata file you upload, if json, must be wrapped in an array. If you do not pass in an array of objects, even if it's a single object, then Deep Lynx will attempt to split up your metadata into its parts instead of treating it like a whole object.

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
file = 'file_example' # str |  (optional)
import_id = 'import_id_example' # str | You can attach the metadata to an existing import if desired. (optional)

try:
    # Upload File
    api_response = api_instance.upload_file(container_id, data_source_id, file=file, import_id=import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **data_source_id** | **str**|  | 
 **file** | **str**|  | [optional] 
 **import_id** | **str**| You can attach the metadata to an existing import if desired. | [optional] 

### Return type

[**UploadFileResponse**](UploadFileResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

