# swagger-client
Retrieves the sets of synonyms for a given word.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NameProcessingApi(swagger_client.ApiClient(configuration))

try:
    api_instance.get_word_classification()
except ApiException as e:
    print("Exception when calling NameProcessingApi->get_word_classification: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://solr-synonyms-api.servicebc-ne-dev.svc:8080/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*NameProcessingApi* | [**get_word_classification**](docs/NameProcessingApi.md#get_word_classification) | **GET** /name-processing/ | 
*ProbesApi* | [**get_liveness**](docs/ProbesApi.md#get_liveness) | **GET** /synonyms/probes/liveness | 
*ProbesApi* | [**get_readiness**](docs/ProbesApi.md#get_readiness) | **GET** /synonyms/probes/readiness | 
*SynonymsApi* | [**get_all_any_designations**](docs/SynonymsApi.md#get_all_any_designations) | **GET** /synonyms/all-any-designations | 
*SynonymsApi* | [**get_all_end_designations**](docs/SynonymsApi.md#get_all_end_designations) | **GET** /synonyms/all-end-designations | 
*SynonymsApi* | [**get_all_substitutions_synonyms**](docs/SynonymsApi.md#get_all_substitutions_synonyms) | **GET** /synonyms/all-substitutions-synonyms | 
*SynonymsApi* | [**get_designated_any_all_words**](docs/SynonymsApi.md#get_designated_any_all_words) | **GET** /synonyms/designated-any-all-words | 
*SynonymsApi* | [**get_designated_end_all_words**](docs/SynonymsApi.md#get_designated_end_all_words) | **GET** /synonyms/designated-end-all-words | 
*SynonymsApi* | [**get_designation_all_in_name**](docs/SynonymsApi.md#get_designation_all_in_name) | **GET** /synonyms/designation-all-in-name | 
*SynonymsApi* | [**get_designation_any_in_name**](docs/SynonymsApi.md#get_designation_any_in_name) | **GET** /synonyms/designation-any-in-name | 
*SynonymsApi* | [**get_designation_end_in_name**](docs/SynonymsApi.md#get_designation_end_in_name) | **GET** /synonyms/designation-end-in-name | 
*SynonymsApi* | [**get_designations**](docs/SynonymsApi.md#get_designations) | **GET** /synonyms/designations | 
*SynonymsApi* | [**get_entity_type_any_designation**](docs/SynonymsApi.md#get_entity_type_any_designation) | **GET** /synonyms/entity-type-any-designation | 
*SynonymsApi* | [**get_entity_type_by_value**](docs/SynonymsApi.md#get_entity_type_by_value) | **GET** /synonyms/entity-type-by-value | 
*SynonymsApi* | [**get_entity_type_end_designation**](docs/SynonymsApi.md#get_entity_type_end_designation) | **GET** /synonyms/entity-type-end-designation | 
*SynonymsApi* | [**get_exception_regex**](docs/SynonymsApi.md#get_exception_regex) | **GET** /synonyms/exception-regex | 
*SynonymsApi* | [**get_incorrect_designation_end_in_name**](docs/SynonymsApi.md#get_incorrect_designation_end_in_name) | **GET** /synonyms/incorrect-designation-end-in-name | 
*SynonymsApi* | [**get_misplaced_any_designations**](docs/SynonymsApi.md#get_misplaced_any_designations) | **GET** /synonyms/misplaced-any-designations | 
*SynonymsApi* | [**get_misplaced_end_designations**](docs/SynonymsApi.md#get_misplaced_end_designations) | **GET** /synonyms/misplaced-end-designations | 
*SynonymsApi* | [**get_number_words**](docs/SynonymsApi.md#get_number_words) | **GET** /synonyms/number-words | 
*SynonymsApi* | [**get_prefixes**](docs/SynonymsApi.md#get_prefixes) | **GET** /synonyms/prefixes | 
*SynonymsApi* | [**get_stop_words**](docs/SynonymsApi.md#get_stop_words) | **GET** /synonyms/stop-words | 
*SynonymsApi* | [**get_synonyms**](docs/SynonymsApi.md#get_synonyms) | **GET** /synonyms/{col}/{term} | 
*SynonymsApi* | [**get_transform_text**](docs/SynonymsApi.md#get_transform_text) | **GET** /synonyms/transform-text | 
*SynonymsApi* | [**get_word_substitutions**](docs/SynonymsApi.md#get_word_substitutions) | **GET** /synonyms/substitutions | 
*SynonymsApi* | [**get_word_synonyms**](docs/SynonymsApi.md#get_word_synonyms) | **GET** /synonyms/synonyms | 


## Documentation For Models

 - [DictionaryList](docs/DictionaryList.md)
 - [String](docs/String.md)
 - [SynonymDictionaryList](docs/SynonymDictionaryList.md)
 - [SynonymList](docs/SynonymList.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



