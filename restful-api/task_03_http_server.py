#!/usr/bin/python3
import http.server
import socketserver

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!\n")


PORT = 8000

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
