def denary_to_unsigned_binary(x):

    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    elif x%2 == 0:
        return denary_to_unsigned_binary(x//2) + "0"
    else:
        return denary_to_unsigned_binary(x//2) + "1"
    
def unsigned_binary_to_denary(x):

    if x == "0":
        return 0
    elif x == "1":
        return 1
    elif x[0] == "1":
        return 2**(len(x)-1) + unsigned_binary_to_denary(x[1:])
    else:
        return unsigned_binary_to_denary(x[1:])

def convert_twoscomplement(x):
    y = ''.join('1' if c == "0" else '0' for c in x)
    for _ in range (len(y)-1,-1,-1):
        if y[_] == "0":
            y = y[0:_]+"1"+"0"*(len(y)-len(y[0:_])-1)
            break
    else:
        y = "0" * len(y) 
    return y
    
def signed_binary_to_denary(x):
    if x[0] == "1":
        y = convert_twoscomplement(x)
        return -unsigned_binary_to_denary(y)
    else:
        return unsigned_binary_to_denary(x)

def denary_to_signed_binary(x):
    if x >= 0:
        return denary_to_unsigned_binary(x)
    else:
        return convert_twoscomplement("0"+denary_to_unsigned_binary(-x))
