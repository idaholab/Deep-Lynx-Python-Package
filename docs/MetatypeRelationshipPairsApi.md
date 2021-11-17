# deep_lynx.MetatypeRelationshipPairsApi

All URIs are relative to *http://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_metatype_relationship_pair**](MetatypeRelationshipPairsApi.md#archive_metatype_relationship_pair) | **DELETE** /containers/{container_id}/metatype_relationship_pairs/{pair_id} | Archive Metatype Relationship Pair
[**create_metatype_relationship_pair**](MetatypeRelationshipPairsApi.md#create_metatype_relationship_pair) | **POST** /containers/{container_id}/metatype_relationship_pairs | Create Metatype Relationship Pair
[**list_metatype_relationship_pairs**](MetatypeRelationshipPairsApi.md#list_metatype_relationship_pairs) | **GET** /containers/{container_id}/metatype_relationship_pairs | List Metatype Relationship Pairs
[**retrieve_metatype_relationship_pair**](MetatypeRelationshipPairsApi.md#retrieve_metatype_relationship_pair) | **GET** /containers/{container_id}/metatype_relationship_pairs/{pair_id} | Retrieve Metatype Relationship Pair
[**update_metatype_relationship_pair**](MetatypeRelationshipPairsApi.md#update_metatype_relationship_pair) | **PUT** /containers/{container_id}/metatype_relationship_pairs/{pair_id} | Update Metaype Relationship Pair

# **archive_metatype_relationship_pair**
> Generic200Response archive_metatype_relationship_pair(container_id, pair_id)

Archive Metatype Relationship Pair

Archives a Metatype Relationship Pair.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipPairsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
pair_id = 'pair_id_example' # str | 

try:
    # Archive Metatype Relationship Pair
    api_response = api_instance.archive_metatype_relationship_pair(container_id, pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipPairsApi->archive_metatype_relationship_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **pair_id** | **str**|  | 

### Return type

[**Generic200Response**](Generic200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metatype_relationship_pair**
> CreateMetatypeRelationshipPairsResponse create_metatype_relationship_pair(body, container_id)

Create Metatype Relationship Pair

Create a new Metaype Relationship Pair. Describes the connection between two metatypes by connecting them using a Metatype Relationship.  Pass in an array for bulk creation.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipPairsApi(deep_lynx.ApiClient(configuration))
body = deep_lynx.CreateMetatypeRelationshipPairRequest() # CreateMetatypeRelationshipPairRequest | 
container_id = 'container_id_example' # str | 

try:
    # Create Metatype Relationship Pair
    api_response = api_instance.create_metatype_relationship_pair(body, container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipPairsApi->create_metatype_relationship_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMetatypeRelationshipPairRequest**](CreateMetatypeRelationshipPairRequest.md)|  | 
 **container_id** | **str**|  | 

### Return type

[**CreateMetatypeRelationshipPairsResponse**](CreateMetatypeRelationshipPairsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metatype_relationship_pairs**
> ListMetatypeRelationshipPairsResponse list_metatype_relationship_pairs(container_id, limit=limit, offset=offset, name=name, archived=archived, count=count, load_relationships=load_relationships, destination_id=destination_id, origin_id=origin_id, metatype_id=metatype_id)

List Metatype Relationship Pairs

List all Metatype Relationship Pairs for current container.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipPairsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
name = 'name_example' # str | Filter metatype relationship pairs with names that match this pattern (optional)
archived = 'archived_example' # str | Set to true to include archived metatype relationship pairs (optional)
count = 'count_example' # str | Set to true to return an integer count of the number of metatype relationship pairs (optional)
load_relationships = 'load_relationships_example' # str | Set to false to not return the relationships for the selected metatype relationship pairs (true by default) (optional)
destination_id = 'destination_id_example' # str | Filter destination by metatype ID (optional)
origin_id = 'origin_id_example' # str | Filter origin by metatype ID (optional)
metatype_id = 'metatype_id_example' # str | Filter by metatype ID (optional)

try:
    # List Metatype Relationship Pairs
    api_response = api_instance.list_metatype_relationship_pairs(container_id, limit=limit, offset=offset, name=name, archived=archived, count=count, load_relationships=load_relationships, destination_id=destination_id, origin_id=origin_id, metatype_id=metatype_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipPairsApi->list_metatype_relationship_pairs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **name** | **str**| Filter metatype relationship pairs with names that match this pattern | [optional] 
 **archived** | **str**| Set to true to include archived metatype relationship pairs | [optional] 
 **count** | **str**| Set to true to return an integer count of the number of metatype relationship pairs | [optional] 
 **load_relationships** | **str**| Set to false to not return the relationships for the selected metatype relationship pairs (true by default) | [optional] 
 **destination_id** | **str**| Filter destination by metatype ID | [optional] 
 **origin_id** | **str**| Filter origin by metatype ID | [optional] 
 **metatype_id** | **str**| Filter by metatype ID | [optional] 

### Return type

[**ListMetatypeRelationshipPairsResponse**](ListMetatypeRelationshipPairsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_metatype_relationship_pair**
> GetMetatypeRelationshipPairResponse retrieve_metatype_relationship_pair(container_id, pair_id)

Retrieve Metatype Relationship Pair

Retrieves a single Metatype Relationship Pair.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipPairsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
pair_id = 'pair_id_example' # str | 

try:
    # Retrieve Metatype Relationship Pair
    api_response = api_instance.retrieve_metatype_relationship_pair(container_id, pair_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipPairsApi->retrieve_metatype_relationship_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **pair_id** | **str**|  | 

### Return type

[**GetMetatypeRelationshipPairResponse**](GetMetatypeRelationshipPairResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metatype_relationship_pair**
> UpdateMetatypeRelationshipPairResponse update_metatype_relationship_pair(container_id, pair_id, body=body)

Update Metaype Relationship Pair

Updates the specified metatype relationship pair.

### Example
```python
from __future__ import print_function
import time
import deep_lynx
from deep_lynx.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = deep_lynx.MetatypeRelationshipPairsApi(deep_lynx.ApiClient(configuration))
container_id = 'container_id_example' # str | 
pair_id = 'pair_id_example' # str | 
body = deep_lynx.RelationshipPair() # RelationshipPair |  (optional)

try:
    # Update Metaype Relationship Pair
    api_response = api_instance.update_metatype_relationship_pair(container_id, pair_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetatypeRelationshipPairsApi->update_metatype_relationship_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**|  | 
 **pair_id** | **str**|  | 
 **body** | [**RelationshipPair**](RelationshipPair.md)|  | [optional] 

### Return type

[**UpdateMetatypeRelationshipPairResponse**](UpdateMetatypeRelationshipPairResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

