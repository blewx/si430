#!/usr/bin/python3
# p02.py
import socket
import struct
import random

def calc_checksum(d):
    total = 0

    for i in range(0, len(d), 2):
        total += d[i] * 256 + d[i + 1]

    while total > 0xffff:
        total = (total >> 16) + (total & 0xffff)

    return total ^ 0xffff

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
#IP header 
ip_header  = b'\x45\x00\x00\x28'  # Version, IHL, Type of Service | Total Length
ip_header += b'\xab\xcd\x00\x00'  # Identification | Flags, Fragment Offset
ip_header += b'\x40\x06\xa6\xec'  # TTL, Protocol | Header Checksum
ip_header += struct.pack(">BBBB", 192, 168, 172, 4)  # Src IP
ip_header += struct.pack(">BBBB", 192, 168, 172, 5)  # Destination IP (192.168.172.5)

#tcp header
tcp_header = (random.randint(1000,9999)).to_bytes(2, 'big')
tcp_header += (9000).to_bytes(2, 'big')
tcp_header += struct.pack(">HH",  random.randint(1000, 9999), 9000)# Source Port | Destination Port
tcp_header += struct.pack(">L",  random.randint(1000, 9999)) # Sequence Number
tcp_header += b'\x50\x02\x71\x10' # Data Offset, Reserved, Flags | Window Size
srcip = struct.pack(">BBBB", 192, 168, 172, 4)  # Src IP
dstip =struct.pack(">BBBB", 192, 168, 172, 5)  # Dst IP
chksum = calc_checksum(srcip + dstip + struct.pack(">BBH", 0, 6, 20) + tcp_header)
tcp_header += struct.pack(">H", chksum) #calculate checksum based off first 16

#bytes of header
tcp_header += b'\x00\x00'# | Urgent Pointer

#update the checksum
packet = ip_header + tcp_header
addr = ("192.168.172.5", 0)  # Destination IP
s.sendto(packet, addr)
