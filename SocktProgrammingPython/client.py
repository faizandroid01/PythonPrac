import socket

c = socket.socket()

c.connect(('localhost', 9999))

clientName = input("Enter your name")

c.send(bytes(clientName, 'utf-8'))
