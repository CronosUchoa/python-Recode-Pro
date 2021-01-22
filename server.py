import http.server
import socketserver
import os


PORT = 8000
os.chdir("static")

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)


try:
    print("Start serving at port %i" % PORT)
    httpd.serve_forever()

except KeyboardInterrupt:    
    pass
    httpd.server_close()
    exit()

