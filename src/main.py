#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


class HttpGetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.startswith("/health"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write('{"status": "OK"}'.encode())


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
  server_address = ('', 8000)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()


if __name__ == "__main__":
    run()
