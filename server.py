from http import server


class SimpleHTTPRequestHandler(server.BaseHTTPRequestHandler):

    def get_request(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'some resp')


def run(server_class=server.HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('127.0.0.1', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()
