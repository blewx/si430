#!bin/usr/python3
from socket import *

def showpkts_UDP():


    packet_type = [8,0] #udp
    desired_port = 9000


    while 1 == 1:
        ETH_P_ALL = 0x0003
        raw_socket = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL))

        (data, addr) = raw_socket.recvfrom(1024)

        #data [15] is the first byte of the ip header
        #17/18 is total length
        total_length = data[17] + data[16] *16


        #print(data[17], " ", f"{data[18]:02x}")
        Dest_mac = data[0:6]
        Source_mac = data[6:12]
        Source_addr = data[26:30]
        Dest_addr = data[30:34]
        Dest_ip = str(Dest_addr[0]) + "." + str(Dest_addr[1]) + "." + str(Dest_addr[2]) + "." + str(Dest_addr[3])
        Source_ip = str(Source_addr[0]) + "." + str(Source_addr[1]) + "." + str(Source_addr[2]) + "." + str(Source_addr[3])
        Source_port = data[36]*256 + data[37]
        Dest_port = data[34]*256 + data[35]

        #check to see if it's not an ip packet
        if data[12] != packet_type[0] or data[13] != packet_type[1]:
            continue

        print("src:  ", Source_ip, "(", Source_port, ") [", end="")
        for i in range(0,6):
            print(f"{Source_mac[i]:02x}",end="")
            if i < 5:
                print("",end=":")
            else:
                print("]")

        print("dst:  ", Dest_ip, "(", Dest_port, ") [", end ="")
        for i in range(0,6):
            print(f"{Dest_mac[i]:02x}",end="")
            if i < 5:
                print("",end=":")
            else:
                print("]"


        to_print = ""
        for k in range(20+14+8,total_length+14):
            to_print += chr(data[k])
        print("",end="   ")
        print(to_print.encode())

howpkts_UDP()
