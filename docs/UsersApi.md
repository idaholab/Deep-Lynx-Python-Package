# deep_lynx.UsersApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_container_invite**](UsersApi.md#accept_container_invite) | **GET** /users/invite | AcceptContainerInvite
[**assign_user_role**](UsersApi.md#assign_user_role) | **POST** /containers/{container_id}/users/roles | AssignUserRole
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_id} | DeleteUser
[**invite_user_to_container**](UsersApi.md#invite_user_to_container) | **POST** /containers/{container_id}/users/invite | InviteUserToContainer
[**list_invited_users_for_container**](UsersApi.md#list_invited_users_for_container) | **GET** /containers/{container_id}/users/invite | ListInvitedUsersForContainer
[**list_outstanding_invites**](UsersApi.md#list_outstanding_invites) | **GET** /users/invites | ListOutstandingInvites
[**list_user_permissions**](UsersApi.md#list_user_permissions) | **GET** /users/permissions | ListUserPermissions
[**list_users**](UsersApi.md#list_users) | **GET** /users | ListUsers
[**list_users_for_container**](UsersApi.md#list_users_for_container) | **GET** /containers/{container_id}/users | ListUsersForContainer
[**list_users_roles**](UsersApi.md#list_users_roles) | **GET** /containers/{container_id}/users/{user_id}/roles | ListUsersRoles
[**retrieve_user**](UsersApi.md#retrieve_user) | **GET** /containers/{container_id}/users/{user_id} | RetrieveUser
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{user_id} | UpdateUser

# **accept_container_invite**
> Generic200Response accept_container_invite(token)

AcceptContainerInvite

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
    # AcceptContainerInvite
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_user_role**
> Generic200Response assign_user_role(body, container_id)

AssignUserRole

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
    # AssignUserRole
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> Generic200Response delete_user(user_id)

DeleteUser

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
    # DeleteUser
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user_to_container**
> Generic200Response invite_user_to_container(container_id, body=body)

InviteUserToContainer

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
    # InviteUserToContainer
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invited_users_for_container**
> ListContainerInvitesResponse list_invited_users_for_container(container_id)

ListInvitedUsersForContainer

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
    # ListInvitedUsersForContainer
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_outstanding_invites**
> ListUserInvitesResponse list_outstanding_invites()

ListOutstandingInvites

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
    # ListOutstandingInvites
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_permissions**
> ListUserPermissionsResponse list_user_permissions()

ListUserPermissions

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
    # ListUserPermissions
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUsersResponse list_users(count=count, load_keys=load_keys, limit=limit, offset=offset, sort_by=sort_by, sort_desc=sort_desc)

ListUsers

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
    # ListUsers
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_for_container**
> ListUsersForContainerResponse list_users_for_container(container_id, limit=limit, offset=offset)

ListUsersForContainer

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
    # ListUsersForContainer
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_roles**
> ListUserRoles list_users_roles(container_id, user_id)

ListUsersRoles

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
    # ListUsersRoles
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_user**
> GetUserResponse retrieve_user(container_id, user_id)

RetrieveUser

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
    # RetrieveUser
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> Generic200Response update_user(user_id, body=body)

UpdateUser

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
    # UpdateUser
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

[httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

