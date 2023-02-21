import os
import http.server
import socketserver

from http import HTTPStatus

def get_file(path):
  
  data =  "// javascript content at path: "+path
  data += "/////////////////////////////////////////////////"
  
  try:
    with open(path, "r") as f_in:      
      data += f_in.read()
      
  except IOError as e:
    data ="// no javascript content at: "+path
    
  return data;

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()       
        src = get_file(self.path)
        self.wfile.write(src.encode())


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
