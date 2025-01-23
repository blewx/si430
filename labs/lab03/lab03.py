def showpkts(data):


    data_size = []
    header = 0
    offset = []
    for k in range(24,len(data)):
        if header == 8: #get size
            data_size.append(data[k] + data[k+1] + data[k+2] + data[k+3])
            offset.append(k+8)
            header = -(data[k] + data[k+1] + data[k+2] + data[k+3]) - 8
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
        
import sys
file = sys.argv[1]
with open(file, 'rb') as f:
    data = f.read()
showpkts(data)
