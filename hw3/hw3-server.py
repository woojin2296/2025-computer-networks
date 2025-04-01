import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())

    name = client.recv(1024)
    print(name.decode())

    student_number = 20201523
    client.send(student_number.to_bytes(4, byteorder='big'))

    client.close()