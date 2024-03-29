from json import loads
from os.path import join

from requests import get
from yapf.yapflib.yapf_api import FormatCode


def _identifier(name):
    """
    :param name: string
    :return: name in lower case and with '_' instead of '-'
    :rtype: string
    """
    if name.isidentifier():
        return name
    return name.lower().lstrip('0123456789. ').replace('-', '_')


def _convert_parameters(ESI_parameters):
    """
    Add converted parameters to ESI_parameters
    :param ESI_parameters:
    """
    addition = {}
    for parameter, value in ESI_parameters.items():
        pythonic_name = _identifier(parameter)
        if pythonic_name != parameter:
            addition[pythonic_name] = value
    ESI_parameters.update(addition)


def _get_parameters_with_description(function_dict, parameters):
    """
    :param function_dict:
    :return: full_description
    :rtype: string
    """
    full_description = ''
    for parameter in function_dict['parameters']:
        description = ':param '
        if '$ref' in parameter:
            parameter_name = parameter['$ref'].replace('#/parameters/', '')
            parameter_name = _identifier(parameter_name)
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
    :return: content formatted according to PEP8
    :rtype: string
    """
    content, _ = FormatCode(content, style_config='pep8')
    return content


def _write_to_file(content, ESI_swagger_version, file):
    """
    :param content: file content
    :param ESI_swagger_version: EVE Swagger Interface version
    :param file: string of name and path
    """
    head = ('# Python EVE Swagger Interface\n'
            '# https://github.com/nicoscha/PESI\n'
            f'# ESI version {ESI_swagger_version}\n'
            'import ESI_request\n')
    content = _format_code(head + content)
    with open(file, 'w') as file:
        file.write(content)


def _create_doc_string(ESI_parameters, function_dict):
    """
    Create a docstring for the function
    :param ESI_parameters:
    :param function_dict:
    :return: docstring
    :rtype: string
    """
    parameter_description = _get_parameters_with_description(function_dict,
                                                             ESI_parameters)
    default_description = function_dict['description'].replace('\n\n', '\n')
    default_description = default_description.replace('\n', '\n    ')
    doc_string = (f'\n    """\n    {parameter_description}'
                  f'{default_description}\n    """\n')
    return doc_string


def _filter_parameter(parameter, as_key_word=False):
    if 'datasource' == parameter:  # data source will be specified in module
        return ''
    parameter = _identifier(parameter)

    if as_key_word:
        return parameter + '=' + parameter
    else:
        if 'if_none_match' == parameter:
            parameter = 'if_none_match=None'
        elif 'accept_language' == parameter:
            parameter = "accept_language='en-us'"
        elif 'page' == parameter:
            parameter = "page='1'"
        return parameter


def _shuffle_kwargs_to_the_end(parameters):
    shuffled_kwargs = []
    shuffled_args = []
    for parameter in parameters:
        if '=' in parameter:
            shuffled_kwargs.append(parameter)
        elif parameter != '':
            shuffled_args.append(parameter)
    return shuffled_args + shuffled_kwargs


def _join_parameters(parameters):
    """
    Takes list of parameter and returns a string with ', ' between parameters
    :param parameters: list
    :return: parameters concatenated by a semicolon
    :rtype: string
    """
    parameter_string = ''
    for p in parameters:
        if p != '':
            parameter_string += ', ' + p
    parameter_string = parameter_string[2:]  # Remove the first ', '
    return parameter_string


def _create_functions(ESI_parameters, ESI_paths, data_source, version):
    content = ''
    for raw_function_name, path_dict in ESI_paths.items():
        for function, function_dict in path_dict.items():
            def_parameters_list, parameters = [], []
            for parameter in function_dict['parameters']:
                if '$ref' in parameter:
                    parameter = parameter['$ref'].replace('#/parameters/', '')
                    def_parameters_list.append(_filter_parameter(parameter))
                    parameters.append(_filter_parameter(parameter,
                                                        as_key_word=True))
                elif 'name' in parameter:
                    def_parameters_list.append(
                        _filter_parameter(parameter['name']))
                    parameters.append(_filter_parameter(parameter['name'],
                                                        as_key_word=True))

            def_parameters = _join_parameters(_shuffle_kwargs_to_the_end(
                def_parameters_list))
            parameters = _join_parameters(parameters)
            function_name = function_dict['operationId']

            definition = f'def {function_name}(*, {def_parameters}):'
            doc_string = _create_doc_string(ESI_parameters, function_dict)
            code = (f"    ESI_request.request({parameters}, "
                    f"data_source='{data_source}', "
                    f"version='{version}', "
                    f"HTTP_method='{function.upper()}', "
                    f"path=f'{raw_function_name}')\n\n\n")
            content += definition + doc_string + code
    return content


def _request_json(version):
    """
    Requests and processes ESI json file
    :param version: ESI version ['dev', 'latest', 'legacy', 'v1', 'v2', ...]
    :return: json.load(requests.get().text)
    :rtype: dict
    """
    headers = {'accept': 'application/json', }
    url = f'https://esi.evetech.net/{version}/swagger.json'
    return loads(get(url, headers=headers).text)


def _get_ESI_versions():
    """
    :return: List of versions available on the server
    :rtype: list
    """
    headers = {'accept': 'application/json'}
    params = ()
    response = get(f'https://esi.evetech.net/versions/', headers=headers,
                   params=params)
    versions = loads(response.text)
    return versions if isinstance(versions, list) else []


def run(path):  # pragma: no cover
    data_sources = ['tranquility', 'singularity']
    versions = _get_ESI_versions()
    for data_source, version in [(d,v) for d in data_sources for v in versions]:
        ESI = _request_json(version)
        _convert_parameters(ESI['parameters'])
        content = _create_functions(ESI_parameters=ESI['parameters'],
                                    ESI_paths=ESI['paths'],
                                    data_source=data_source,
                                    version=version)
        ESI_swagger_version = ESI['info']['version']
        _write_to_file(content, ESI_swagger_version=ESI_swagger_version,
                       file=join(path, f'ESI_{data_source}_{version}.py'))
