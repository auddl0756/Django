#python 표준 라이브러리에 웹 서버와의 연동 기능을 개발할 수 있도록 wsgiref package의 하위 모듈로
#wsgiref.simple_server 모듏을 제공

from wsgiref.simple_server import make_server

#간단한 웹 서버와 마찬가지로 서버의 ip,port,핸들러 클래스를 가지고
# HTTPServer 객체를 만들고 serve_forever()를 호출합니다

# make_server : Create a new WSGI server listening on host and port for app

def my_app(environ,start_response):
    status ='200 OK'
    headers= [('Content-Type','text/plain')]
    start_response(status,headers)

    response =[b"this is a sample WSGI Application"]

    return response

if __name__ =='__main__':
    print("statted WSGI server on port 8888")
    server = make_server('',8888,my_app)
    server.serve_forever()