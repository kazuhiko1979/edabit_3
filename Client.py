import socket

s = socket.socket()
host = 'localhost'
port = 8080

s.connect((host, port))
fileName = 'bilal.txt'
s.send(fileName.encode())
readfile = s.recv(1024)
print(readfile.decode())
s.close()