from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3002))
s.listen(1)

client, addr = s.accept()

while True:
    msg = client.recv(1024).decode()
    if msg == 'quit':
        break
    if msg == 'Request':
        heartbeat = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)
        data = f"{heartbeat}:{steps}:{cal}"
        client.send(data.encode())

client.close()