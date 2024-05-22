0x04. UTF-8 Validation

UTF-8 (Unicode Transformation Format - 8-bit) is a variable-width character encoding used for electronic communication. UTF-8 can encode all possible characters (code points) in Unicode, and it is backward-compatible with ASCII. UTF-8 is designed to be efficient in terms of both storage and processing and is the most common encoding used on the web.

Key Concepts:
1. Bitwise Operations in Python:

a. AND (&): Compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, it is set to 0.
b. OR (|): Compares each bit of the first operand to the corresponding bit of the second operand. If one of the bits is 1, the corresponding result bit is set to 1. Otherwise, it is set to 0.
c. XOR (^): Compares each bit of the first operand to the corresponding bit of the second operand. If one of the bits is 0 and the other bit is 1, the corresponding result bit is set to 1. Otherwise, it is set to 0.
d. NOT (~): Inverts all the bits of the operand.
e. Left Shift (<<): Shifts the bits of the first operand left by the number of positions specified by the second operand.
f. Right Shift (>>): Shifts the bits of the first operand right by the number of positions specified by the second operand.
2. UTF-8 Encoding Scheme:
3. Data Representation:
4. List Manipulation in Python:
5. Boolean Logic:

TASK:

Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
==============================================================================
# UTF-8 Validation

This project contains a Python function to validate whether a given dataset represents a valid UTF-8 encoding.

## Function

### `validUTF8(data)`

This function takes a list of integers representing byte data and returns `True` if the data is a valid UTF-8 encoding, else `False`.

## Usage

To use this function, simply import it and call it with a list of integers:

```python
from 0-validate_utf8 import validUTF8

data = [197, 130, 1]
print(validUTF8(data))  # True

data = [235, 140, 4]
print(validUTF8(data))  # False
