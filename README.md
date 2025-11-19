# Number Converter CLI v1.0

## Description
A simple CLI tool that (currently) converts between binary and decimal

## Project Structure
```bash
numberconverters/
│
├── converters/          # Package for all conversion modules
│   ├── __init__.py      # Marks this as a package
│   ├── binary.py        # Binary ↔ denary functions
│   ├── hex.py           # Hex ↔ denary functions (future)
│   └── octal.py         # Octal ↔ denary functions (future)
├── cli.py               # CLI interface that uses the package
└── README.md
```

## Features
- Convert denary numbers to binary
- Convert binary numbers to denary
- Easy-to-use CLI with `to-binary` and `to-denary` commands
- Future: Add hex and octal conversions

## Usage
```bash
python cli.py dec2bin 42
# Output: 101010

python cli.py bin2dec 101010
# Output: 42
```


