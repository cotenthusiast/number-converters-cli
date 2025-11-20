from .binary import signed_binary_to_denary as binary_to_denary
from .binary import denary_to_signed_binary as denary_to_binary

def hexadecimal_to_denary(hex_string): # hexadecimal string to denary number
    hex_string = hex_string.upper() # convert to uppercase
    options = { # mapping of hexadecimal digits to binary nibbles
        '0': "0000",
        '1': "0001",
        '2': "0010",
        '3': "0011",
        '4': "0100",
        '5': "0101",
        '6': "0110",
        '7': "0111",
        '8': "1000",
        '9': "1001",
        'A': "1010",
        'B': "1011",
        'C': "1100",
        'D': "1101",
        'E': "1110",
        'F': "1111"      
    }
    for c in hex_string: # validate hex string
        if c not in options: #  raise error for invalid digit
            raise ValueError("Invalid hexadecimal digit: " + c)
    binary_string = ''.join(options[c] for c in hex_string) # convert hex to binary
    denary_value = binary_to_denary(binary_string) # convert binary to denary
    return denary_value
        
def denary_to_hexadecimal(denary_number): # denary number to hexadecimal string
    bin = denary_to_binary(denary_number) # convert denary to binary string
    while len(bin) % 4 != 0: # pad with leading zeros
        bin = '0' + bin # pad with leading zeros
    hex_string = "" # initialize hex string
    options = { # mapping of binary nibbles to hexadecimal digits
        "0000": '0',
        "0001": '1',
        "0010": '2',
        "0011": '3',
        "0100": '4',
        "0101": '5',
        "0110": '6',
        "0111": '7',
        "1000": '8',
        "1001": '9',
        "1010": 'A',
        "1011": 'B',
        "1100": 'C',
        "1101": 'D',
        "1110": 'E',
        "1111": 'F'      
    }
    for i in range (0,len(bin), 4): # iterate through binary string in nibbles
        nibble  = bin[i:i+4] # get current nibble
        hex_string += options[nibble] # append corresponding hex digit
    return hex_string # return final hex string

def hexadecimal_to_binary(hex_string): # hexadecimal string to binary string
    hex_string = hex_string.upper() # convert to uppercase
    options = { # mapping of hexadecimal digits to binary nibbles
        '0': "0000",
        '1': "0001",
        '2': "0010",
        '3': "0011",
        '4': "0100",
        '5': "0101",
        '6': "0110",
        '7': "0111",
        '8': "1000",
        '9': "1001",
        'A': "1010",
        'B': "1011",
        'C': "1100",
        'D': "1101",
        'E': "1110",
        'F': "1111"      
    }
    for c in hex_string: # validate hex string
        if c not in options:
            raise ValueError("Invalid hexadecimal digit: " + c) # raise error for invalid digit
    binary_string = ''.join(options[c] for c in hex_string) # convert hex to binary
    return binary_string # return binary string

def binary_to_hexadecimal(binary_string): # binary_string to hexadecimal
    while len(bin) % 4 != 0: # pad with leading zeros
        bin = '0' + bin
    hex_string = "" # initialize hex string
    options = { # mapping of binary nibbles to hexadecimal digits
        "0000": '0',
        "0001": '1',
        "0010": '2',
        "0011": '3',
        "0100": '4',
        "0101": '5',
        "0110": '6',
        "0111": '7',
        "1000": '8',
        "1001": '9',
        "1010": 'A',
        "1011": 'B',
        "1100": 'C',
        "1101": 'D',
        "1110": 'E',
        "1111": 'F'      
    }
    for i in range (0,len(bin), 4): # iterate through binary string in nibbles
        nibble  = bin[i:i+4] # get current nibble
        hex_string += options[nibble] # append corresponding hex digit
    return hex_string # return final hex string