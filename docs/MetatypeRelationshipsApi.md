# deep_lynx.MetatypeRelationshipsApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_metatype_relationship**](MetatypeRelationshipsApi.md#archive_metatype_relationship) | **DELETE** /containers/{container_id}/metatype_relationships/{relationship_id} | Archive Metatype Relationship
[**create_metatype_relationship**](MetatypeRelationshipsApi.md#create_metatype_relationship) | **POST** /containers/{container_id}/metatype_relationships | Create Metatype Relationship
[**list_metatype_relationships**](MetatypeRelationshipsApi.md#list_metatype_relationships) | **GET** /containers/{container_id}/metatype_relationships | List Metatype Relationships
[**retrieve_metatype_relationship**](MetatypeRelationshipsApi.md#retrieve_metatype_relationship) | **GET** /containers/{container_id}/metatype_relationships/{relationship_id} | Retrieve Metatype Relationship
[**update_metatype_relationship**](MetatypeRelationshipsApi.md#update_metatype_relationship) | **PUT** /containers/{container_id}/metatype_relationships/{relationship_id} | Update Metatype Relationship

# **archive_metatype_relationship**
> Generic200Response archive_metatype_relationship(container_id, relationship_id)

Archive Metatype Relationship

Archive the metatype relationship.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
relationship_id = 'relationship_id_example' # str | 

try:
    # Archive Metatype Relationship
    api_response = api_instance.archive_metatype_relationship(container_id, relationship_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipsApi->archive_metatype_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **relationship_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metatype_relationship**
> CreateMetatypeRelationshipsResponse create_metatype_relationship(body, container_id)

Create Metatype Relationship

Create a new metatype relationship. Describes the connection that could exist between two metatypes and acts as a vehicle for relationship specific keys.  Pass in an array for bulk creation.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipsApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateMetatypeRelationshipRequest() # CreateMetatypeRelationshipRequest | 
container_id = 'container_id_example' # str | 

try:
    # Create Metatype Relationship
    api_response = api_instance.create_metatype_relationship(body, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipsApi->create_metatype_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMetatypeRelationshipRequest**](CreateMetatypeRelationshipRequest.md)|  | 
 **container_id** | **str**|  | 

### Return type

[**CreateMetatypeRelationshipsResponse**](CreateMetatypeRelationshipsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metatype_relationships**
> ListMetatypeRelationshipsResponse list_metatype_relationships(container_id, limit=limit, offset=offset, name=name, description=description, count=count, load_keys=load_keys, sort_by=sort_by, sort_desc=sort_desc)

List Metatype Relationships

List metatype relationships. Describes the connection between two metatypes and acts as a vehicle for relationship specific keys.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
name = 'name_example' # str | Filter metatype relationships with names that match this pattern (optional)
description = 'description_example' # str | Filter metatype relationships with descriptions that match this pattern (optional)
count = 'count_example' # str | Set to true to return an integer count of the number of metatype relationships (optional)
load_keys = 'load_keys_example' # str | Set to false to not return the keys for the selected metatype relationships (true by default) (optional)
sort_by = 'sort_by_example' # str | Supply the name of a metatype relationship attribute (name, created_at, etc) by which to sort (optional)
sort_desc = 'sort_desc_example' # str | Set true to sort descending (optional)

try:
    # List Metatype Relationships
    api_response = api_instance.list_metatype_relationships(container_id, limit=limit, offset=offset, name=name, description=description, count=count, load_keys=load_keys, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipsApi->list_metatype_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **name** | **str**| Filter metatype relationships with names that match this pattern | [optional] 
 **description** | **str**| Filter metatype relationships with descriptions that match this pattern | [optional] 
 **count** | **str**| Set to true to return an integer count of the number of metatype relationships | [optional] 
 **load_keys** | **str**| Set to false to not return the keys for the selected metatype relationships (true by default) | [optional] 
 **sort_by** | **str**| Supply the name of a metatype relationship attribute (name, created_at, etc) by which to sort | [optional] 
 **sort_desc** | **str**| Set true to sort descending | [optional] 

### Return type

[**ListMetatypeRelationshipsResponse**](ListMetatypeRelationshipsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_metatype_relationship**
> GetMetatypeRelationshipResponse retrieve_metatype_relationship(container_id, relationship_id)

Retrieve Metatype Relationship

Retrieve a single Metatype Relationship.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
relationship_id = 'relationship_id_example' # str | 

try:
    # Retrieve Metatype Relationship
    api_response = api_instance.retrieve_metatype_relationship(container_id, relationship_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipsApi->retrieve_metatype_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **relationship_id** | **str**|  | 

### Return type

[**GetMetatypeRelationshipResponse**](GetMetatypeRelationshipResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metatype_relationship**
> UpdateMetatypeRelationshipResponse update_metatype_relationship(body, container_id, relationship_id)

Update Metatype Relationship

Updates the specified metatype relationship.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipsApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.UpdateMetatypeRelationshipRequest() # UpdateMetatypeRelationshipRequest | 
container_id = 'container_id_example' # str | 
relationship_id = 'relationship_id_example' # str | 

try:
    # Update Metatype Relationship
    api_response = api_instance.update_metatype_relationship(body, container_id, relationship_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipsApi->update_metatype_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateMetatypeRelationshipRequest**](UpdateMetatypeRelationshipRequest.md)|  | 
 **container_id** | **str**|  | 
 **relationship_id** | **str**|  | 

### Return type

[**UpdateMetatypeRelationshipResponse**](UpdateMetatypeRelationshipResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

