import sys 
file  = sys.argv[1]
with open(file, 'rb') as f:
    data = f.read()


lower_val = 0

num_iters = len(data) #variable that figures out how far past data lenght the program needs to run so that it
              #prints the correct number of double spaces to print the last text line (|****|)
while(num_iters % 16  == 0):
    num_iters += 1
num_iters = int(num_iters/16)

counter = 0
for k in range(num_iters+1):
    to_print = ""
    bytes = data[k*16:(k+1)*16]
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
    print('|',end="")
    for byte in to_print:
        if(byte.isprintable()):
            if byte == '\n':  #check to see if the byte is = \n, this means
                #that it read in a period as a newline,
                            #so change that \n into a . for printing
                print('.',end="")
            else:
                print(byte, end="")
        else:
            print('.',end="")
    print('|')

print('{:08x}'.format(len(data)))
