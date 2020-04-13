from urllib import request
import json


get_url = 'https://www.cbr-xml-daily.ru/daily_json.js'


def get_rate(currency, request_value, url=get_url) -> json:
    resp = json.loads(request.urlopen(url).read())['Valute']
    return data_handler(currency, resp[currency]['Value'], request_value)


def data_handler(currency: str, currency_value: float, request_value: float) -> json:
    """
    :param currency: current currency
    :param currency_value: rate for current currency
    :param request_value: value for converting
    :return: json with answer
    """
    data = {
        'currency': currency,
        'rate': currency_value,
        'request_value': request_value,
        'result_value': round(request_value * currency_value, 2)
    }
    return json.dumps(data)


if __name__ == "__main__":
    print(get_rate('USD', 100))
