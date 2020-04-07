# coding: utf-8

"""
    Synonyms API

    Retrieves the sets of synonyms for a given word.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SynonymsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_designations(self, **kwargs):  # noqa: E501
        """get_designations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_designations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type_code: 
        :param str position_code: 
        :param str lang: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_designations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_designations_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_designations_with_http_info(self, **kwargs):  # noqa: E501
        """get_designations  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_designations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type_code: 
        :param str position_code: 
        :param str lang: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type_code', 'position_code', 'lang']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_designations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'entity_type_code' in params:
            query_params.append(('entity_type_code', params['entity_type_code']))  # noqa: E501
        if 'position_code' in params:
            query_params.append(('position_code', params['position_code']))  # noqa: E501
        if 'lang' in params:
            query_params.append(('lang', params['lang']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/synonyms/designations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_number_words(self, **kwargs):  # noqa: E501
        """get_number_words  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_number_words(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_number_words_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_number_words_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_number_words_with_http_info(self, **kwargs):  # noqa: E501
        """get_number_words  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_number_words_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_number_words" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/synonyms/number-words', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_prefixes(self, **kwargs):  # noqa: E501
        """get_prefixes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prefixes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_prefixes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_prefixes_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_prefixes_with_http_info(self, **kwargs):  # noqa: E501
        """get_prefixes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_prefixes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_prefixes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/synonyms/prefixes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_synonyms(self, col, term, **kwargs):  # noqa: E501
        """get_synonyms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_synonyms(col, term, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str col: (required)
        :param str term: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_synonyms_with_http_info(col, term, **kwargs)  # noqa: E501
        else:
            (data) = self.get_synonyms_with_http_info(col, term, **kwargs)  # noqa: E501
            return data

    def get_synonyms_with_http_info(self, col, term, **kwargs):  # noqa: E501
        """get_synonyms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_synonyms_with_http_info(col, term, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str col: (required)
        :param str term: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['col', 'term']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_synonyms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'col' is set
        if ('col' not in params or
                params['col'] is None):
            raise ValueError("Missing the required parameter `col` when calling `get_synonyms`")  # noqa: E501
        # verify the required parameter 'term' is set
        if ('term' not in params or
                params['term'] is None):
            raise ValueError("Missing the required parameter `term` when calling `get_synonyms`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'col' in params:
            path_params['col'] = params['col']  # noqa: E501
        if 'term' in params:
            path_params['term'] = params['term']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/synonyms/{col}/{term}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transform_text(self, **kwargs):  # noqa: E501
        """get_transform_text  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transform_text(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str text: 
        :param str designation_all: 
        :param str prefix_list: 
        :param str number_list: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transform_text_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_transform_text_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_transform_text_with_http_info(self, **kwargs):  # noqa: E501
        """get_transform_text  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transform_text_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str text: 
        :param str designation_all: 
        :param str prefix_list: 
        :param str number_list: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['text', 'designation_all', 'prefix_list', 'number_list']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transform_text" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text' in params:
            query_params.append(('text', params['text']))  # noqa: E501
        if 'designation_all' in params:
            query_params.append(('designation_all', params['designation_all']))  # noqa: E501
        if 'prefix_list' in params:
            query_params.append(('prefix_list', params['prefix_list']))  # noqa: E501
        if 'number_list' in params:
            query_params.append(('number_list', params['number_list']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/synonyms/transform-text', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_word_stops(self, word, **kwargs):  # noqa: E501
        """get_word_stops  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_word_stops(word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str word: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_word_stops_with_http_info(word, **kwargs)  # noqa: E501
        else:
            (data) = self.get_word_stops_with_http_info(word, **kwargs)  # noqa: E501
            return data

    def get_word_stops_with_http_info(self, word, **kwargs):  # noqa: E501
        """get_word_stops  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_word_stops_with_http_info(word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str word: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['word']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_word_stops" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'word' is set
        if ('word' not in params or
                params['word'] is None):
            raise ValueError("Missing the required parameter `word` when calling `get_word_stops`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'word' in params:
            path_params['word'] = params['word']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/synonyms/stop-words/{word}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_word_substitutions(self, word, **kwargs):  # noqa: E501
        """get_word_substitutions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_word_substitutions(word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str word: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_word_substitutions_with_http_info(word, **kwargs)  # noqa: E501
        else:
            (data) = self.get_word_substitutions_with_http_info(word, **kwargs)  # noqa: E501
            return data

    def get_word_substitutions_with_http_info(self, word, **kwargs):  # noqa: E501
        """get_word_substitutions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_word_substitutions_with_http_info(word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str word: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['word']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_word_substitutions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'word' is set
        if ('word' not in params or
                params['word'] is None):
            raise ValueError("Missing the required parameter `word` when calling `get_word_substitutions`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'word' in params:
            path_params['word'] = params['word']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/synonyms/substitutions/{word}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_word_synonyms(self, word, **kwargs):  # noqa: E501
        """get_word_synonyms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_word_synonyms(word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str word: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_word_synonyms_with_http_info(word, **kwargs)  # noqa: E501
        else:
            (data) = self.get_word_synonyms_with_http_info(word, **kwargs)  # noqa: E501
            return data

    def get_word_synonyms_with_http_info(self, word, **kwargs):  # noqa: E501
        """get_word_synonyms  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_word_synonyms_with_http_info(word, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str word: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['word']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_word_synonyms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'word' is set
        if ('word' not in params or
                params['word'] is None):
            raise ValueError("Missing the required parameter `word` when calling `get_word_synonyms`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'word' in params:
            path_params['word'] = params['word']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/synonyms/synonyms/{word}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
