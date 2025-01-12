import sys 
file  = sys.argv[1]
with open(file, 'rb') as f:
    data = f.read()

lower_val = 0
for i in range(len(data)):
    if i % 16 == 0 or i == len(data):
        bytes = data[lower_val:i]
        if i > 0:
            print('|',end="")
            for byte in bytes:
                if byte == ord('\n'):  #check to see if the byte is = \n, this means
                                       #that it read in a period as a newline,
                                       #so change that \n into a . for printing
                    print('.',end="")
                else:
                    print(chr(byte), end="")
            print('|')
            lower_val = i
        print('{:08x}'.format(i), end='  ') #print bytes read sofar
    elif i % 8 == 0:
        print('{:02x}'.format(data[i]), end='  ') #special print to print double
                                                  #space for formatting between
                                                  #bytes 8 and 9 of each 16 byte
                                                  #row
    else:
        print('{:02x}'.format(data[i]), end=' ')

print()
print('{:08x}'.format(len(data)))
