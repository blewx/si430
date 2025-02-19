#!bin/usr/python3
from socket import *
'''
ETH_P_ALL = 0x0003
raw_socket = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL))

(data, addr) = raw_socket.recvfrom(1024)

print("addr=", addr)
print(" ".join([f"{data[i]:02x}" for i in range(16)]))
print("data=", data)
'''

def showpkts_TCP():


    packet_type = [8,0] #udp
    desired_port = 9000


    while 1 == 1:
        print("hi")
        ETH_P_ALL = 0x0003
        raw_socket = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL))

        (data, addr) = raw_socket.recvfrom(1024)

        #data [15] is the first byte of the ip header
        #17/18 is total length
        total_length = data[17] + data[16] *16


        #print(data[17], " ", f"{data[18]:02x}")
        Dest_mac = data[0:6]
        Source_mac = data[6:12]
        Dest_addr = data[26:30]
        Source_addr = data[30:34]
        Dest_ip = str(Dest_addr[0]) + "." + str(Dest_addr[1]) + "." + str(Dest_addr[2]) + "." + str(Dest_addr[3])
        Source_ip = str(Source_addr[0]) + "." + str(Source_addr[1]) + "." + str(Source_addr[2]) + "." + str(Source_addr[3])

        #check to see if it's not an ip packet
        #print(f"{data[12]:02x}", " ", f"{data[13]:02x}")
        #print(data[12], " ", f"{data[13]:02x}")
        if data[12] != packet_type[0] or data[13] != packet_type[1]:
            continue

        print("src:  ", Source_ip, "(port) [", end="")
        for i in range(0,6):
            print(Source_mac[i],end="")
            if i < 5:
                print("",end=":")
            else:
                print("]")

        print("dst:  ", Dest_ip, "(port) [", end ="")
        for i in range(0,6):
            print(Dest_mac[i],end="")
            if i < 5:
                print("",end=":")
            else:
                print("]")


        #print("addr=", addr)
        #print(" ".join([f"{data[i]:02x}" for i in range(18)]))
        #print("data=", data[14+20:total_length+14].decode())a
        print(len(data))
        print(total_length)
        to_print = ""
        for k in range(14+20,total_length):
            to_print += chr(data[k])
            print(chr(data[k]))
        print("",end="   ")
        print(to_print.encode())











def showpkts_IP(data):

    data_size = []
    header = 0
    offset = []
    for k in range(24,len(data)):
        if header == 8: #get size
            data_size.append(data[k] + data[k+1]*256 + data[k+2]*65536 +
                    data[k+3]*16777216)
            offset.append(k+8)
            header = -(data[k] + data[k+1]*256 + data[k+2]*65536 +
                    data[k+3]*16777216)- 8
            #subtract an extra 8 because we're still reading in the data size
        header += 1          


    for i in range(len(data_size)):
        counter = 1
        print("Dst-MAC= ", end="")
        for k in range(offset[i], 6+offset[i]): 
            print('{:02x}'.format(data[k]),end= "")
            if k == 5+offset[i]:
                print('\n',end="")
            else:
                print(':',end="")

        #Read in the src-mac
        print("Src-MAC= ", end="")
        for k in range(6+offset[i], 12+offset[i]): 
            print('{:02x}'.format(data[k]),end= "")
            if k == 11+offset[i]:
                print('\n',end="")
            else:
                print(':',end="")


        print("IHL= ", (data[14+offset[i]])%16) #mod 16 bc it is the second bit
        #not the whole byte

        print("Total Length= ", data[(17+offset[i])])


        print("Src-IP= ",end =" ")
        for k in range(26+offset[i], 30+offset[i]): #read in the src-ip
            if k == 29+offset[i]:
                print(data[k],end="\n")
            else:
                print(data[k],end=".")

        print("Dst-IP= ",end =" ")
        for k in range(30+offset[i], 34+offset[i]): #read in the dst-ip
            if k == 33+offset[i]:
                print(data[k],end="\n")
            else:
                print(data[k],end=".")


        print("data:")
        for k in range(offset[i]+34, offset[i] + 34 + ( data[17+offset[i]] - 20)): #loop through each peice of data to print it
            print('{:02x}'.format(data[k]),end= " ")
            if counter  % 16  == 0:
                print()
            counter += 1           
        print()


#if '__name__' == '__main__':
#import sys
#file = sys.argv[1]
#with open(file, 'rb') as f:
#    data = f.read()
#showpkts_TCP(data, "192.168.172.4", "192.168.172.5")
showpkts_TCP()
