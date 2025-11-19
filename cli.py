from converters.binary import signed_binary_to_denary as binary_to_denary
from converters.binary import denary_to_signed_binary as denary_to_binary
import argparse

parser = argparse.ArgumentParser(
    prog = "converter",
    description = "program that converts between different formats",
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

args = parser.parse_args()

result = args.func(args.operand)
print(result)
