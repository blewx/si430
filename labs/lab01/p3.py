def pr(a):
    print(f"dec: {a:d}\nhex: 0x{a:02x}\nbin: {a:08b}")
def zero_out_top(a,n):
    d = int(n*'0' + (8-n)*'1',2)
    a = a & d 
    return a
def set_zero_at(a,n):
    de = int(n*'1'+ '0' + (8-n-1)*'1',2)
    a = a & de
    return a;
def set_one_at(a,n):
    de = int(n*'0'+ '1' + (8-n-1)*'0',2)
    a = a | de
    return a;
