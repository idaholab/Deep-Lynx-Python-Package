# deep_lynx.MiscApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health**](MiscApi.md#health) | **GET** /health | Health

# **health**
> str health()

Health

Simple endpoint, returns 200 on call. Can be used for a simple Up monitor by an external service.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MiscApi(deep_lynx.ApiClient(configuration))

try:
    # Health
    api_response = api_instance.health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

