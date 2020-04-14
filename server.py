from http import server
import handler


class SimpleHTTPRequestHandler(server.BaseHTTPRequestHandler):

    def do_GET(self) -> None:
        if self.path.startswith('/rest/convert?'):
            try:
                resp = handler.data_handler(self.path)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(resp.encode())
            except (KeyError, ValueError) as err:
                self.send_response(400)
                self.send_error(400, f"Wrong argument {err}")

        else:
            self.send_response(400)
            self.send_error(400, 'For converting use /rest/convert?value=')


def run(address, port, server_class=server.HTTPServer, handler_class=SimpleHTTPRequestHandler) -> None:
    server_address = (address, port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
