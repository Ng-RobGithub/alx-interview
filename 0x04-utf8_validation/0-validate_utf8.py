#!/usr/bin/python3
"""UTF-8 Validation module.
This module contains a function to validate if a given
data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): The data set to be validated.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for num in data:
        byte = num & 0xFF
        """Ensure we only consider the 8 least significant bits """

        if num_bytes == 0:
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7) != 0:  # 1-byte character must start with 0
                return False
        else:
            if (byte >> 6) != 0b10:  # Continuation bytes must start with 10
                return False
            num_bytes -= 1

    return num_bytes == 0
