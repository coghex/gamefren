import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.86.127', 8000))
inp = "initgamefren\n"
while 1:
    try:
        s.sendall(inp.encode())
        data = s.recv(1024)
        print(data.decode())
        inp = input("inp: ")
    except:
        s.close()
