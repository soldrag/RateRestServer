from urllib import request
import json


get_url = 'https://www.cbr-xml-daily.ru/daily_json.js'


def get_rate(valute, request_value, url=get_url) -> json:
    resp = dict(json.loads(request.urlopen(url).read())['Valute'])
    return data_handler((valute, resp[valute]), request_value)


def data_handler(raw_data: tuple, request_value) -> json:
    currency, resp = raw_data
    data = {
        'valute': currency,
        'rate': resp['Value'],
        'request_value': request_value,
        'result_value': round(request_value * resp['Value'], 2)
    }
    return json.dumps(data)


if __name__ == "__main__":
    print(get_rate('USD', 100))
