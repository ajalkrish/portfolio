
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class PortfolioHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        return super().do_GET()

server = HTTPServer(("127.0.0.1", 8000), PortfolioHandler)

print("Portfolio website: http://127.0.0.1:8000/")
server.serve_forever()