
#!/usr/bin/python3
# p02.py
import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)


ethernet  = b'\x08\x00\x27\x2e\xc5\x60' # MAC Address Destination
ethernet += b'\x08\x00\x27\x50\x76\x69' # MAC Address Source
ethernet += b'\x08\x00'                 # Protocol-Type: IPv4

ip_header  = b'\x45\x00\x00\x28'  # Version, IHL, Type of Service | Total Length
ip_header += b'\xab\xcd\x00\x00'  # Identification | Flags, Fragment Offset
ip_header += b'\x40\x06\xa6\xec'  # TTL, Protocol | Header Checksum
ip_header += struct.pack(">BBBB", 66, 76, 173, 67) # First and Last intials, B L I C
ip_header += struct.pack(">BBBB",  192, 168, 172, 5)

tcp_header  = b'\x23\x28\x23\x28' # Source Port 9000 | Destination Port 9000
tcp_header += b'\x00\x00\x00\x00' # Sequence Number
tcp_header += b'\x00\x00\x00\x00' # Acknowledgement Number
tcp_header += b'\x50\x02\x71\x10' # Data Offset, Reserved, Flags | Window Size
tcp_header += b'\xe6\x32\x00\x00' # Checksum | Urgent Pointer

packet = ip_header + tcp_header
addr = ("192.168.172.5", 0)
s.sendto(packet, addr)
