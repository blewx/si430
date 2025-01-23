def showpkts(data):


    counter = 1
    data_size = -1
    for k in range(24,len(data)): #start at 24 to get rid of global header
        print('{:02x}'.format(data[k]),end= " ")
        if counter  % 16  == 0:
            print()
        counter += 1
        '''
        to_print = ""
        bytes = data[]
        print('{:08x}'.format(k*16), end='  ') #print bytes read sofar
        #print(k, "  ", num_iters)
        for i in range(0 + (k*16),16 + (k*16)):
            if counter < len(data):
                to_print += chr(data[counter])
            counter += 1
            #print(" | ")
            if i >= len(data):
                print('  ', end = ' ')
                if i % 8 == 0 and (i % 16 == 8) or (i % 16 == 15):
                    print("", end=' ')
            elif i % 8 == 0 and (i % 16 == 8) or (i % 16 == 15):
                print('{:02x}'.format(data[i]), end='  ') #special print to print double
                                                        #space for formatting between
                                                        #bytes 8 and 9 of each 16 byte
                                                        #row
            else:
                print('{:02x}'.format(data[i]), end=' ')
    '''
import sys
file = sys.argv[1]
with open(file, 'rb') as f:
    data = f.read()
showpkts(data)
