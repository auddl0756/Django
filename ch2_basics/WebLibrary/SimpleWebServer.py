from http.server import HTTPServer,BaseHTTPRequestHandler

#웹 서버의 역할은 http 통신에서 클라이언트의 요청을 받고 처리해서 돌려주는것
#웹서버를 만드는 규칙
#1. http.server 모듈을 import
#2. BaseHTTPRequestHandler를 상속받아, 원하는 로직으로 핸들러 클래스를 정의
#3. HTTPServer객체 생성(인자 : ip,port,구현한 핸들러 클래스)
#4. HTTPServer객체의 serve_forever() 호출


# HTTPServer : Base class for various socket-based server classes.
# BaseHTTPRequestHandler : HTTP request handler base class.

class MyHandler(BaseHTTPRequestHandler):    #this is hanlder
    def do_GET(self):
        self.send_response(200,'OK')
        self.send_header('Content-Type','text/plain')
        self.end_headers()
        self.wfile.write(b"Hello world!")


if __name__ == '__main__':
    server = HTTPServer(('',8888),MyHandler)
    print("Started WebServer on port 8888")
    print("Press ^C to quit WebServer")
    server.serve_forever()

