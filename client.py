import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.86.127', 8000))
msg = 'Hello There, I\'m Python\n'
s.sendall(msg.encode())
data = s.recv(1024)
s.close()
print('Received:\n', data.decode())
