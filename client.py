from socket import *
import sys


serverName = '127.0.0.1'
serverPort = 12345


def create_socket_and_send(request_message):
    #클라이언트 소켓 생성
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect((serverName, serverPort))
    #서버에 요청메세지 전송
    clientSock.send(request_message.encode('utf-8'))

    #응답 확인
    recieve_message = clientSock.recv(65535)
    print(recieve_message.decode())

    clientSock.close()

#post 요청메세지
Post_request = 'POST /index.html HTTP/1.1\r\n'
Post_request +='Host:127.0.0.1:12345\r\n'
Post_request +='Content-Type: text/plain\r\n'
Post_request +='Content-Length: 2\r\n'
Post_request +='Connection: Keep-Alive\r\n\r\n'
Post_request +=    "\t{\r\n"
Post_request +=        '\tname: jh\r\n'
Post_request +=    '\t}\r\n\r\n'

#post 요청메세지 404에러 유도
Post_request_404 = 'POST /indx.html HTTP/1.1\r\n'
Post_request_404 +='Host:127.0.0.1:12345\r\n'
Post_request_404 +='Content-Type: text/plain\r\n'
Post_request_404 +='Content-Length: 2\r\n'
Post_request_404 +='Connection: Keep-Alive\r\n\r\n'
Post_request_404 +=    "\t{\r\n"
Post_request_404 +=        '\tname: jh\r\n'
Post_request_404 +=    '\t}\r\n\r\n'

#post 요청메세지 400에러 유도
Post_request_400 = 'POST /index.html HTTP/1.1\r\n'
Post_request_400 +='Host:127.0.0.1:12345\r\n'
Post_request_400 +='Content-Type: text/plain\r\n'
Post_request_400 +='Content-Length: 2\r\n'
Post_request_400 +='Connection: Keep-Alive\r\n\r\n'
Post_request_400 +=    "\t{\r\n"
Post_request_400 +=        '\tname: 1234\r\n'
Post_request_400 +=    '\t}\r\n\r\n'

#put 요청메세지
Put_request = 'PUT /index.html HTTP/1.1\r\n'
Put_request +='Host:127.0.0.1:12345\r\n'
Put_request +='Content-Type: text/plain\r\n'
Put_request +='Content-Length: 3\r\n'
Put_request +='Connection: Keep-Alive\r\n\r\n'
Put_request +=    "\t{\r\n"
Put_request +=        '\tname: kia\r\n'
Put_request +=    '\t}\r\n\r\n'



#put 요청메세지 404 에러 유도
Put_request_404 = 'PUT /indx.html HTTP/1.1\r\n'
Put_request_404 +='Host:127.0.0.1:12345\r\n'
Put_request_404 +='Content-Type: text/plain\r\n'
Put_request_404 +='Content-Length: 3\r\n'
Put_request_404 +='Connection: Keep-Alive\r\n\r\n'
Put_request_404 +=    "\t{\r\n"
Put_request_404 +=        '\tname: kia\r\n'
Put_request_404 +=    '\t}\r\n\r\n'

#put 요청메세지 400 에러 유도
Put_request_400 = 'PUT /index.html HTTP/1.1\r\n'
Put_request_400 +='Host:127.0.0.1:12345\r\n'
Put_request_400 +='Content-Type: text/plain\r\n'
Put_request_400 +='Content-Length: 3\r\n'
Put_request_400 +='Connection: Keep-Alive\r\n\r\n'
Put_request_400 +=    "\t{\r\n"
Put_request_400 +=        '\tname: 1234\r\n'
Put_request_400 +=    '\t}\r\n\r\n'

Put_request_505 = 'PUT /index.html HTTP/1.0\r\n'
Put_request_505 +='Host:127.0.0.1:12345\r\n'
Put_request_505 +='Content-Type: text/plain\r\n'
Put_request_505 +='Content-Length: 3\r\n'
Put_request_505 +='Connection: Keep-Alive\r\n\r\n'
Put_request_505 +=    "\t{\r\n"
Put_request_505 +=        '\tname: kia\r\n'
Put_request_505 +=    '\t}\r\n\r\n'



#Head 요청메시지
Head_request = 'HEAD /index.html HTTP/1.1\r\n'
Head_request +='Host:127.0.0.1:12345\r\n'
Head_request +='Connection: Keep-Alive\r\n\r\n'

#Get 요청메세지
Get_request = 'GET /index.html HTTP/1.1\r\n'
Get_request +='Host:127.0.0.1:12345\r\n'
Get_request +='Connection: Keep-Alive\r\n\r\n'

#Get 요청메세지 404
Get_request_404 = 'GET /inex.html HTTP/1.1\r\n'
Get_request_404 +='Host:127.0.0.1:12345\r\n'
Get_request_404 +='Connection: Keep-Alive\r\n\r\n'



create_socket_and_send(Get_request)


