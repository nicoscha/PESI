import requests
from json import loads


def _args_to_params(kwargs):
    """
    Creates a tuple of keyword, value tuples and changes parameter names for ESI
    :param kwargs:
    :return:
    """
    params = ()
    for parameter, value in kwargs.items():
        if value is None:
            continue
        if parameter == 'if_none_match':
            parameter = 'If-None-Match'
        if parameter == 'accept_language':
            parameter = 'Accept-Language'
        params = (*params, (parameter, value))
    return params


def request(data_source, version, HTTP_method, path, proxies=None, **kwargs):
    """
    Requests and processes ESI json file
    :param data_source: ['tranquility', 'singularity']
    :param version: ESI version ['dev', 'latest', 'legacy', 'v1', 'v2', ...]
    :param HTTP_method: ['GET', 'POST', 'PUT', 'DELETE', ...]
    :param path: endpoint
    :param proxies: Dictionary mapping protocol to the URL of the proxy
    :param kwargs: parameters for the endpoint
    :return: loads: python dict, json.load(requests.get().text)
    """
    headers = {'accept': 'application/json'}
    params = _args_to_params(kwargs)
    response = requests.request(HTTP_method,
                                f'https://esi.evetech.net/{version}{path}',
                                headers=headers, params=params,
                                proxies=proxies)
    return loads(response.text)
