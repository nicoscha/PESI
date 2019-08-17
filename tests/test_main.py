import unittest

import ESI_to_py
import ESI_request


class Test_ESIReader(unittest.TestCase):
    def test_join_parameters(self):
        test_parameter = ['abc', 'def', 'ghj']
        returned = ESI_to_py._join_parameters(test_parameter)
        expected = 'abc, def, ghj'
        self.assertEqual(expected, returned)

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

    def test_get_parameters_with_description(self):
        function_dict = {'parameters': [{'$ref': '#/parameters/datasource'},
                                        {'$ref': '#/parameters/language',
                                         'enum':['de', 'en-us', 'fr',
                                                 'ja', 'ru', 'zh']},
                                        {'description': 'ID for a war',
                                         'format': 'int32', 'in': 'path',
                                         'minimum': 1, 'name': 'war_id',
                                         'required': True, 'type': 'integer'}]}
        parameters = {'datasource': {'default': 'tranquility',
                                     'description': 'The server name you would like data from',
                                     'enum': ['tranquility', 'singularity'],
                                     'in': 'query', 'name': 'datasource',
                                     'type': 'string'},
                      'language': {'default': 'en-us',
                                   'description': 'Language to use in the response, takes precedence over Accept-Language',
                                   'enum': ['de', 'en-us', 'fr',
                                            'ja', 'ru', 'zh'],
                                   'in': 'query', 'name': 'language', 'type': 'string'},}

        full_description = ESI_to_py._get_parameters_with_description(
                               function_dict=function_dict,
                               parameters=parameters)
        expected_description = (''':param language: ['de', 'en-us', 'fr', '''
                                ''''ja', 'ru', 'zh'] Language to use in the '''
                                'response, takes precedence over '
                                'Accept-Language\n'
                                '    :param war_id: ID for a war\n    ')
        self.assertEqual(expected_description, full_description)

    def test_format_code(self):
        """Minimal test. For further tests see package tests"""
        test_code = 'x=1'
        expected_code = 'x = 1\n'
        returned_code = ESI_to_py._format_code(test_code)
        self.assertEqual(expected_code, returned_code)

    def test_write_to_file(self):
        pass # TODO Test file creation and content

    def test_create_doc_string(self):
        ESI_parameters = {'datasource': {'default': 'tranquility',
                                         'description': 'The server name you would like data from',
                                         'enum': ['tranquility', 'singularity'],
                                         'in': 'query', 'name': 'datasource',
                                         'type': 'string'},
                          'page': {'default': 1,
                                   'description': 'Which page of results to return',
                                   'format': 'int32', 'in': 'query',
                                   'minimum': 1, 'name': 'page',
                                   'type': 'integer'},
                          'if_none_match': {'description': 'ETag from a previous request. A 304 will be returned if this matches the current ETag',
                                            'in': 'header',
                                            'name': 'If-None-Match',
                                            'type': 'string'}}
        function_dict = {'description': 'Return a list of kills related to a war\n\n---\nAlternate route: `/dev/wars/{war_id}/killmails/`\n\nAlternate route: `/legacy/wars/{war_id}/killmails/`\n\nAlternate route: `/v1/wars/{war_id}/killmails/`\n\n---\nThis route is cached for up to 3600 seconds',
                         'operationId': 'get_wars_war_id_killmails',
                         'parameters': [{'$ref': '#/parameters/datasource'},
                                        {'$ref': '#/parameters/If-None-Match'},
                                        {'$ref': '#/parameters/page'},
                                        {'description': 'A valid war ID',
                                         'format': 'int32', 'in': 'path',
                                         'minimum': 1, 'name': 'war_id',
                                         'required': True, 'type': 'integer'}]}
        expected_doc_string = (
            '\n    """\n'
            '    :param if_none_match: ETag from a previous request. '
            'A 304 will be returned if this matches the current ETag\n'
            '    :param page: Which page of results to return\n'
            '    :param war_id: A valid war ID\n'
            '    Return a list of kills related to a war\n'
            '    ---\n'
            '    Alternate route: `/dev/wars/{war_id}/killmails/`\n'
            '    Alternate route: `/legacy/wars/{war_id}/killmails/`\n'
            '    Alternate route: `/v1/wars/{war_id}/killmails/`\n'
            '    ---\n'
            '    This route is cached for up to 3600 seconds\n'
            '    """\n')
        doc_string = ESI_to_py._create_doc_string(ESI_parameters=ESI_parameters,
                                                  function_dict=function_dict)
        self.assertEqual(expected_doc_string, doc_string)

    def test_filter_parameter_no_keyword(self):
        expected = 'one'
        returned = ESI_to_py._filter_parameter('one')
        self.assertEqual(expected, returned)

    def test_filter_parameter_unfiltered_as_keyword(self):
        expected = 'one=one'
        returned = ESI_to_py._filter_parameter('one', as_key_word=True)
        self.assertEqual(expected, returned)

    def test_filter_parameter_filtered_not_keyword(self):
        parameters = {'datasource': '',
                      'If-None-Match': 'if_none_match=None',
                      'Accept-Language': "accept_language='en-us'",
                      'page': "page='1'"}
        for parameter, expected in parameters.items():
            returned = ESI_to_py._filter_parameter(parameter)
            self.assertEqual(expected, returned)

    def test_filter_parameter_filtered_as_keyword(self):
        parameters = {'datasource': '',
                      'If-None-Match': 'if_none_match=if_none_match',
                      'Accept-Language': 'accept_language=accept_language',
                      'page': 'page=page'}
        for parameter, expected in parameters.items():
            returned = ESI_to_py._filter_parameter(parameter, as_key_word=True)
            self.assertEqual(expected, returned)

    def test_shuffle_kwargs_to_the_end(self):
        test = ['arg_1', 'kwarg_1=kwarg_1', 'arg_2', 'kwarg_2=kwarg_2', 'arg_3']
        returned = ESI_to_py._shuffle_kwargs_to_the_end(test)
        expected = ['arg_1', 'arg_2', 'arg_3',
                    'kwarg_1=kwarg_1', 'kwarg_2=kwarg_2']
        self.assertEqual(expected, returned)

    def test_create_functions(self):
        ESI_parameters = {'datasource': {'default': 'tranquility',
                                         'description': 'The server name you would like data from',
                                         'enum': ['tranquility', 'singularity'],
                                         'in': 'query', 'name': 'datasource',
                                         'type': 'string'},
                          'if_none_match': {'description': 'ETag from a previous request. A 304 will be returned if this matches the current ETag',
                                            'in': 'header',
                                            'name': 'If-None-Match',
                                            'type': 'string'}}
        ESI_paths = {'/wars/': {'get': {'description': 'Return a list of wars\n\n---\nAlternate route: `/dev/wars/`\n\nAlternate route: `/legacy/wars/`\n\nAlternate route: `/v1/wars/`\n\n---\nThis route is cached for up to 3600 seconds',
                                        'operationId': 'get_wars',
                                        'parameters': [{'$ref': '#/parameters/datasource'},
                                                       {'$ref': '#/parameters/If-None-Match'},
                                                       {'description': 'Only return wars with ID smaller than this',
                                                        'format': 'int32',
                                                        'in': 'query',
                                                        'name': 'max_war_id',
                                                        'required': False,
                                                        'type': 'integer'}]}}}
        function = ESI_to_py._create_functions(ESI_parameters=ESI_parameters,
                                               ESI_paths=ESI_paths,
                                               data_source='tranquility',
                                               version='latest')
        expected = (
            'def get_wars(*, max_war_id, if_none_match=None):\n'
            '    """\n'
            '    :param if_none_match: ETag from a previous request. '
            'A 304 will be returned if this matches the current ETag\n'
            '    :param max_war_id: '
            'Only return wars with ID smaller than this\n'
            '    Return a list of wars\n'
            '    ---\n'
            '    Alternate route: `/dev/wars/`\n'
            '    Alternate route: `/legacy/wars/`\n'
            '    Alternate route: `/v1/wars/`\n'
            '    ---\n'
            '    This route is cached for up to 3600 seconds\n'
            '    """\n'
            '    ESI_request.request(if_none_match=if_none_match, '
            "max_war_id=max_war_id, data_source='tranquility', "
            "version='latest', path=f'/wars/')\n\n\n")
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
