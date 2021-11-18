# deep_lynx.TasksApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](TasksApi.md#create_task) | **POST** /containers/{container_id}/task | Create Task
[**get_task**](TasksApi.md#get_task) | **GET** /containers/{container_id}/task/{task_id} | Get Task
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /containers/{container_id}/task | List Tasks
[**update_task**](TasksApi.md#update_task) | **PUT** /containers/{container_id}/task/{task_id} | Update Task

# **create_task**
> CreateTaskResponse create_task(container_id, body=body)

Create Task

Creates a new task

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TasksApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
body = deep_lynx.Task() # Task |  (optional)

try:
    # Create Task
    api_response = api_instance.create_task(container_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **body** | [**Task**](Task.md)|  | [optional] 

### Return type

[**CreateTaskResponse**](CreateTaskResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> GetTaskResponse get_task(container_id, task_id)

Get Task

Retrieves a specific task by ID

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TasksApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
task_id = 'task_id_example' # str | 

try:
    # Get Task
    api_response = api_instance.get_task(container_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **task_id** | **str**|  | 

### Return type

[**GetTaskResponse**](GetTaskResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> ListTasksResponse list_tasks(container_id)

List Tasks

Lists all tasks with a \"ready\" status

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TasksApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 

try:
    # List Tasks
    api_response = api_instance.list_tasks(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->list_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 

### Return type

[**ListTasksResponse**](ListTasksResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> UpdateTaskResponse update_task(container_id, task_id, body=body)

Update Task

Updates a task

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.TasksApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
task_id = 'task_id_example' # str | 
body = deep_lynx.Task() # Task |  (optional)

try:
    # Update Task
    api_response = api_instance.update_task(container_id, task_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **task_id** | **str**|  | 
 **body** | [**Task**](Task.md)|  | [optional] 

### Return type

[**UpdateTaskResponse**](UpdateTaskResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

