from converters.binary import signed_binary_to_denary as binary_to_denary
from converters.binary import denary_to_signed_binary as denary_to_binary
from converters.hexadecimal import *
from converters.octal import *

import argparse

parser = argparse.ArgumentParser(
    prog = "converter",
    description = "program that converts between different formats ",
    epilog = "Thank you for using the %(prog)s"
)

subparsers = parser.add_subparsers(
    title="conversions",
    help = "conversions between different formats"
)

#parser for binary to denary
bin2dec_parser = subparsers.add_parser(
    "bin2dec", help = "convert between binary and denary")
bin2dec_parser.add_argument(
    "operand",
    type = str,
    help = "binary number"
    )
bin2dec_parser.set_defaults(func=binary_to_denary)

#parser for denary to binary
dec2bin_parser = subparsers.add_parser(
    "dec2bin", help = "convert between denary and binary"
    )
dec2bin_parser.add_argument(
    "operand",
    type = int,
    help = "denary number"
    )
dec2bin_parser.set_defaults(func=denary_to_binary)

#parser for hexadecimal to denary
hex2dec_parser = subparsers.add_parser(
    "hex2dec", help = "convert between hexadecimal and denary"
    )
hex2dec_parser.add_argument(
    "operand",
    type = str,
    help = "hexadecimal number"
    )
hex2dec_parser.set_defaults(func=hexadecimal_to_denary)

#parser for denary to hexadecimal
dec2hex_parser = subparsers.add_parser(
    "dec2hex", help = "convert between denary and hexadecimal"
    )
dec2hex_parser.add_argument(
    "operand",
    type = int,
    help = "denary number"
    )
dec2hex_parser.set_defaults(func=denary_to_hexadecimal)

#parser for hexadecimal to binary
hex2bin_parser = subparsers.add_parser(
    "hex2bin", help = "convert between hexadecimal and binary"
    )
hex2bin_parser.add_argument(
    "operand",
    type = str,
    help = "hexadecimal number"
    )
hex2bin_parser.set_defaults(func=hexadecimal_to_binary)

#parser for binary to hexadecimal
bin2hex_parser = subparsers.add_parser(
    "bin2hex", help = "convert between binary and hexadecimal"
    )
bin2hex_parser.add_argument(
    "operand",
    type = str,
    help = "binary number"
    )
bin2hex_parser.set_defaults(func=binary_to_hexadecimal)

#parser for octal to denary
oct2dec_parser = subparsers.add_parser(
    "oct2dec", help = "convert between octal and denary"
    )
oct2dec_parser.add_argument(
    "operand",
    type = str,
    help = "octal number"
    )
oct2dec_parser.set_defaults(func=octal_to_denary)

#parser for denary to octal
dec2oct_parser = subparsers.add_parser(
    "dec2oct", help = "convert between denary and octal"
    )
dec2oct_parser.add_argument(
    "operand",
    type = int,
    help = "denary number"
    )
dec2oct_parser.set_defaults(func=denary_to_octal)

#parser for octal to binary
oct2bin_parser = subparsers.add_parser(
    "oct2bin", help = "convert between octal and binary"
    )
oct2bin_parser.add_argument(
    "operand",
    type = str,
    help = "octal number"
    )
oct2bin_parser.set_defaults(func=octal_to_binary)

#parser for binary to octal
bin2oct_parser = subparsers.add_parser( 
    "bin2oct", help = "convert between binary and octal" 
    )
bin2oct_parser.add_argument(
    "operand",
    type = str,
    help = "binary number"
    )
bin2oct_parser.set_defaults(func=binary_to_octal)

#parser for octal to hexadecimal
oct2hex_parser = subparsers.add_parser(
    "oct2hex", help = "convert between octal and hexadecimal"
    )
oct2hex_parser.add_argument(
    "operand",
    type = str,
    help = "octal number"
    )
oct2hex_parser.set_defaults(func=octal_to_hexadecimal)

#parser for hexadecimal to octal
hex2oct_parser = subparsers.add_parser(
    "hex2oct", help = "convert between hexadecimal and octal"
    )
hex2oct_parser.add_argument(
    "operand",
    type = str,
    help = "hexadecimal number"
    )
hex2oct_parser.set_defaults(func=hexadecimal_to_octal)

args = parser.parse_args()

result = args.func(args.operand)
print(result)
