# swagger_client.SynonymsApi

All URIs are relative to *http://localhost:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_designations**](SynonymsApi.md#get_designations) | **GET** /synonyms/designations | 
[**get_number_words**](SynonymsApi.md#get_number_words) | **GET** /synonyms/number-words | 
[**get_prefixes**](SynonymsApi.md#get_prefixes) | **GET** /synonyms/prefixes | 
[**get_synonyms**](SynonymsApi.md#get_synonyms) | **GET** /synonyms/{col}/{term} | 
[**get_transform_text**](SynonymsApi.md#get_transform_text) | **GET** /synonyms/transform-text | 
[**get_word_stops**](SynonymsApi.md#get_word_stops) | **GET** /synonyms/stop-words/{word} | 
[**get_word_substitutions**](SynonymsApi.md#get_word_substitutions) | **GET** /synonyms/substitutions/{word} | 
[**get_word_synonyms**](SynonymsApi.md#get_word_synonyms) | **GET** /synonyms/synonyms/{word} | 


# **get_designations**
> get_designations(entity_type_code=entity_type_code, position_code=position_code, lang=lang)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
entity_type_code = 'entity_type_code_example' # str |  (optional)
position_code = 'position_code_example' # str |  (optional)
lang = 'lang_example' # str |  (optional)

try:
    api_instance.get_designations(entity_type_code=entity_type_code, position_code=position_code, lang=lang)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_designations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type_code** | **str**|  | [optional] 
 **position_code** | **str**|  | [optional] 
 **lang** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_number_words**
> get_number_words()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()

try:
    api_instance.get_number_words()
except ApiException as e:
    print("Exception when calling SynonymsApi->get_number_words: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prefixes**
> get_prefixes()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()

try:
    api_instance.get_prefixes()
except ApiException as e:
    print("Exception when calling SynonymsApi->get_prefixes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_synonyms**
> get_synonyms(col, term)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
col = 'col_example' # str | 
term = 'term_example' # str | 

try:
    api_instance.get_synonyms(col, term)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_synonyms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **col** | **str**|  | 
 **term** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transform_text**
> get_transform_text(text=text, designation_all=designation_all, prefix_list=prefix_list, number_list=number_list)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
text = 'text_example' # str |  (optional)
designation_all = 'designation_all_example' # str |  (optional)
prefix_list = 'prefix_list_example' # str |  (optional)
number_list = 'number_list_example' # str |  (optional)

try:
    api_instance.get_transform_text(text=text, designation_all=designation_all, prefix_list=prefix_list, number_list=number_list)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_transform_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**|  | [optional] 
 **designation_all** | **str**|  | [optional] 
 **prefix_list** | **str**|  | [optional] 
 **number_list** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transform_text**
> String get_transform_text(text=text, designation_all=designation_all, prefix_list=prefix_list, number_list=number_list, exceptions_ws=exceptions_ws)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
text = 'text_example' # str |  (optional)
designation_all = 'designation_all_example' # str |  (optional)
prefix_list = 'prefix_list_example' # str |  (optional)
number_list = 'number_list_example' # str |  (optional)
exceptions_ws = 'exceptions_ws_example' # str |  (optional)

try:
    api_response = api_instance.get_transform_text(text=text, designation_all=designation_all, prefix_list=prefix_list, number_list=number_list, exceptions_ws=exceptions_ws)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_word_stops: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**|  | [optional] 
 **designation_all** | **str**|  | [optional] 
 **prefix_list** | **str**|  | [optional] 
 **number_list** | **str**|  | [optional] 
 **exceptions_ws** | **str**|  | [optional] 

### Return type

[**String**](String.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_word_substitutions**
> get_word_substitutions(word)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
word = 'word_example' # str | 

try:
    api_instance.get_word_substitutions(word)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_word_substitutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **word** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_word_synonyms**
> get_word_synonyms(word)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
word = 'word_example' # str | 

try:
    api_instance.get_word_synonyms(word)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_word_synonyms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **word** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

