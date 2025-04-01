import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 3333))

while True:
    expression = input("계산식 입력(종료:q) : ")
    
    sock.send(expression.encode())

    if expression == 'q':
        break

    print("결과:", sock.recv(1024).decode())

sock.close()