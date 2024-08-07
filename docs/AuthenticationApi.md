# deep_lynx.AuthenticationApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_o_auth_token**](AuthenticationApi.md#exchange_o_auth_token) | **POST** /oauth/exchange | Exchange OAuth Token
[**list_service_keys_for_container**](AuthenticationApi.md#list_service_keys_for_container) | **GET** /containers/{container_id}/service-users/keys | List Service User Keys for Container
[**retrieve_o_auth_token**](AuthenticationApi.md#retrieve_o_auth_token) | **GET** /oauth/token | Retrieve OAuth Token
[**rsa_cancel**](AuthenticationApi.md#rsa_cancel) | **POST** /rsa/cancel | RSA Cancel
[**rsa_initialize**](AuthenticationApi.md#rsa_initialize) | **POST** /rsa/initialize | RSA Initialize
[**rsa_status**](AuthenticationApi.md#rsa_status) | **POST** /rsa/status | RSA Status
[**rsa_verify**](AuthenticationApi.md#rsa_verify) | **POST** /rsa/verify | RSA Verify

# **exchange_o_auth_token**
> str exchange_o_auth_token(body=body)

Exchange OAuth Token

Exchanges credentials for a JSON Web Token (JWT). Multiple authentication flows are supported, see DeepLynx documentation for details.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.AuthenticationApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.TokenExchangeRequest() # TokenExchangeRequest |  (optional)

try:
    # Exchange OAuth Token
    api_response = api_instance.exchange_o_auth_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->exchange_o_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenExchangeRequest**](TokenExchangeRequest.md)|  | [optional] 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_keys_for_container**
> InlineResponse20011 list_service_keys_for_container(container_id, note=note)

List Service User Keys for Container

Used to list all service-user keys in a container. Useful for obtaining keys in a container with a certain note to verify an application has ben authorized for a container.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.AuthenticationApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
note = 'note_example' # str | note with which keypair was created (optional)

try:
    # List Service User Keys for Container
    api_response = api_instance.list_service_keys_for_container(container_id, note=note)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->list_service_keys_for_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **note** | **str**| note with which keypair was created | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_o_auth_token**
> str retrieve_o_auth_token(x_api_key, x_api_secret, x_api_expiry=x_api_expiry)

Retrieve OAuth Token

Returns an OAuth token. The API key and secret must be supplied.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.AuthenticationApi(deep_lynx.ApiClient(configuration))
x_api_key = 'x_api_key_example' # str | The API key
x_api_secret = 'x_api_secret_example' # str | The API secret
x_api_expiry = 'x_api_expiry_example' # str | The API expiry date (optional)

try:
    # Retrieve OAuth Token
    api_response = api_instance.retrieve_o_auth_token(x_api_key, x_api_secret, x_api_expiry=x_api_expiry)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->retrieve_o_auth_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_key** | **str**| The API key | 
 **x_api_secret** | **str**| The API secret | 
 **x_api_expiry** | **str**| The API expiry date | [optional] 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rsa_cancel**
> RSAResponse rsa_cancel(body=body)

RSA Cancel

Cancels an RSA authentication attempt

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.AuthenticationApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.RSACancelRequest() # RSACancelRequest |  (optional)

try:
    # RSA Cancel
    api_response = api_instance.rsa_cancel(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->rsa_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RSACancelRequest**](RSACancelRequest.md)|  | [optional] 

### Return type

[**RSAResponse**](RSAResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rsa_initialize**
> RSAResponse rsa_initialize(body=body)

RSA Initialize

Used to begin (and optionally complete) an RSA authentication. Either a user's ID may be provided and the SecurID provided in a later `verify` request, or else the user may provide both the user ID (`subjectName`) and `securID` at once to `initialize` to complete the authentication request. The `securID` is the combination of the user's memorized token and 6 digit temporary RSA pin (with no spaces or characters between them).

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.AuthenticationApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.RSAInitRequest() # RSAInitRequest |  (optional)

try:
    # RSA Initialize
    api_response = api_instance.rsa_initialize(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->rsa_initialize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RSAInitRequest**](RSAInitRequest.md)|  | [optional] 

### Return type

[**RSAResponse**](RSAResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rsa_status**
> RSAStatusResponse rsa_status(body=body)

RSA Status

Returns the status of an RSA authentication attempt

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.AuthenticationApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.RSAStatusRequest() # RSAStatusRequest |  (optional)

try:
    # RSA Status
    api_response = api_instance.rsa_status(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->rsa_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RSAStatusRequest**](RSAStatusRequest.md)|  | [optional] 

### Return type

[**RSAStatusResponse**](RSAStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rsa_verify**
> RSAResponse rsa_verify(body=body)

RSA Verify

Provides RSA with the user's SecurID to complete authentication

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.AuthenticationApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.RSAVerifyRequest() # RSAVerifyRequest |  (optional)

try:
    # RSA Verify
    api_response = api_instance.rsa_verify(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->rsa_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RSAVerifyRequest**](RSAVerifyRequest.md)|  | [optional] 

### Return type

[**RSAResponse**](RSAResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

