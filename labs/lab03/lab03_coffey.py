
def showpkts(data):
    counter = 1
    data_size = -1

    # Omit Global Header & Print Packet Header
    for k in range(24,32):
        print('{:02x}'.format(data[k]),end= " ")
        if counter  % 16  == 0:
            print()
        counter += 1

    # Read Packet Length
    hexLength = []
    for x in range(32,40):
        print('{:02x}'.format(data[x]), end = " ")
        if counter % 16 == 0:
            print()
        counter += 1

        # if packet length, read
        if x > 36:
            

import sys
file = sys.argv[1]
with open(file, 'rb') as f:
    data = f.read()
showpkts(data)
