import os
import http.server
import socketserver

from http import HTTPStatus

src='''
function version_of_my_lib() {
  return "Wersja taka owaka...";
}

function test_alg() {
  return Math.sqrt(16);
}

'''

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()        
        self.wfile.write(src.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
