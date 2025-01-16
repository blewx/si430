#!/usr/bin/python3
# serv_tcp.py

import socket
import sys
import select

sock = socket.socket()
sock.bind(("0.0.0.0",8000))
sock.listen()
(newsock, addr) = sock.accept()
print("connection from", addr)

while True:
  socklist = [newsock, sys.stdin]  ## focus here!!!
  (r_sockets, w_sockets, e_sockets) = select.select(socklist, [], [])

  if e_sockets:     ## an error took place --> stop the loop
    break

  if newsock in r_sockets:   # we have something to read from new sock!
    data = newsock.recv(1024)
    data = data.decode()[:-1]
    if not data:  # no data means the connection has been closed.
      break
    print(data)

  if sys.stdin in r_sockets:  # we have something to read from sys.stdin!
    s = sys.stdin.readline()  # we need to use the low-level function readline()
    newsock.send(s.encode())


newsock.close()
sock.close()
