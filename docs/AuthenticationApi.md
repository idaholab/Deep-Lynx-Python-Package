# deep_lynx.AuthenticationApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_o_auth_token**](AuthenticationApi.md#exchange_o_auth_token) | **POST** /oauth/exchange | ExchangeOAuthToken
[**post_containers_container_id_metatypes_metatype_id**](AuthenticationApi.md#post_containers_container_id_metatypes_metatype_id) | **POST** /containers/{container_id}/metatypes/{metatype_id} | post-containers-container_id-metatypes-metatype_id
[**post_rsa_cancel**](AuthenticationApi.md#post_rsa_cancel) | **POST** /rsa/cancel | post-rsa-cancel
[**post_rsa_initialize**](AuthenticationApi.md#post_rsa_initialize) | **POST** /rsa/initialize | post-rsa-initialize
[**post_rsa_status**](AuthenticationApi.md#post_rsa_status) | **POST** /rsa/status | post-rsa-status
[**post_rsa_verify**](AuthenticationApi.md#post_rsa_verify) | **POST** /rsa/verify | post-rsa-verify
[**retrieve_o_auth_token**](AuthenticationApi.md#retrieve_o_auth_token) | **GET** /oauth/token | RetrieveOAuthToken

# **exchange_o_auth_token**
> str exchange_o_auth_token(body=body)

ExchangeOAuthToken

Exchanges credentials for a JSON Web Token (JWT). Multiple authentication flows are supported, see Deep Lynx documentation for details.

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
    # ExchangeOAuthToken
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_containers_container_id_metatypes_metatype_id**
> ValidateMetatypePropertiesResponse post_containers_container_id_metatypes_metatype_id(container_id, metatype_id, body=body)

post-containers-container_id-metatypes-metatype_id

Returns any errors associated with the intended properties or keys for a metatype or else the data itself if no errors are present.

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
metatype_id = 'metatype_id_example' # str | 
body = NULL # object |  (optional)

try:
    # post-containers-container_id-metatypes-metatype_id
    api_response = api_instance.post_containers_container_id_metatypes_metatype_id(container_id, metatype_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->post_containers_container_id_metatypes_metatype_id: %s\n" % e)
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_rsa_cancel**
> RSAResponse post_rsa_cancel(body=body)

post-rsa-cancel

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
    # post-rsa-cancel
    api_response = api_instance.post_rsa_cancel(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->post_rsa_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RSACancelRequest**](RSACancelRequest.md)|  | [optional] 

### Return type

[**RSAResponse**](RSAResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_rsa_initialize**
> RSAResponse post_rsa_initialize(body=body)

post-rsa-initialize

Used to begin (and optionally complete) an RSA authentication. Either a user's ID may be provided and the SecurID provided in a later `verify` request,  or else the user may provide both the user ID (`subjectName`) and `securID` at once to `initialize` to complete the authentication request.  The `securID` is the combination of the user's memorized token and 6 digit temporary RSA pin (with no spaces or characters between them).

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
    # post-rsa-initialize
    api_response = api_instance.post_rsa_initialize(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->post_rsa_initialize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RSAInitRequest**](RSAInitRequest.md)|  | [optional] 

### Return type

[**RSAResponse**](RSAResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_rsa_status**
> RSAStatusResponse post_rsa_status(body=body)

post-rsa-status

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
    # post-rsa-status
    api_response = api_instance.post_rsa_status(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->post_rsa_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RSAStatusRequest**](RSAStatusRequest.md)|  | [optional] 

### Return type

[**RSAStatusResponse**](RSAStatusResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_rsa_verify**
> RSAResponse post_rsa_verify(body=body)

post-rsa-verify

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
    # post-rsa-verify
    api_response = api_instance.post_rsa_verify(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->post_rsa_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RSAVerifyRequest**](RSAVerifyRequest.md)|  | [optional] 

### Return type

[**RSAResponse**](RSAResponse.md)

### Authorization

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_o_auth_token**
> str retrieve_o_auth_token(x_api_key, x_api_secret, x_api_expiry=x_api_expiry)

RetrieveOAuthToken

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
    # RetrieveOAuthToken
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

