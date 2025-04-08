from socket import *
import time

device1 = socket(AF_INET, SOCK_STREAM)
device1.connect(('localhost', 3001))

device2 = socket(AF_INET, SOCK_STREAM)
device2.connect(('localhost', 3002))

with open("data.txt", "w") as file:
    while True:
        choice = input("Enter (1/2/quit) : ")
        print(choice)
        timestamp = time.ctime()
        
        if choice == 'quit':
            device1.send('quit'.encode())
            device2.send('quit'.encode())
            break
        
        if choice == '1':
            device1.send('Request'.encode())
            data = device1.recv(1024).decode()
            temp, humid, illum = data.split(':')
            entry = f"{timestamp}: Device1: Temp={temp}, Humid={humid}, Illum={illum}\n"
            file.write(entry)
            count += 1
            print(entry)

        elif choice == '2':
            device2.send('Request'.encode())
            data = device2.recv(1024).decode()
            heartbeat, steps, cal = data.split(':')
            entry = f"{timestamp}: Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}\n"
            file.write(entry)
            count += 1
            print(entry)

device1.close()
device2.close()