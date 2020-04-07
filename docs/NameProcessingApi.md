# swagger_client.NameProcessingApi

All URIs are relative to *https://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_word_classification**](NameProcessingApi.md#get_word_classification) | **GET** /name-processing/ | 


# **get_word_classification**
> get_word_classification()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NameProcessingApi()

try:
    api_instance.get_word_classification()
except ApiException as e:
    print("Exception when calling NameProcessingApi->get_word_classification: %s\n" % e)
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

