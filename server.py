import http.server
import socketserver

class Server(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Sample response')

port = 8080
server = socketserver.ThreadingTCPServer(('', port), Server)
print("[*] Server on port {}".format(port))
server.serve_forever()