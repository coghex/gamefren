import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8000))
s.listen(1)
(conn, addr) = s.accept()
print ('Connected by ', addr)
while 1:
  data = conn.recv(1024)
  if not data: break
  print(data.decode())
  msg = "Well Hello to You Too."
  conn.sendall(msg.encode())
conn.close()
