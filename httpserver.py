from http.server import HTTPServer,BaseHTTPRequestHandler
import time

HOST = "192.168.104.119"
PORT = 8000


class MyHTTP(BaseHTTPRequestHandler):
    #GET request
    def do_GET(self):
        self.send_response(200)
        self.send_header("Context-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h4>Hello All!! This is a test website created using python</h4></body></html>","utf-8"))
    #POST request
    def do_POST(self):
        self.send_response(200)
        self.send_header("Context-type", "application/json")
        self.end_headers()
        date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}',"utf-8"))

server = HTTPServer((HOST,PORT),MyHTTP)
print("Server is running....")

server.serve_forever()
server.server_close()
print("Server Stopped..")