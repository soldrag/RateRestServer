# RateRestServer
## REST web server for converting currency

It is simply rest web server converting currency -> rub.

For start server run main.py, or you can build docker container. 

main.py have 3 optional named arguments
* -a: server address (default 0.0.0.0)
* -p: server port (default 8000)
* -l: logging level 0-2 (default info level)
  * 0: debug level
  * 1: info level
  * 2: error level

For converting use GET request with pattern: server_address:port/rest/convert?value=value&currency=currency
  * value: float value for converting (70.5)
  * currency: optional argument (default USD), you can select currency for converting (USD, EUR, AUD..)
  
 request example 'http://127.0.0.1:8000/rest/convert?value=100&currency=EUR'
 
 Server return json object:
``` 
 {
    'currency': currency,
    'rate': currency_rate,
    'request_value': request_value,
    'converted_value': converted_value
 } 
``` 
