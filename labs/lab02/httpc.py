#!/usr/bin/python3
# httpc.py

import socket
import sys
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print(socket.gethostbyname(sys.argv[1]))

sock.connect((socket.gethostbyname(sys.argv[1]), 80))
to_send = f'GET / HTTP/1.1\r\nhost: {sys.argv[1]}\r\n\r\n'
sock.sendall(to_send.encode())
data = sock.recv(4096)
print(data.decode())
