# deep_lynx.DataExportApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_export**](DataExportApi.md#create_data_export) | **POST** /containers/{container_id}/data/export | Create Data Export
[**delete_data_export**](DataExportApi.md#delete_data_export) | **DELETE** /containers/{container_id}/data/export/{export_id} | Delete Data Export
[**list_data_exports**](DataExportApi.md#list_data_exports) | **GET** /containers/{container_id}/data/export | List Data Exports
[**retrieve_data_export**](DataExportApi.md#retrieve_data_export) | **GET** /containers/{container_id}/data/export/{export_id} | Retrieve Data Export
[**start_data_export**](DataExportApi.md#start_data_export) | **POST** /containers/{container_id}/data/export/{export_id} | Start Data Export
[**stop_data_export**](DataExportApi.md#stop_data_export) | **PUT** /containers/{container_id}/data/export/{export_id} | Stop Data Export

# **create_data_export**
> Generic200Response create_data_export(body, container_id)

Create Data Export

Create a new data export with the included configuration. Configuration values may be encrypted depending on the adapter you've choosen. See the readme for the exporters for more information.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataExportApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateDataExportRequest() # CreateDataExportRequest | 
container_id = 'container_id_example' # str | 

try:
    # Create Data Export
    api_response = api_instance.create_data_export(body, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExportApi->create_data_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDataExportRequest**](CreateDataExportRequest.md)|  | 
 **container_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_export**
> Generic200Response delete_data_export(container_id, export_id)

Delete Data Export

Deletes a data export record. This does not guarantee the export will stop immediately.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataExportApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
export_id = 'export_id_example' # str | 

try:
    # Delete Data Export
    api_response = api_instance.delete_data_export(container_id, export_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExportApi->delete_data_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **export_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_exports**
> ListDataExportsResponse list_data_exports(container_id, count=count, limit=limit, offset=offset, sort_by=sort_by, sort_desc=sort_desc)

List Data Exports

List data exports for the container.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataExportApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
count = true # bool | boolean indicating if the return value should be a count only (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | column to sort results by (optional)
sort_desc = true # bool | boolean indicating if results should be in descending order (optional)

try:
    # List Data Exports
    api_response = api_instance.list_data_exports(container_id, count=count, limit=limit, offset=offset, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExportApi->list_data_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **count** | **bool**| boolean indicating if the return value should be a count only | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**| column to sort results by | [optional] 
 **sort_desc** | **bool**| boolean indicating if results should be in descending order | [optional] 

### Return type

[**ListDataExportsResponse**](ListDataExportsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_data_export**
> GetDataExportResponse retrieve_data_export(container_id, export_id)

Retrieve Data Export

Fetch a data export record by ID

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataExportApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
export_id = 'export_id_example' # str | 

try:
    # Retrieve Data Export
    api_response = api_instance.retrieve_data_export(container_id, export_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExportApi->retrieve_data_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **export_id** | **str**|  | 

### Return type

[**GetDataExportResponse**](GetDataExportResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_data_export**
> Generic200Response start_data_export(container_id, export_id)

Start Data Export

Start or restart a data export by id.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataExportApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
export_id = 'export_id_example' # str | 

try:
    # Start Data Export
    api_response = api_instance.start_data_export(container_id, export_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExportApi->start_data_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **export_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_data_export**
> Generic200Response stop_data_export(container_id, export_id)

Stop Data Export

Stops a data export. Please note that this just sends a **stop** signal. The application's export adapter determines how to handle the said signal. In some cases the export stopping might not be immediate.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.DataExportApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
export_id = 'export_id_example' # str | 

try:
    # Stop Data Export
    api_response = api_instance.stop_data_export(container_id, export_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataExportApi->stop_data_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **export_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

