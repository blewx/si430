#!bin/usr/python3

def showpkts(data):
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
        print("data:")
        for k in range(offset[i], data_size[i]+offset[i]): #read in the size of the first packet
            print('{:02x}'.format(data[k]),end= " ")
            if counter  % 16  == 0:
                print()
            counter += 1           
        print()
        print()


def showpkts_TCP(data, ip1, ip2):

    data_size = []
    header = 0
    offset = []
    #convert both ip strings to int lists
    ip1h = ip1.split(".")
    ip2h = ip2.split(".")
    for i in range(4):
        ip1h[i] = int(ip1h[i])
        ip2h[i] = int(ip2h[i])

    for k in range(24, len(data)):
        #check to see if we are looking at the correct IP addresses.
        if ( (ip1h[0] == data[k] and 
              ip1h[1] == data[k+1] and 
              ip1h[2] == data[k+2] and 
              ip1h[3] == data[k+3] and 
              ip2h[0] == data[k+4] and 
              ip2h[1] == data[k+5] and 
              ip2h[2] == data[k+6] and 
              ip2h[3] == data[k+7]) or

            (ip2h[0] == data[k] and 
             ip2h[1] == data[k+1] and 
             ip2h[2] == data[k+2] and 
             ip2h[3] == data[k+3] and 
             ip1h[0] == data[k+4] and 
             ip1h[1] == data[k+5] and 
             ip1h[2] == data[k+6] and 
             ip1h[3] == data[k+7])   ) :
                offset.append(k)
    
    for i in offset:
        data_len = (data[i-9] + data[i-10]*256) #subtract data header len to get past the
        #header
        ip_header_len = (data[i-12]%16)*4 
        tcp_header_len = (data[i+20]//16)*4 

        #find the ips and ports for both the sender and receiver
        sender_ip = str(data[i]) + "." + str(data[i+1]) + "." + str(data[i+2]) + "." + str(data[i+3])
        receiver_ip = str(data[i+4]) + "." + str(data[i+5]) + "." + str(data[i+6]) + "." + str(data[i+7])
        sender_port = (data[i+9] + data[i+8]*256)         
        receiver_port = (data[i+11] + data[i+10]*256) 

        #filter out if there is no payload
        if data_len - ip_header_len - tcp_header_len > 0:
            print(sender_ip + "(" + str(sender_port) + ") -> " + receiver_ip + "(" +
              str(receiver_port) + ") :")
            #print the data
            to_print = ""
            for k in range(i + 40, i + 40 + data_len - ip_header_len -
                           tcp_header_len):
                to_print += chr(data[k])
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
#showpkts_IP(data)
