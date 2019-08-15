from requests import get
from os.path import split, join
from json import loads
from yapf.yapflib.yapf_api import FormatCode


def _pythonic_name(name):
    """
    :param name: string
    :return: string in lower case with '_' instead of '-'
    """
    return name.lower().replace('-', '_')


def _convert_parameters(ESI_parameters):
    """
    Add converted parameters to ESI_parameters
    :param ESI_parameters:
    """
    addition = {}
    for parameter, value in ESI_parameters.items():
        pythonic_name = _pythonic_name(parameter)
        if pythonic_name != parameter:
            addition[pythonic_name] = value
    ESI_parameters.update(addition)


def _get_parameters_with_description(function_dict, parameters):
    """
    :param function_dict:
    :return: full_description: string
    """
    full_description = ''
    for parameter in function_dict['parameters']:
        description = ':param '
        if '$ref' in parameter:
            parameter_name = parameter['$ref'].replace('#/parameters/', '')
            parameter_name = _pythonic_name(parameter_name)
            if parameter_name == 'datasource':
                continue  # This parameter is not a function parameter
            description += parameter_name + ': '
            parameter_dict = parameters[parameter_name]
            if 'enum' in parameter_dict:  # self.parameter[parameter_name]:
                description += str(parameter_dict["enum"]) + ' '
            description += parameter_dict['description']
        if 'description' in parameter:
            name = parameter['name']
            description += name + ': '
            if 'enum' in parameter:
                description += str(parameter["enum"]) + ' '
            description += parameter['description'].replace('\n\n', '\n')
        full_description += description + '\n    '
    return full_description


def _format_code(content):
    """
    Takes a string outputs a PEP8 version of it
    :param content: string
    :return: content: string
    """
    content, _ = FormatCode(content, style_config='pep8')
    return content


def _write_to_file(content, file_name):
    """
    :param content: file content
    :param file_name: string of name and path
    """
    head = 'import ESI_request\n'
    content = _format_code(head + content)
    with open(file_name, 'w') as file:
        file.write(content)


def _create_doc_string(ESI_parameters, function_dict):
    """
    Create a docstring for the function
    :param ESI_parameters:
    :param function_dict:
    :return: doc_string: string
    """
    description = function_dict['description']
    parameter_description = _get_parameters_with_description(function_dict,
                                                             ESI_parameters)
    default_description = description.replace('\n\n', '\n').replace('\n', '\n    ')
    doc_string = (f'\n    """\n    {parameter_description}{default_description}\n    """\n')
    return doc_string


def _filter_parameter(parameter, as_key_word=False):
    if 'datasource' == parameter:  # data source will be specified in module
        return ''
    elif 'If-None-Match' == parameter:  # Ajust name
        parameter = 'if_none_match'
    elif 'Accept-Language' == parameter:
        parameter = 'accept_language'
    if as_key_word:
        return ', ' + parameter + '=' + parameter
    else:
        return ', ' + parameter


def _create_functions(ESI_parameters, ESI_paths, data_source, version):
    content = ''
    for raw_function_name, path_dict in ESI_paths.items():
        for function, function_dict in path_dict.items():
            def_parameters, parameters = '', ''
            for parameter in function_dict['parameters']:
                if '$ref' in parameter:
                    parameter = parameter['$ref'].replace('#/parameters/', '')
                    def_parameters += _filter_parameter(parameter)
                    parameters += _filter_parameter(parameter,
                                                    as_key_word=True)
                elif 'name' in parameter:
                    def_parameters += _filter_parameter(parameter['name'])
                    parameters += _filter_parameter(parameter['name'],
                                                    as_key_word=True)
            def_parameters = def_parameters.replace(', ', '', 1)
            parameters = parameters.replace(', ', '', 1)
            function_name = function_dict['operationId']

            definition = f'def {function_name}({def_parameters}):'
            doc_string = _create_doc_string(ESI_parameters, function_dict)
            code = f"    ESI_request.request({parameters}, data_source='{data_source}', version='{version}', path=f'{raw_function_name}')\n\n\n"
            content += definition + doc_string + code
    return content


def _request_json(version):
    """
    Requests and processes ESI json file
    :param version: ESI version ['_dev', '_latest', '_legacy', 'dev', 'latest', 'legacy', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6']
    :return: python dict, json.load(requests.get().text)
    """
    headers = {'accept': 'application/json', }
    url = f'https://esi.evetech.net/{version}/swagger.json'
    return loads(get(url, headers=headers).text)


def run(path): # pragma: no cover
    data_sources = ['tranquility', 'singularity']
    versions = ['_dev', '_latest', '_legacy', 'dev', 'latest', 'legacy',
                'v1', 'v2', 'v3', 'v4', 'v5', 'v6']
    for data_source, version in [(d,v) for d in data_sources for v in versions]:
        ESI = _request_json(version)
        _convert_parameters(ESI['parameters'])
        content = _create_functions(ESI_parameters=ESI['parameters'],
                                  ESI_paths=ESI['paths'],
                                  data_source=data_source,
                                  version=version)
        _write_to_file(content, join(path, f'ESI_{data_source}_{version}.py'))
