from http.server import BaseHTTPRequestHandler, HTTPServer


class HostHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        host_header = self.headers.get("Host", "undefined")
        self.wfile.write(f"[{host_header}]".encode())


port = 3001
server = HTTPServer(("0.0.0.0", port), HostHandler)
print(f"Python server running on http://0.0.0.0:{port}")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Shutting down the server.")
    server.socket.close()
