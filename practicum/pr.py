#!bin/usr/python3


def showpkts_ARP(data):

    ARP_PROTOCOL = [8,6]
        
    data_size = []
    header = 0
    offset = []
    #convert both ip strings to int lists
    
    for k in range(24, len(data)):
        #check to see if we are looking at the correct IP addresses.
        if ( data[k] == ARP_PROTOCOL[0] and
            data[k+1] == ARP_PROTOCOL[1]
            ) :
            offset.append(k)
    
    '''print dst-mac
    src-mac
    opcode
    sender-hw-addr
    sender-prot-addr
    target-hw-addr
    target-prot-addr'''


    for i in offset:
        ps = packet_start = i - 12
        if data[ps+21] == 1 or data[ps+21] == 2: #check to ensure that we
                                                 # have a valid packet
            print("===")
            
            print("Dst-MAC=",end=" ")
            for k in range(ps, ps+6):
                print('{:02x}'.format(data[k]),end= "")
                if k == 5+ps:
                    print('\n',end="")
                else:
                    print(':',end="")

            print("Src-MAC=",end=" ")
            for k in range(ps+6, ps+12):
                print('{:02x}'.format(data[k]),end= "")
                if k == 11+ps:
                    print('\n',end="")
                else:
                    print(':',end="")
            
            print("Opcode=",end=" ")
            print('{:2x}'.format(data[ps+20]*256 + data[ps+21]),end= "\n")


            print("Sender-HW-Addr=",end=" ")
            for k in range(ps+22, ps+28):
                print('{:02x}'.format(data[k]),end= "")
                if k == 27+ps:
                    print('\n',end="")
                else:
                    print(':',end="")
            
            print("Sender-Prot-Addr= ",end =" ")
            for k in range(28+ps, 32+ps): #read in the src-ip
                if k == 31+ps:
                    print(data[k],end="\n")
                else:
                    print(data[k],end=".")

            print("Target-HW-Addr=",end=" ")
            for k in range(ps+32, ps+38):
                print('{:02x}'.format(data[k]),end= "")
                if k == 37+ps:
                    print('\n',end="")
                else:
                    print(':',end="")
            
            print("Target-Prot-Addr= ",end =" ")
            for k in range(38+ps, 42+ps): #read in the src-ip
                if k == 41+ps:
                    print(data[k],end="\n")
                else:
                    print(data[k],end=".")

            
            print("===\n")
        
