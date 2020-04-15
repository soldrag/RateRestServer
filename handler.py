from urllib import request
from urllib.parse import urlparse, parse_qs
import json
from typing import Tuple


SOURCE_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


def request_args_parser(request_path: str) -> Tuple[str, float]:
    """
    Parse arguments from url path, default currency - USD
    :param request_path: url_path
    :return: tuple from parsed currency and requested value
    """
    default_currency = 'USD'
    args = parse_qs(urlparse(request_path).query)
    currency = default_currency if args.get('currency') is None else args.get('currency')[0]
    request_value = args.get('value')[0]
    if not currency.isascii() or not request_value.isascii():
        raise ValueError('Not ASCII symbols in arguments')
    return currency, float(request_value)


def get_currency_rate(currency: str, url: str) -> float:
    """
    Get json from source and return selected currency rate
    :param currency: str
    :param url: source url
    :return: currency rate
    """
    currency_rate = json.loads(request.urlopen(url).read())
    currency_rate = currency_rate['Valute'][currency]['Value']
    if not isinstance(currency_rate, float):
        float(currency_rate)
    return currency_rate


def json_compiler(currency: str, currency_rate: float, request_value: float, converted_value: float) -> str:
    """
    Compile json for response
    :param currency: current currency
    :param currency_rate: rate for current currency
    :param request_value: value for converting
    :param converted_value: converted value
    :return: json with converted value and other
    """
    if currency_rate < 0 or request_value < 0 or converted_value < 0:
        raise ValueError('Values must be positive')
    data = {
        'currency': currency,
        'rate': currency_rate,
        'request_value': request_value,
        'converted_value': converted_value
    }
    return json.dumps(data)


def data_handler(request_path: str) -> str:
    """
    Just call all handlers and return json response
    :param request_path: url path from request
    :return: json object
    """
    currency, request_value = request_args_parser(request_path)
    currency_rate = get_currency_rate(currency, SOURCE_URL)
    converted_value = round(request_value * currency_rate, 2)
    return json_compiler(currency, currency_rate, request_value, converted_value)
