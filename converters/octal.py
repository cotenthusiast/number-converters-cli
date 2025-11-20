from .binary import signed_binary_to_denary as binary_to_denary
from .binary import denary_to_signed_binary as denary_to_binary
from .binary import unsigned_binary_to_denary as binary_to_denary2
from .hexadecimal import *
import math

def octal_to_denary(octal_string):
    sum = 0 # Initialize sum to 0
    for i in range (len(octal_string)): # Iterate through each digit
        c = octal_string[i] # Get the current digit
        sum += int(c) * 8 ** i # Convert digit to denary and add to sum
    return sum # Return the final denary value

def denary_to_octal(denary_number):
    x = math.log(denary_number, 8) # Calculate the highest power of 8
    if x % 1 != 0:
        x = int(x) + 1
    octal_string = "" # Initialize octal string
    temp = 0 # Temporary variable to hold digit value
    for i in range (x): #  Iterate through each power of 8
        while denary_number > 8 ** i: 
            denary_number -= 8 ** i # Subtract powers of 8 from denary number
            temp += 1 # Increment temporary variable
        octal_string = str(temp) + octal_string
        temp = 0
    return octal_string # Return the final octal string

def octal_to_binary(octal_string):
    den = octal_to_denary(octal_string) # Convert octal to denary
    bin = denary_to_binary(den) # Convert denary to binary
    return bin # Return binary string

def binary_to_octal(binary_string):
    den = binary_to_denary(binary_string) # Convert binary to denary
    octal_string = denary_to_octal(den) # Convert denary to octal
    return octal_string # Return octal string

def octal_to_hexadecimal(octal_string):
    denary_value = octal_to_denary(octal_string) # Convert octal to denary 
    hex_string = denary_to_hexadecimal(denary_value) # Convert denary to hexadecimal
    return hex_string # return hexadecimal string

def hexadecimal_to_octal(hex_string):
    bin_value = hexadecimal_to_binary(hex_string) # Convert hexadecimal to binary
    denary_value = binary_to_denary2(bin_value) # Convert binary to denary (unsigned)
    octal_string = denary_to_octal(denary_value) # Convert denary to octal
    octal_string = octal_string.lstrip("0") or "0" # Remove leading zeros

    return octal_string # Return octal string
