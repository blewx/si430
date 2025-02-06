#!/usr/bin/python3
# raw.py

from socket import *
ETH_P_ALL = 0x0003
raw_socket = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL))

(data, addr) = raw_socket.recvfrom(1024)

print("addr=", addr)
print(" ".join([f"{data[i]:02x}" for i in range(16)]))
print("data=", data)