import unittest

import ESI_to_py
import ESI_request


class Test_ESIReader(unittest.TestCase):
    def test_pythonic_name(self):
        non_pythonic_name = 'CamelCase-With-Hyphen'
        pythonic_name = 'camelcase_with_hyphen'
        self.assertEqual(ESI_to_py._pythonic_name(non_pythonic_name),
                         pythonic_name)

    def test_convert_parameters(self):
        ESI_parameters = {'pythonic_name': None, 'CamelCase-With-Hyphen': True}
        ESI_parameters_with_addition = {'pythonic_name': None,
                                         'CamelCase-With-Hyphen': True,
                                         'camelcase_with_hyphen': True}
        ESI_to_py._convert_parameters(ESI_parameters)
        self.assertEqual(ESI_parameters, ESI_parameters_with_addition)

    def test_get_parameters_with_description(self): # TODO Extract dicts and string in different file (line to long)
        function_dict = {'parameters': [{'$ref': '#/parameters/datasource'}, {'$ref': '#/parameters/language', 'enum':['de', 'en-us', 'fr', 'ja', 'ru', 'zh']}, {'description': 'ID for a war', 'format': 'int32', 'in': 'path', 'minimum': 1, 'name': 'war_id', 'required': True, 'type': 'integer'}]}
        parameters = {'Accept-Language': {'default': 'en-us', 'description': 'Language to use in the response', 'enum': ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'], 'in': 'header', 'name': 'Accept-Language', 'type': 'string'}, 'If-None-Match': {'description': 'ETag from a previous request. A 304 will be returned if this matches the current ETag', 'in': 'header', 'name': 'If-None-Match', 'type': 'string'}, 'alliance_id': {'description': 'An EVE alliance ID', 'format': 'int32', 'in': 'path', 'minimum': 1, 'name': 'alliance_id', 'required': True, 'type': 'integer'}, 'character_id': {'description': 'An EVE character ID', 'format': 'int32', 'in': 'path', 'minimum': 1, 'name': 'character_id', 'required': True, 'type': 'integer'}, 'corporation_id': {'description': 'An EVE corporation ID', 'format': 'int32', 'in': 'path', 'minimum': 1, 'name': 'corporation_id', 'required': True, 'type': 'integer'}, 'datasource': {'default': 'tranquility', 'description': 'The server name you would like data from', 'enum': ['tranquility', 'singularity'], 'in': 'query', 'name': 'datasource', 'type': 'string'}, 'language': {'default': 'en-us', 'description': 'Language to use in the response, takes precedence over Accept-Language', 'enum': ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'], 'in': 'query', 'name': 'language', 'type': 'string'}, 'page': {'default': 1, 'description': 'Which page of results to return', 'format': 'int32', 'in': 'query', 'minimum': 1, 'name': 'page', 'type': 'integer'}, 'token': {'description': 'Access token to use if unable to set a header', 'in': 'query', 'name': 'token', 'type': 'string'}, 'accept_language': {'default': 'en-us', 'description': 'Language to use in the response', 'enum': ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'], 'in': 'header', 'name': 'Accept-Language', 'type': 'string'}, 'if_none_match': {'description': 'ETag from a previous request. A 304 will be returned if this matches the current ETag', 'in': 'header', 'name': 'If-None-Match', 'type': 'string'}}
        full_description = ESI_to_py._get_parameters_with_description(
                               function_dict=function_dict,
                               parameters=parameters)
        expected_description = ''':param language: ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'] Language to use in the response, takes precedence over Accept-Language
    :param war_id: ID for a war\n    '''
        self.assertEqual(expected_description, full_description)

    def test_format_code(self):
        """Minimal test. For further tests see package tests"""
        test_code = 'x=1'
        expected_code = 'x = 1\n'
        returned_code = ESI_to_py._format_code(test_code)
        self.assertEqual(expected_code, returned_code)

    def test_write_to_file(self):
        pass # TODO Test file creation and content

    def test_create_doc_string(self): # TODO Extract dicts and string in different file (line to long)
        ESI_parameters = {'Accept-Language': {'default': 'en-us', 'description': 'Language to use in the response', 'enum': ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'], 'in': 'header', 'name': 'Accept-Language', 'type': 'string'}, 'If-None-Match': {'description': 'ETag from a previous request. A 304 will be returned if this matches the current ETag', 'in': 'header', 'name': 'If-None-Match', 'type': 'string'}, 'alliance_id': {'description': 'An EVE alliance ID', 'format': 'int32', 'in': 'path', 'minimum': 1, 'name': 'alliance_id', 'required': True, 'type': 'integer'}, 'character_id': {'description': 'An EVE character ID', 'format': 'int32', 'in': 'path', 'minimum': 1, 'name': 'character_id', 'required': True, 'type': 'integer'}, 'corporation_id': {'description': 'An EVE corporation ID', 'format': 'int32', 'in': 'path', 'minimum': 1, 'name': 'corporation_id', 'required': True, 'type': 'integer'}, 'datasource': {'default': 'tranquility', 'description': 'The server name you would like data from', 'enum': ['tranquility', 'singularity'], 'in': 'query', 'name': 'datasource', 'type': 'string'}, 'language': {'default': 'en-us', 'description': 'Language to use in the response, takes precedence over Accept-Language', 'enum': ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'], 'in': 'query', 'name': 'language', 'type': 'string'}, 'page': {'default': 1, 'description': 'Which page of results to return', 'format': 'int32', 'in': 'query', 'minimum': 1, 'name': 'page', 'type': 'integer'}, 'token': {'description': 'Access token to use if unable to set a header', 'in': 'query', 'name': 'token', 'type': 'string'}, 'accept_language': {'default': 'en-us', 'description': 'Language to use in the response', 'enum': ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'], 'in': 'header', 'name': 'Accept-Language', 'type': 'string'}, 'if_none_match': {'description': 'ETag from a previous request. A 304 will be returned if this matches the current ETag', 'in': 'header', 'name': 'If-None-Match', 'type': 'string'}}
        function_dict = {'description': 'Return a list of kills related to a war\n\n---\nAlternate route: `/dev/wars/{war_id}/killmails/`\n\nAlternate route: `/legacy/wars/{war_id}/killmails/`\n\nAlternate route: `/v1/wars/{war_id}/killmails/`\n\n---\nThis route is cached for up to 3600 seconds', 'operationId': 'get_wars_war_id_killmails', 'parameters': [{'$ref': '#/parameters/datasource'}, {'$ref': '#/parameters/If-None-Match'}, {'$ref': '#/parameters/page'}, {'description': 'A valid war ID', 'format': 'int32', 'in': 'path', 'minimum': 1, 'name': 'war_id', 'required': True, 'type': 'integer'}], 'responses': {'200': {'description': 'A list of killmail IDs and hashes', 'examples': {'application/json': [{'killmail_hash': '8eef5e8fb6b88fe3407c489df33822b2e3b57a5e', 'killmail_id': 2}, {'killmail_hash': 'b41ccb498ece33d64019f64c0db392aa3aa701fb', 'killmail_id': 1}]}, 'headers': {'Cache-Control': {'description': 'The caching mechanism used', 'type': 'string'}, 'ETag': {'description': 'RFC7232 compliant entity tag', 'type': 'string'}, 'Expires': {'description': 'RFC7231 formatted datetime string', 'type': 'string'}, 'Last-Modified': {'description': 'RFC7231 formatted datetime string', 'type': 'string'}, 'X-Pages': {'default': 1, 'description': 'Maximum page number', 'format': 'int32', 'type': 'integer'}}, 'schema': {'description': '200 ok array', 'items': {'description': '200 ok object', 'properties': {'killmail_hash': {'description': 'A hash of this killmail', 'title': 'get_wars_war_id_killmails_killmail_hash', 'type': 'string'}, 'killmail_id': {'description': 'ID of this killmail', 'format': 'int32', 'title': 'get_wars_war_id_killmails_killmail_id', 'type': 'integer'}}, 'required': ['killmail_id', 'killmail_hash'], 'title': 'get_wars_war_id_killmails_200_ok', 'type': 'object'}, 'maxItems': 2000, 'title': 'get_wars_war_id_killmails_ok', 'type': 'array'}}, '304': {'description': 'Not modified', 'headers': {'Cache-Control': {'description': 'The caching mechanism used', 'type': 'string'}, 'ETag': {'description': 'RFC7232 compliant entity tag', 'type': 'string'}, 'Expires': {'description': 'RFC7231 formatted datetime string', 'type': 'string'}, 'Last-Modified': {'description': 'RFC7231 formatted datetime string', 'type': 'string'}}}, '400': {'description': 'Bad request', 'examples': {'application/json': {'error': 'Bad request message'}}, 'schema': {'$ref': '#/definitions/bad_request'}}, '420': {'description': 'Error limited', 'examples': {'application/json': {'error': 'Error limited message'}}, 'schema': {'$ref': '#/definitions/error_limited'}}, '422': {'description': 'War not found', 'examples': {'application/json': {'error': 'Unprocessable entity message'}}, 'schema': {'description': 'Unprocessable entity', 'properties': {'error': {'description': 'Unprocessable entity message', 'title': 'get_wars_war_id_killmails_422_unprocessable_entity', 'type': 'string'}}, 'title': 'get_wars_war_id_killmails_unprocessable_entity', 'type': 'object'}}, '500': {'description': 'Internal server error', 'examples': {'application/json': {'error': 'Internal server error message'}}, 'schema': {'$ref': '#/definitions/internal_server_error'}}, '503': {'description': 'Service unavailable', 'examples': {'application/json': {'error': 'Service unavailable message'}}, 'schema': {'$ref': '#/definitions/service_unavailable'}}, '504': {'description': 'Gateway timeout', 'examples': {'application/json': {'error': 'Gateway timeout message'}}, 'schema': {'$ref': '#/definitions/gateway_timeout'}}}, 'summary': 'List kills for a war', 'tags': ['Wars'], 'x-alternate-versions': ['dev', 'legacy', 'v1'], 'x-cached-seconds': 3600}
        expected_doc_string = '''\n    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param page: Which page of results to return
    :param war_id: A valid war ID
    Return a list of kills related to a war
    ---
    Alternate route: `/dev/wars/{war_id}/killmails/`
    Alternate route: `/legacy/wars/{war_id}/killmails/`
    Alternate route: `/v1/wars/{war_id}/killmails/`
    ---
    This route is cached for up to 3600 seconds
    """\n'''
        doc_string = ESI_to_py._create_doc_string(ESI_parameters=ESI_parameters,
                                                  function_dict=function_dict)
        self.assertEqual(expected_doc_string, doc_string)

    def test_filter_parameter_no_keyword(self):
        expected = ', one'
        returned = ESI_to_py._filter_parameter('one')
        self.assertEqual(expected, returned)

    def test_filter_parameter_unfiltered_as_keyword(self):
        expected = ', one=one'
        returned = ESI_to_py._filter_parameter('one', as_key_word=True)
        self.assertEqual(expected, returned)

    def test_filter_parameter_filtered_not_keyword(self):
        parameters = {'datasource': '',
                      'If-None-Match': ', if_none_match=None',
                      'Accept-Language': ", accept_language='en-us'",
                      'page': ", page='1'"}
        for parameter, expected in parameters.items():
            returned = ESI_to_py._filter_parameter(parameter)
            self.assertEqual(expected, returned)

    def test_filter_parameter_filtered_as_keyword(self):
        parameters = {'datasource': '',
                      'If-None-Match': ', if_none_match=if_none_match',
                      'Accept-Language': ', accept_language=accept_language',
                      'page': ', page=page'}
        for parameter, expected in parameters.items():
            returned = ESI_to_py._filter_parameter(parameter, as_key_word=True)
            self.assertEqual(expected, returned)

    def test_shuffle_kwargs_to_the_end(self):
        test = ', arg_1, kwarg_1=kwarg_1, arg_2, kwarg_2=kwarg_2, arg_3'
        returned = ESI_to_py._shuffle_kwargs_to_the_end(test)
        expected = ', arg_1, arg_2, arg_3, kwarg_1=kwarg_1, kwarg_2=kwarg_2'
        self.assertEqual(expected, returned)

    def test_create_functions(self): # TODO Extract dicts and string in different file (line to long)
        ESI_parameters = {'Accept-Language': {'default': 'en-us', 'description': 'Language to use in the response', 'enum': ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'], 'in': 'header', 'name': 'Accept-Language', 'type': 'string'}, 'If-None-Match': {'description': 'ETag from a previous request. A 304 will be returned if this matches the current ETag', 'in': 'header', 'name': 'If-None-Match', 'type': 'string'}, 'alliance_id': {'description': 'An EVE alliance ID', 'format': 'int32', 'in': 'path', 'minimum': 1, 'name': 'alliance_id', 'required': True, 'type': 'integer'}, 'character_id': {'description': 'An EVE character ID', 'format': 'int32', 'in': 'path', 'minimum': 1, 'name': 'character_id', 'required': True, 'type': 'integer'}, 'corporation_id': {'description': 'An EVE corporation ID', 'format': 'int32', 'in': 'path', 'minimum': 1, 'name': 'corporation_id', 'required': True, 'type': 'integer'}, 'datasource': {'default': 'tranquility', 'description': 'The server name you would like data from', 'enum': ['tranquility', 'singularity'], 'in': 'query', 'name': 'datasource', 'type': 'string'}, 'language': {'default': 'en-us', 'description': 'Language to use in the response, takes precedence over Accept-Language', 'enum': ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'], 'in': 'query', 'name': 'language', 'type': 'string'}, 'page': {'default': 1, 'description': 'Which page of results to return', 'format': 'int32', 'in': 'query', 'minimum': 1, 'name': 'page', 'type': 'integer'}, 'token': {'description': 'Access token to use if unable to set a header', 'in': 'query', 'name': 'token', 'type': 'string'}, 'accept_language': {'default': 'en-us', 'description': 'Language to use in the response', 'enum': ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'], 'in': 'header', 'name': 'Accept-Language', 'type': 'string'}, 'if_none_match': {'description': 'ETag from a previous request. A 304 will be returned if this matches the current ETag', 'in': 'header', 'name': 'If-None-Match', 'type': 'string'}}
        ESI_paths = {'/wars/': {'get': {'description': 'Return a list of wars\n\n---\nAlternate route: `/dev/wars/`\n\nAlternate route: `/legacy/wars/`\n\nAlternate route: `/v1/wars/`\n\n---\nThis route is cached for up to 3600 seconds', 'operationId': 'get_wars', 'parameters': [{'$ref': '#/parameters/datasource'}, {'$ref': '#/parameters/If-None-Match'}, {'description': 'Only return wars with ID smaller than this', 'format': 'int32', 'in': 'query', 'name': 'max_war_id', 'required': False, 'type': 'integer'}], 'responses': {'200': {'description': 'A list of war IDs, in descending order by war_id', 'examples': {'application/json': [3, 2, 1]}, 'headers': {'Cache-Control': {'description': 'The caching mechanism used', 'type': 'string'}, 'ETag': {'description': 'RFC7232 compliant entity tag', 'type': 'string'}, 'Expires': {'description': 'RFC7231 formatted datetime string', 'type': 'string'}, 'Last-Modified': {'description': 'RFC7231 formatted datetime string', 'type': 'string'}}, 'schema': {'description': '200 ok array', 'items': {'description': '200 ok integer', 'format': 'int32', 'title': 'get_wars_200_ok', 'type': 'integer'}, 'maxItems': 2000, 'title': 'get_wars_ok', 'type': 'array'}}, '304': {'description': 'Not modified', 'headers': {'Cache-Control': {'description': 'The caching mechanism used', 'type': 'string'}, 'ETag': {'description': 'RFC7232 compliant entity tag', 'type': 'string'}, 'Expires': {'description': 'RFC7231 formatted datetime string', 'type': 'string'}, 'Last-Modified': {'description': 'RFC7231 formatted datetime string', 'type': 'string'}}}, '400': {'description': 'Bad request', 'examples': {'application/json': {'error': 'Bad request message'}}, 'schema': {'$ref': '#/definitions/bad_request'}}, '420': {'description': 'Error limited', 'examples': {'application/json': {'error': 'Error limited message'}}, 'schema': {'$ref': '#/definitions/error_limited'}}, '500': {'description': 'Internal server error', 'examples': {'application/json': {'error': 'Internal server error message'}}, 'schema': {'$ref': '#/definitions/internal_server_error'}}, '503': {'description': 'Service unavailable', 'examples': {'application/json': {'error': 'Service unavailable message'}}, 'schema': {'$ref': '#/definitions/service_unavailable'}}, '504': {'description': 'Gateway timeout', 'examples': {'application/json': {'error': 'Gateway timeout message'}}, 'schema': {'$ref': '#/definitions/gateway_timeout'}}}, 'summary': 'List wars', 'tags': ['Wars'], 'x-alternate-versions': ['dev', 'legacy', 'v1'], 'x-cached-seconds': 3600}}}
        function = ESI_to_py._create_functions(ESI_parameters=ESI_parameters,
                                               ESI_paths=ESI_paths,
                                               data_source='tranquility',
                                               version='latest')
        expected = '''def get_wars(*, max_war_id, if_none_match=None):
    """
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :param max_war_id: Only return wars with ID smaller than this
    Return a list of wars
    ---
    Alternate route: `/dev/wars/`
    Alternate route: `/legacy/wars/`
    Alternate route: `/v1/wars/`
    ---
    This route is cached for up to 3600 seconds
    """
    ESI_request.request(if_none_match=if_none_match, max_war_id=max_war_id, data_source='tranquility', version='latest', path=f'/wars/')\n\n\n'''
        self.assertEqual(expected, function)

    def test_request_json(self):
        ESI = ESI_to_py._request_json(version='latest')
        self.assertNotEqual({}, ESI)


class Test_ESI_request(unittest.TestCase):
    def test_args_to_params(self):
        expected_params = (('agr1', 1), ('agr2', 2))
        returned_params = ESI_request._args_to_params({'agr1': 1, 'agr2': 2})
        self.assertEqual(expected_params, returned_params)

    def test_request_no_parameter(self):
        response = ESI_request.request(data_source='tranquility',
                                       version='latest', path='')
        self.assertEqual(response, {'error': 'Not found'})

    def test_request_one_parameter(self):
        response = ESI_request.request(alliance_id='1',
                                       data_source='tranquility',
                                       version='latest', path='')
        self.assertEqual(response, {'error': 'Not found'})

    def test_simple_ESI_request(self):
        response = ESI_request.request(if_none_match=None,
                                       data_source='singularity',
                                       version='latest',
                                       path=f'/alliances/')
        self.assertIsInstance(response, type([]))
        self.assertNotEqual(response, [])


if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)
