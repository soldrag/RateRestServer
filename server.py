from http import server
from urllib.parse import urlparse, parse_qs
import handler


class SimpleHTTPRequestHandler(server.BaseHTTPRequestHandler):

    def do_GET(self):
        parse = parse_qs(urlparse(self.path).query)
        if self.path.startswith('/rest/convert?'):
            try:
                args = parse
                currency = 'USD' if args.get('currency') is None else args.get('currency')[0]
                value = float(args['value'][0])
                resp = handler.get_rate(currency, value)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(resp.encode())
            except KeyError as err:
                self.send_response(400)
                self.send_error(400, f"Wrong argument {err}")
            except ValueError as err:
                self.send_response(400)
                self.send_error(400, f"Wrong argument {err}")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Nothing')


def run(address='127.0.0.1', port=8000, server_class=server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = (address, port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
