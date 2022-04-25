# deep_lynx.UsersApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_container_invite**](UsersApi.md#accept_container_invite) | **GET** /users/invite | Accept Container Invite
[**assign_user_role**](UsersApi.md#assign_user_role) | **POST** /containers/{container_id}/users/roles | Assign User Role
[**create_service_user**](UsersApi.md#create_service_user) | **POST** /containers/{container_id}/service-users | Create Service User
[**create_service_user_key_pair**](UsersApi.md#create_service_user_key_pair) | **POST** /containers/{container_id}/service-users/{service_user_id}/keys | Create Service User KeyPair
[**delete_service_user**](UsersApi.md#delete_service_user) | **DELETE** /containers/{container_id}/service-users/{service_user_id} | Delete Service User
[**delete_service_user_key_pair**](UsersApi.md#delete_service_user_key_pair) | **DELETE** /containers/{container_id}/service-users/{service_user_id}/keys/{key_id} | Delete Service User KeyPair
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_id} | Delete User
[**get_service_user_permissions**](UsersApi.md#get_service_user_permissions) | **GET** /containers/{container_id}/service-users/{service_user_id}/permissions | Get Service User Permissions
[**invite_user_to_container**](UsersApi.md#invite_user_to_container) | **POST** /containers/{container_id}/users/invite | Invite User to Container
[**list_invited_users_for_container**](UsersApi.md#list_invited_users_for_container) | **GET** /containers/{container_id}/users/invite | List Invited Users for Container
[**list_outstanding_invites**](UsersApi.md#list_outstanding_invites) | **GET** /users/invites | List Outstanding Invites
[**list_service_user_key_pairs**](UsersApi.md#list_service_user_key_pairs) | **GET** /containers/{container_id}/service-users/{service_user_id}/keys | List Service User KeyPairs
[**list_service_users**](UsersApi.md#list_service_users) | **GET** /containers/{container_id}/service-users | List Service Users
[**list_user_permissions**](UsersApi.md#list_user_permissions) | **GET** /users/permissions | List User Permissions
[**list_users**](UsersApi.md#list_users) | **GET** /users | List Users
[**list_users_for_container**](UsersApi.md#list_users_for_container) | **GET** /containers/{container_id}/users | List Users for Container
[**list_users_roles**](UsersApi.md#list_users_roles) | **GET** /containers/{container_id}/users/{user_id}/roles | List User&#x27;s Roles
[**retrieve_user**](UsersApi.md#retrieve_user) | **GET** /containers/{container_id}/users/{user_id} | Retrieve User
[**set_service_user_permissions**](UsersApi.md#set_service_user_permissions) | **PUT** /containers/{container_id}/service-users/{service_user_id}/permissions | Set Service User Permissions
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{user_id} | Update User

# **accept_container_invite**
> Generic200Response accept_container_invite(token)

Accept Container Invite

Accepts a container invite for the current user. The token received in the container invite previously must be attached to this request as a query parameter.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
token = 'token_example' # str | the token supplied in the container invite

try:
    # Accept Container Invite
    api_response = api_instance.accept_container_invite(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->accept_container_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| the token supplied in the container invite | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_user_role**
> Generic200Response assign_user_role(body, container_id)

Assign User Role

Assign a role to a user, roles must consist of role name and domain

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.AssignRoleRequest() # AssignRoleRequest | 
container_id = 'container_id_example' # str | 

try:
    # Assign User Role
    api_response = api_instance.assign_user_role(body, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->assign_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignRoleRequest**](AssignRoleRequest.md)|  | 
 **container_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_user**
> create_service_user(container_id, body=body)

Create Service User

Creates a new service user for container

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
body = deep_lynx.CreateServiceUser() # CreateServiceUser |  (optional)

try:
    # Create Service User
    api_instance.create_service_user(container_id, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->create_service_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **body** | [**CreateServiceUser**](CreateServiceUser.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_user_key_pair**
> create_service_user_key_pair(container_id, service_user_id)

Create Service User KeyPair

Creates a new api/secret keypair. This will return the secret as well - this is the only time that you will be able to see the secret.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
service_user_id = 'service_user_id_example' # str | 

try:
    # Create Service User KeyPair
    api_instance.create_service_user_key_pair(container_id, service_user_id)
except ApiException as e:
    print("Exception when calling UsersApi->create_service_user_key_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **service_user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_user**
> delete_service_user(container_id, service_user_id)

Delete Service User

Deletes a service user.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
service_user_id = 'service_user_id_example' # str | 

try:
    # Delete Service User
    api_instance.delete_service_user(container_id, service_user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_service_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **service_user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_user_key_pair**
> delete_service_user_key_pair(container_id, service_user_id, key_id)

Delete Service User KeyPair

Delete a service user keypair.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
service_user_id = 'service_user_id_example' # str | 
key_id = 'key_id_example' # str | 

try:
    # Delete Service User KeyPair
    api_instance.delete_service_user_key_pair(container_id, service_user_id, key_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_service_user_key_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **service_user_id** | **str**|  | 
 **key_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> Generic200Response delete_user(user_id)

Delete User

Deletes the specified user.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Delete User
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_user_permissions**
> list[InlineResponse2002] get_service_user_permissions(container_id, service_user_id)

Get Service User Permissions

Get service user permissions.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
service_user_id = 'service_user_id_example' # str | 

try:
    # Get Service User Permissions
    api_response = api_instance.get_service_user_permissions(container_id, service_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_service_user_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **service_user_id** | **str**|  | 

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user_to_container**
> Generic200Response invite_user_to_container(container_id, body=body)

Invite User to Container

Create a new user using the username_password identity type.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
body = deep_lynx.ContainerInvite() # ContainerInvite |  (optional)

try:
    # Invite User to Container
    api_response = api_instance.invite_user_to_container(container_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->invite_user_to_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **body** | [**ContainerInvite**](ContainerInvite.md)|  | [optional] 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invited_users_for_container**
> ListContainerInvitesResponse list_invited_users_for_container(container_id)

List Invited Users for Container

List all invitations to container.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 

try:
    # List Invited Users for Container
    api_response = api_instance.list_invited_users_for_container(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_invited_users_for_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 

### Return type

[**ListContainerInvitesResponse**](ListContainerInvitesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_outstanding_invites**
> ListUserInvitesResponse list_outstanding_invites()

List Outstanding Invites

Lists the outstanding container invites for the current user.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))

try:
    # List Outstanding Invites
    api_response = api_instance.list_outstanding_invites()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_outstanding_invites: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListUserInvitesResponse**](ListUserInvitesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_user_key_pairs**
> list_service_user_key_pairs(container_id, service_user_id)

List Service User KeyPairs

Lists a service user's api/secret keypairs. This lists only the key, not the secret.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
service_user_id = 'service_user_id_example' # str | 

try:
    # List Service User KeyPairs
    api_instance.list_service_user_key_pairs(container_id, service_user_id)
except ApiException as e:
    print("Exception when calling UsersApi->list_service_user_key_pairs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **service_user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_users**
> ListServiceUserResponse list_service_users(container_id)

List Service Users

Retrieve a list of all service users for container

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 

try:
    # List Service Users
    api_response = api_instance.list_service_users(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_service_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 

### Return type

[**ListServiceUserResponse**](ListServiceUserResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_permissions**
> ListUserPermissionsResponse list_user_permissions()

List User Permissions

List permissions for the user.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))

try:
    # List User Permissions
    api_response = api_instance.list_user_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_user_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListUserPermissionsResponse**](ListUserPermissionsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUsersResponse list_users(count=count, load_keys=load_keys, limit=limit, offset=offset, sort_by=sort_by, sort_desc=sort_desc)

List Users

List users.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
count = true # bool | boolean indicating if the return value should be a count only (optional)
load_keys = true # bool | if supplied, the API keys for the user will also be returned (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
sort_by = 'sort_by_example' # str | column to sort results by (optional)
sort_desc = true # bool | boolean indicating if results should be in descending order (optional)

try:
    # List Users
    api_response = api_instance.list_users(count=count, load_keys=load_keys, limit=limit, offset=offset, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **bool**| boolean indicating if the return value should be a count only | [optional] 
 **load_keys** | **bool**| if supplied, the API keys for the user will also be returned | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **sort_by** | **str**| column to sort results by | [optional] 
 **sort_desc** | **bool**| boolean indicating if results should be in descending order | [optional] 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_for_container**
> ListUsersForContainerResponse list_users_for_container(container_id, limit=limit, offset=offset)

List Users for Container

List Users for container.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)

try:
    # List Users for Container
    api_response = api_instance.list_users_for_container(container_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_users_for_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**ListUsersForContainerResponse**](ListUsersForContainerResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_roles**
> ListUserRoles list_users_roles(container_id, user_id)

List User's Roles

List Users' roles

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # List User's Roles
    api_response = api_instance.list_users_roles(container_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->list_users_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**ListUserRoles**](ListUserRoles.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user**
> GetUserResponse retrieve_user(container_id, user_id)

Retrieve User

Retrieve a user by ID

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Retrieve User
    api_response = api_instance.retrieve_user(container_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->retrieve_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_service_user_permissions**
> set_service_user_permissions(container_id, service_user_id, body=body)

Set Service User Permissions

Set service user permissions.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
service_user_id = 'service_user_id_example' # str | 
body = deep_lynx.ServiceUserIdPermissionsBody() # ServiceUserIdPermissionsBody |  (optional)

try:
    # Set Service User Permissions
    api_instance.set_service_user_permissions(container_id, service_user_id, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->set_service_user_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **service_user_id** | **str**|  | 
 **body** | [**ServiceUserIdPermissionsBody**](ServiceUserIdPermissionsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> Generic200Response update_user(user_id, body=body)

Update User

Updates the specified user.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.UsersApi(deep_lynx.ApiClient(configuration))
user_id = 'user_id_example' # str | 
body = deep_lynx.User() # User |  (optional)

try:
    # Update User
    api_response = api_instance.update_user(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **body** | [**User**](User.md)|  | [optional] 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

