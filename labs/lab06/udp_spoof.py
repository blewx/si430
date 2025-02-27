
#!/usr/bin/python3
# udp_spoof.py
from socket import *
raw_socket = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)

udp_payload = b"Hello World\n"

import struct
udp_header = struct.pack(">HHHH", 12345, 9000, 8 + len(udp_payload), 0)
ip_payload = udp_header + udp_payload


version = 4
ihl = 5
# version is 4 bits, IHL is 4 bits
# version_ihl is 8 bits (1 byte)
version_ihl = (version << 4) | ihl
type_of_service = 0
total_length = 20 + len(ip_payload)
ip_header = struct.pack(">BBH",
              version_ihl, type_of_service, total_length)

ip_header += struct.pack(">HH", 12345, 0)


ttl = 20
protocol = 17
checksum = 0
ip_header += struct.pack(">BBH", ttl, protocol, checksum)

ip_header += struct.pack(">BBBB", 66, 76, 173, 67) # First and Last intials, B L I C

ip_header += struct.pack(">BBBB", 10, 60, 101, 236)

ip_pkt = ip_header + ip_payload


addr = ("10.60.101.236", 9000)
raw_socket.sendto(ip_pkt, addr)

