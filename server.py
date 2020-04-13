from http import server
from urllib.parse import urlparse, parse_qs
import handler


class SimpleHTTPRequestHandler(server.BaseHTTPRequestHandler):

    def do_GET(self):
        parse = parse_qs(urlparse(self.path).query)
        if self.path.startswith('/?'):
            args = parse
            valute = args.get('valute')[0]
            value = float(args.get('value')[0])
            resp = handler.get_rate(valute, value)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(resp.encode())


def run(server_class=server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('127.0.0.1', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()
