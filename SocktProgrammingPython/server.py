import socket

# by default it connects to   ipv4 , Tcp ,, can take (ipv6 , Udp)
s = socket.socket()

s.bind(('localhost', 9999))
print("Server is On")

# start listening
s.listen(3)
print('waiting for connections')

while True:
    c, add = s.accept()

    clientName = c.recv(1024).decode()
    print('Connected to :', add, clientName)
