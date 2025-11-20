# Number Converter CLI v1.02

## Description
A simple CLI tool that converts between binary, decimal, hex and octal

## Project Structure
```bash
numberconverters/
│
├── converters/          # Package for all conversion modules
│   ├── __init__.py      # Marks this as a package
│   ├── binary.py        # Binary ↔ Decimal functions
│   ├── hex.py           # Hex ↔ Decimal and Hex ↔ Binary functions 
│   └── octal.py         # Octal ↔ Decimal , Octal ↔ Binary and Octal ↔ Hex functions 
├── cli.py               # CLI interface that uses the package
└── README.md
```

## Features
- Convert numbers between decimal, binary, hexadecimal, and octal
- Easy-to-use command line interface (CLI)
- Planned future enhancement: organize sub-parsers into functional groups

## Usage
```bash
python cli.py dec2bin 42
# Output: 101010

python cli.py bin2dec 101010
# Output: 42
```


