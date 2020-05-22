# swagger_client.SynonymsApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_any_designations**](SynonymsApi.md#get_all_any_designations) | **GET** /synonyms/all-any-designations | 
[**get_all_end_designations**](SynonymsApi.md#get_all_end_designations) | **GET** /synonyms/all-end-designations | 
[**get_all_substitutions_synonyms**](SynonymsApi.md#get_all_substitutions_synonyms) | **GET** /synonyms/all-substitutions-synonyms | 
[**get_designated_any_all_words**](SynonymsApi.md#get_designated_any_all_words) | **GET** /synonyms/designated-any-all-words | 
[**get_designated_end_all_words**](SynonymsApi.md#get_designated_end_all_words) | **GET** /synonyms/designated-end-all-words | 
[**get_designation_all_in_name**](SynonymsApi.md#get_designation_all_in_name) | **GET** /synonyms/designation-all-in-name | 
[**get_designation_any_in_name**](SynonymsApi.md#get_designation_any_in_name) | **GET** /synonyms/designation-any-in-name | 
[**get_designation_end_in_name**](SynonymsApi.md#get_designation_end_in_name) | **GET** /synonyms/designation-end-in-name | 
[**get_designations**](SynonymsApi.md#get_designations) | **GET** /synonyms/designations | 
[**get_entity_type_any_designation**](SynonymsApi.md#get_entity_type_any_designation) | **GET** /synonyms/entity-type-any-designation | 
[**get_entity_type_by_value**](SynonymsApi.md#get_entity_type_by_value) | **GET** /synonyms/entity-type-by-value | 
[**get_entity_type_end_designation**](SynonymsApi.md#get_entity_type_end_designation) | **GET** /synonyms/entity-type-end-designation | 
[**get_exception_regex**](SynonymsApi.md#get_exception_regex) | **GET** /synonyms/exception-regex | 
[**get_incorrect_designation_end_in_name**](SynonymsApi.md#get_incorrect_designation_end_in_name) | **GET** /synonyms/incorrect-designation-end-in-name | 
[**get_misplaced_any_designations**](SynonymsApi.md#get_misplaced_any_designations) | **GET** /synonyms/misplaced-any-designations | 
[**get_misplaced_end_designations**](SynonymsApi.md#get_misplaced_end_designations) | **GET** /synonyms/misplaced-end-designations | 
[**get_number_words**](SynonymsApi.md#get_number_words) | **GET** /synonyms/number-words | 
[**get_prefixes**](SynonymsApi.md#get_prefixes) | **GET** /synonyms/prefixes | 
[**get_regex_prefixes**](SynonymsApi.md#get_regex_prefixes) | **GET** /synonyms/regex-prefixes | 
[**get_stop_words**](SynonymsApi.md#get_stop_words) | **GET** /synonyms/stop-words | 
[**get_synonyms**](SynonymsApi.md#get_synonyms) | **GET** /synonyms/{col}/{term} | 
[**get_transform_text**](SynonymsApi.md#get_transform_text) | **GET** /synonyms/transform-text | 
[**get_word_substitutions**](SynonymsApi.md#get_word_substitutions) | **GET** /synonyms/substitutions | 
[**get_word_synonyms**](SynonymsApi.md#get_word_synonyms) | **GET** /synonyms/synonyms | 


# **get_all_any_designations**
> SynonymDictionaryList get_all_any_designations()



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
    api_response = api_instance.get_all_any_designations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_all_any_designations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SynonymDictionaryList**](SynonymDictionaryList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_end_designations**
> SynonymDictionaryList get_all_end_designations()



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
    api_response = api_instance.get_all_end_designations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_all_end_designations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SynonymDictionaryList**](SynonymDictionaryList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_substitutions_synonyms**
> SynonymDictionaryList get_all_substitutions_synonyms(words=words, words_are_distinctive=words_are_distinctive)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
words = 'words_example' # str |  (optional)
words_are_distinctive = 'words_are_distinctive_example' # str |  (optional)

try:
    api_response = api_instance.get_all_substitutions_synonyms(words=words, words_are_distinctive=words_are_distinctive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_all_substitutions_synonyms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **words** | **str**|  | [optional] 
 **words_are_distinctive** | **str**|  | [optional] 

### Return type

[**SynonymDictionaryList**](SynonymDictionaryList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_designated_any_all_words**
> SynonymList get_designated_any_all_words(entity_type_code=entity_type_code, position_code=position_code, lang=lang)



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
    api_response = api_instance.get_designated_any_all_words(entity_type_code=entity_type_code, position_code=position_code, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_designated_any_all_words: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type_code** | **str**|  | [optional] 
 **position_code** | **str**|  | [optional] 
 **lang** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_designated_end_all_words**
> SynonymList get_designated_end_all_words(entity_type_code=entity_type_code, position_code=position_code, lang=lang)



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
    api_response = api_instance.get_designated_end_all_words(entity_type_code=entity_type_code, position_code=position_code, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_designated_end_all_words: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type_code** | **str**|  | [optional] 
 **position_code** | **str**|  | [optional] 
 **lang** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_designation_all_in_name**
> SynonymList get_designation_all_in_name(name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
name = 'name_example' # str |  (optional)

try:
    api_response = api_instance.get_designation_all_in_name(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_designation_all_in_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_designation_any_in_name**
> SynonymList get_designation_any_in_name(name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
name = 'name_example' # str |  (optional)

try:
    api_response = api_instance.get_designation_any_in_name(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_designation_any_in_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_designation_end_in_name**
> SynonymList get_designation_end_in_name(name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
name = 'name_example' # str |  (optional)

try:
    api_response = api_instance.get_designation_end_in_name(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_designation_end_in_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_designations**
> SynonymList get_designations(entity_type_code=entity_type_code, position_code=position_code, lang=lang)



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
    api_response = api_instance.get_designations(entity_type_code=entity_type_code, position_code=position_code, lang=lang)
    pprint(api_response)
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

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_type_any_designation**
> SynonymList get_entity_type_any_designation(entity_any_designation_dict=entity_any_designation_dict, all_designation_any_end_list=all_designation_any_end_list)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
entity_any_designation_dict = 'entity_any_designation_dict_example' # str |  (optional)
all_designation_any_end_list = 'all_designation_any_end_list_example' # str |  (optional)

try:
    api_response = api_instance.get_entity_type_any_designation(entity_any_designation_dict=entity_any_designation_dict, all_designation_any_end_list=all_designation_any_end_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_entity_type_any_designation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_any_designation_dict** | **str**|  | [optional] 
 **all_designation_any_end_list** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_type_by_value**
> SynonymList get_entity_type_by_value(entity_type_dicts=entity_type_dicts, designation=designation)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
entity_type_dicts = 'entity_type_dicts_example' # str |  (optional)
designation = 'designation_example' # str |  (optional)

try:
    api_response = api_instance.get_entity_type_by_value(entity_type_dicts=entity_type_dicts, designation=designation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_entity_type_by_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type_dicts** | **str**|  | [optional] 
 **designation** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_type_end_designation**
> SynonymList get_entity_type_end_designation(entity_end_designation_dict=entity_end_designation_dict, all_designation_any_end_list=all_designation_any_end_list)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
entity_end_designation_dict = 'entity_end_designation_dict_example' # str |  (optional)
all_designation_any_end_list = 'all_designation_any_end_list_example' # str |  (optional)

try:
    api_response = api_instance.get_entity_type_end_designation(entity_end_designation_dict=entity_end_designation_dict, all_designation_any_end_list=all_designation_any_end_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_entity_type_end_designation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_end_designation_dict** | **str**|  | [optional] 
 **all_designation_any_end_list** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exception_regex**
> SynonymList get_exception_regex(text=text)



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

try:
    api_response = api_instance.get_exception_regex(text=text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_exception_regex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_incorrect_designation_end_in_name**
> SynonymList get_incorrect_designation_end_in_name(tokenized_name=tokenized_name, designation_end_list=designation_end_list)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
tokenized_name = 'tokenized_name_example' # str |  (optional)
designation_end_list = 'designation_end_list_example' # str |  (optional)

try:
    api_response = api_instance.get_incorrect_designation_end_in_name(tokenized_name=tokenized_name, designation_end_list=designation_end_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_incorrect_designation_end_in_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenized_name** | **str**|  | [optional] 
 **designation_end_list** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_misplaced_any_designations**
> SynonymList get_misplaced_any_designations(name=name, designation_any_entity_type=designation_any_entity_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
name = 'name_example' # str |  (optional)
designation_any_entity_type = 'designation_any_entity_type_example' # str |  (optional)

try:
    api_response = api_instance.get_misplaced_any_designations(name=name, designation_any_entity_type=designation_any_entity_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_misplaced_any_designations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **designation_any_entity_type** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_misplaced_end_designations**
> SynonymList get_misplaced_end_designations(name=name, designation_end_entity_type=designation_end_entity_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
name = 'name_example' # str |  (optional)
designation_end_entity_type = 'designation_end_entity_type_example' # str |  (optional)

try:
    api_response = api_instance.get_misplaced_end_designations(name=name, designation_end_entity_type=designation_end_entity_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_misplaced_end_designations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **designation_end_entity_type** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_number_words**
> SynonymList get_number_words()



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
    api_response = api_instance.get_number_words()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_number_words: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prefixes**
> SynonymList get_prefixes()



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
    api_response = api_instance.get_prefixes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_prefixes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_regex_prefixes**
> String get_regex_prefixes(text=text, prefixes_str=prefixes_str, exception_designation=exception_designation)



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
prefixes_str = 'prefixes_str_example' # str |  (optional)
exception_designation = 'exception_designation_example' # str |  (optional)

try:
    api_response = api_instance.get_regex_prefixes(text=text, prefixes_str=prefixes_str, exception_designation=exception_designation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_regex_prefixes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**|  | [optional] 
 **prefixes_str** | **str**|  | [optional] 
 **exception_designation** | **str**|  | [optional] 

### Return type

[**String**](String.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stop_words**
> SynonymList get_stop_words(word=word)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
word = 'word_example' # str |  (optional)

try:
    api_response = api_instance.get_stop_words(word=word)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_stop_words: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **word** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

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
    print("Exception when calling SynonymsApi->get_transform_text: %s\n" % e)
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
> SynonymList get_word_substitutions(word=word)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
word = 'word_example' # str |  (optional)

try:
    api_response = api_instance.get_word_substitutions(word=word)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_word_substitutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **word** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_word_synonyms**
> SynonymList get_word_synonyms(word=word)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SynonymsApi()
word = 'word_example' # str |  (optional)

try:
    api_response = api_instance.get_word_synonyms(word=word)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynonymsApi->get_word_synonyms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **word** | **str**|  | [optional] 

### Return type

[**SynonymList**](SynonymList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

