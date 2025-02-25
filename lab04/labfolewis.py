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
    #convert both ip strings to hex lists
    ip1h = ip1.split(".")
    ip2h = ip2.split(".")
    for i in range(4):
        ip1h[i] = int(ip1h[i])#hex(int(ip1h[i]))
        ip2h[i] = int(ip2h[i])#hex(int(ip1h[i]))
    print(ip1h)
    print(ip2h)

    for k in range(24, len(data)):
        #print(ip1h[0])
        #print(data[k])
        if ( ip1h[0] == data[k] and 
        ip1h[1] == data[k+1] and 
        ip1h[2] == data[k+2] and 
        ip1h[3] == data[k+3] and 
        ip2h[0] == data[k+4] and 
        ip2h[1] == data[k+5] and 
        ip2h[2] == data[k+6] and 
        ip2h[3] == data[k+7] ) :
            offset.append(k)
            print(data[k-9])
            for i in range(8):
                print(data[k+i],end="")
                if i == 3 or i == 7:
                    print("",end=" ")
                else:
                    print("",end=".")
            print()
    for i in offset:
        print(data[i-10], end = " ")
        print(data[i-9])
        data_len = (data[i-9] + data[i-10]*256) #subtract data header len to get past the
        #header
        data_header_len = (data[i-12]%16)*4 


        print(str(hex(i)) + " protocol == " + str( data[i-3]) + " len == " +
                str(data_len) + " data header len == " + str(data_header_len))
    
'''
    for k in range(24,len(data)):
        

    for i in range(len(data_size)):
        counter = 1
        print("Dst-MAC= ", end="")
        for k in range(offset[i], 6+offset[i]): #read in the size of the first packet
            print('{:02x}'.format(data[k]),end= "")
            if k == 5+offset[i]:
                print('\n',end="")
            else:
                print(':',end="")
        print("Src-MAC= ", end="")
        for k in range(6+offset[i], 12+offset[i]): #read in the size of the first packet
            print('{:02x}'.format(data[k]),end= "")
            if k == 11+offset[i]:
                print('\n',end="")
            else:
                print(':',end="")
        
        #for k in range(12+offset[i], 14+offset[i]): #read in the size of the first packet
        #print("= ", 14+offset[i])
        print("IHL= ", (data[14+offset[i]])%16) #mod 16 bc it is 
        print("Total Length= ", data[(17+offset[i])])
        
        print("Dst-IP= ",end =" ")
        for k in range(26+offset[i], 30+offset[i]): #read in the size of the first packet
            if k == 29+offset[i]:
                print(data[k],end="\n")
            else:
                print(data[k],end=".")

        print("Src-IP= ",end =" ")
        for k in range(30+offset[i], 34+offset[i]): #read in the size of the first packet
            if k == 33+offset[i]:
                print(data[k],end="\n")
            else:
                print(data[k],end=".")

        print("data:")
        for k in range(offset[i]+34, data_size[i]+offset[i]): #read in the size of the first packet
            print('{:02x}'.format(data[k]),end= " ")
            if counter  % 16  == 0:
                print()
            counter += 1           
        print()
'''

def showpkts_Eth(data):

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
        for k in range(offset[i], 6+offset[i]): #read in the size of the first packet
            print('{:02x}'.format(data[k]),end= "")
            if k == 5+offset[i]:
                print('\n',end="")
            else:
                print(':',end="")
        print("Src-MAC= ", end="")
        for k in range(6+offset[i], 12+offset[i]): #read in the size of the first packet
            print('{:02x}'.format(data[k]),end= "")
            if k == 11+offset[i]:
                print('\n',end="")
            else:
                print(':',end="")
        
        #print("= ", 14+offset[i])
        print("IHL= ", (data[14+offset[i]])%16) #mod 16 bc it is 
        print("Total Length= ", data[(17+offset[i])])
        
        print("Dst-IP= ",end =" ")
        for k in range(26+offset[i], 30+offset[i]): #read in the size of the first packet
            if k == 29+offset[i]:
                print(data[k],end="\n")
            else:
                print(data[k],end=".")

        print("Src-IP= ",end =" ")
        for k in range(30+offset[i], 34+offset[i]): #read in the size of the first packet
            if k == 33+offset[i]:
                print(data[k],end="\n")
            else:
                print(data[k],end=".")

        print("data:")
        for k in range(offset[i]+34, data_size[i]+offset[i]): #read in the size of the first packet
            print('{:02x}'.format(data[k]),end= " ")
            if counter  % 16  == 0:
                print()
            counter += 1           
        print()


#if '__name__' == '__main__':
import sys
file = sys.argv[1]
with open(file, 'rb') as f:
    data = f.read()
showpkts_TCP(data, "192.168.172.4", "192.168.172.5")
