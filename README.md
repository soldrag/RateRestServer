# RateRestServer
Test task
It is simply rest webserver converting currency -> rub.
For start server run main.py
main.py have 3 optional named arguments
-a: server address (default 127.0.0.1)
-p: server port (default 8000)
-l: logging level (default info level)
  1: debug level
  2: info level
  3: error level

For converting use GET request with pattern: server_address:port/rest/convert?value=value&currency=currency
  value: float value for converting (70.5)
  currency: optional argument (default USD), you can select currency for converting (USD, EUR, AUD..)
  