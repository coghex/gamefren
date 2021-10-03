import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('172.23.125.55', 8000))
s.sendall('Hello There, I\'m Python\n')
data = s.recv(1024)
s.close()
print 'Received:\n', repr(data)
