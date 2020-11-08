import socket

sock = socket.socket()
sock.connect(('localhost', 2404))
sock.send(str.encode('hello, world!'))

data = sock.recv(1024)
sock.close()

print(data)
