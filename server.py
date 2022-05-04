from socket import *
import datetime
import sys


server_port = 12345

#tcp 서버 생성
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', server_port))

serverSocket.listen()
print('server is running')

def GET_HEAD(request_header):
    now = datetime.datetime.now().strftime("Date: %a, %d %b %Y %H:%M:%S KST")

    # 주소가 잘못된 경우
    if (request_headers[1] != '/index.html'):
        message = 'HTTP/1.1 404 Not Found\r\n'
    else:
        message = 'HTTP/1.1 200 OK\r\n'
    message += now + '\r\n\r\n'
    return message

def POST_PUT(request_message):
    now = datetime.datetime.now().strftime("Date: %a, %d %b %Y %H:%M:%S KST")
    # 주소가 잘못된 경우
    if (request_headers[2] != 'HTTP/1.1'):
        message = 'HTTP/1.1 505 HTTP Version Not Supported\r\n'
        message += now + '\r\n\r\n'
        return message
    if (request_headers[1] != '/index.html'):
        message = 'HTTP/1.1 404 Not Found\r\n'
        message += now + '\r\n\r\n'
        return message
    # post의 name은 숫자가 올 수 없다고 가정.
    # name의 인자로 숫자가 들어온 경우
    try:
        int(request_headers[12])
        message = 'HTTP/1.1 400 Bad Request\r\n'
        message += now+'\r\n\r\n'
        message += request_headers[10] + '\r\n\t'
        message += 'message:' + ' '
        message += 'name must be String' + '\r\n'
        message += request_headers[13] + '\r\n\r\n'
        return message
    # 나머지 경우는 pass
    except ValueError:
        pass
    # 코드에 문제가 없으므로 200 OK 리턴.
    message =  'HTTP/1.1 200 OK\r\n'
    message += request_headers[4] + request_headers[5] + '\r\n'
    message += request_headers[6] + request_headers[7] + '\r\n'
    message += now +'\r\n\r\n'
    message += request_headers[10]+'\r\n\t'
    message += request_headers[11]+' '
    message += request_headers[12]+'\r\n'
    message += request_headers[13]+'\r\n\r\n'
    return message

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        # receive message through socket when it the connection is created
        message = connectionSocket.recv(65535).decode()
        request_headers = message.split()
        print(request_headers)
        if (request_headers[0] in ['GET', 'HEAD']):
            sendingData = GET_HEAD(request_headers)

        elif (request_headers[0] in ['POST','PUT']):
            sendingData = POST_PUT(request_headers)

        #response heder에 시간정보 추가


        #response message 전송
        connectionSocket.send(sendingData.encode('utf-8'))
        connectionSocket.close()

    #파일 입출력을 고려해서 try except 문을 짰지만 구현 실패했습니다.
    except IOError:
        connectionSocket.send('HTTP/1.1 404 Not Found\n'.encode('utf-8'))
        #Close client socket
        connectionSocket.close()
