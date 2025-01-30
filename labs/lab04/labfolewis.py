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
        print("data:")
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
        print("Type= ", end="")
        for k in range(12+offset[i], 14+offset[i]): #read in the size of the first packet
            print('{:02x}'.format(data[k]),end= "")
            if k == 13+offset[i]:
                print('\n',end="")
            else:
                print(' ',end="")

        for k in range(offset[i]+14, data_size[i]+offset[i]): #read in the size of the first packet
            print('{:02x}'.format(data[k]),end= " ")
            if counter  % 16  == 0:
                print()
            counter += 1           
        print()
        print()


#if '__name__' == '__main__':
import sys
file = sys.argv[1]
with open(file, 'rb') as f:
    data = f.read()
showpkts(data)
