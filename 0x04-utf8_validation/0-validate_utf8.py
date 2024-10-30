#!/usr/bin/python3
"""utf-8 validation module"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Args:
        data (List[int]): List of integers representing bytes.
    Returns:
        bool: True if the data is valid UTF-8, False otherwise.
    """
    num_bytes_expected: int = 0  # Number of bytes expected for the curr char

    for byte in data:
        if byte < 0 or byte > 255:
            return False  # Each integer should be a valid byte (0-255)

        if num_bytes_expected == 0:
            if (byte >> 7) == 0b0:  # 1-byte character (0xxxxxxx)
                continue
            elif (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
                num_bytes_expected = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                num_bytes_expected = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                num_bytes_expected = 3
            else:
                return False  # Invalid first byte
        else:
            # Check continuation bytes (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            num_bytes_expected -= 1

    return num_bytes_expected == 0
