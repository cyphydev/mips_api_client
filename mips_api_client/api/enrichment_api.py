# coding: utf-8

"""
    Mips UIUC Datatypes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mips_api_client.api_client import ApiClient


class EnrichmentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def enrichments_meta_delete(self, name, provider, tag, version, force, **kwargs):  # noqa: E501
        """Enrichments Meta Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enrichments_meta_delete(name, provider, tag, version, force, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str provider: (required)
        :param str tag: (required)
        :param str version: (required)
        :param bool force: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enrichments_meta_delete_with_http_info(name, provider, tag, version, force, **kwargs)  # noqa: E501
        else:
            (data) = self.enrichments_meta_delete_with_http_info(name, provider, tag, version, force, **kwargs)  # noqa: E501
            return data

    def enrichments_meta_delete_with_http_info(self, name, provider, tag, version, force, **kwargs):  # noqa: E501
        """Enrichments Meta Delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enrichments_meta_delete_with_http_info(name, provider, tag, version, force, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: (required)
        :param str provider: (required)
        :param str tag: (required)
        :param str version: (required)
        :param bool force: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'provider', 'tag', 'version', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enrichments_meta_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `enrichments_meta_delete`")  # noqa: E501
        # verify the required parameter 'provider' is set
        if ('provider' not in params or
                params['provider'] is None):
            raise ValueError("Missing the required parameter `provider` when calling `enrichments_meta_delete`")  # noqa: E501
        # verify the required parameter 'tag' is set
        if ('tag' not in params or
                params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `enrichments_meta_delete`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `enrichments_meta_delete`")  # noqa: E501
        # verify the required parameter 'force' is set
        if ('force' not in params or
                params['force'] is None):
            raise ValueError("Missing the required parameter `force` when calling `enrichments_meta_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'provider' in params:
            query_params.append(('provider', params['provider']))  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'force' in params:
            query_params.append(('force', params['force']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/enrichments/meta', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enrichments_meta_get(self, **kwargs):  # noqa: E501
        """Enrichments Meta Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enrichments_meta_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name:
        :param str provider:
        :param str tag:
        :param str version:
        :return: list[EnrichmentMeta]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enrichments_meta_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.enrichments_meta_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def enrichments_meta_get_with_http_info(self, **kwargs):  # noqa: E501
        """Enrichments Meta Get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enrichments_meta_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name:
        :param str provider:
        :param str tag:
        :param str version:
        :return: list[EnrichmentMeta]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'provider', 'tag', 'version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enrichments_meta_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'provider' in params:
            query_params.append(('provider', params['provider']))  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/enrichments/meta', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EnrichmentMeta]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def enrichments_meta_post(self, body, **kwargs):  # noqa: E501
        """Enrichments Meta Post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enrichments_meta_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EnrichmentMeta body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enrichments_meta_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.enrichments_meta_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def enrichments_meta_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Enrichments Meta Post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enrichments_meta_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EnrichmentMeta body: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enrichments_meta_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `enrichments_meta_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/enrichments/meta', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
