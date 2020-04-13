from urllib import request
import json


get_url = 'https://www.cbr-xml-daily.ru/daily_json.js'


def get_rate(url: str) -> float:
    resp = dict(json.loads(request.urlopen(url).read()))
    return float(resp['Valute']['USD']['Value'])


if __name__ == "__main__":
    print(get_rate(get_url))
