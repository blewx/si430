#!/usr/bin/python3
# serv_tcp.py

# Import libraries
from socket import *
import sys
import select

PORT = 9000
ADDR = "127.0.0.1"
newaddr = ''

# Open and bind socket
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((ADDR,PORT))

while True:
    
    # Get socket list
    socklist = [sock, sys.stdin]
    (r_sockets, w_sockets, e_sockets) = select.select(socklist, [], [])
    
    # Error
    if e_sockets:
        break;

    # Receive Data
    if sock in r_sockets:
        data, newaddr = sock.recvfrom(1024)
        data = data.decode()
        if not data:
            break
        print(data)

    # Write Data
    if sys.stdin in r_sockets:
        msg = sys.stdin.readline()
        msg = msg.strip()
        if msg == "quit":
            break
        if newaddr != '':
            sock.sendto(msg.encode(), newaddr)


sock.close()
