from http import server
import socketserver

class myHandler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8000

handler = myHandler

myserver = socketserver.TCPServer(("", PORT), handler)
print(f"Starting Server on Port:{PORT}")
myserver.serve_forever()