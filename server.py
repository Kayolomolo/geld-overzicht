import http.server, os, socketserver
os.chdir(os.path.dirname(os.path.abspath(__file__)))
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 3456), http.server.SimpleHTTPRequestHandler) as s:
    s.serve_forever()
