import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8000))
s.listen(1)
conn, addr = s.accept()
print 'Connected by ', addr
while 1:
  data = conn.recv(1024)
  if not data: break
  print repr(data)
  conn.sendall("Well Hello to You Too.")
conn.close()
