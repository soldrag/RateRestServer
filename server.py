from http import server
import handler
from urllib.error import URLError
from json import JSONDecodeError
import logging


server_logger = logging.getLogger()


class SimpleHTTPRequestHandler(server.BaseHTTPRequestHandler):

    def log_message(self, format: str, *args) -> None:
        pass

    def do_GET(self) -> None:
        server_logger.debug(f'Get request: {self.path}')
        if self.path.startswith('/rest/convert?'):
            try:
                resp = handler.data_handler(self.path)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(resp.encode())
                server_logger.debug(f'Response: 200, {resp}')
            except JSONDecodeError:
                self.send_response(400)
                self.send_error(400, f'Cant parse json object from source: {handler.source_url}')
                server_logger.error(f'Response: 400, Cant parse json object from source: {handler.source_url}')
            except (KeyError, ValueError) as err:
                self.send_response(400)
                self.send_error(400, f'{err}')
                server_logger.error(f'Response: 400, {err}')
            except URLError as err:
                self.send_response(400)
                self.send_error(400, f'Cant access to data source: {err}')
                server_logger.error(f'Response: 400, Cant access to data source: {err}')
        else:
            self.send_response(400)
            self.send_error(400, 'For converting use /rest/convert?value={value}')
            server_logger.debug('Response: 400, For converting use /rest/convert?value={value}')


def run(address, port, server_class=server.HTTPServer, handler_class=SimpleHTTPRequestHandler) -> None:
    server_address = (address, port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
