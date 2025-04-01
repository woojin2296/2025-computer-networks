import socket

def calculate(expression):
    try:
        expression = expression.replace(' ', '')
        if '+' in expression:
            a, b = map(int, expression.split('+'))
            return str(a + b)
        elif '-' in expression:
            a, b = map(int, expression.split('-'))
            return str(a - b)
        elif '*' in expression:
            a, b = map(int, expression.split('*'))
            return str(a * b)
        elif '/' in expression:
            a, b = map(int, expression.split('/'))
            return f"{a / b:.1f}" 
        else:
            return "잘못된 연산식입니다."
    except:
        return "잘못된 연산식입니다."

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3333))
s.listen(1)

while True:
    client, addr = s.accept()

    while True:
        data = client.recv(1024).decode()
        client.send(calculate(data).encode())

    client.close()