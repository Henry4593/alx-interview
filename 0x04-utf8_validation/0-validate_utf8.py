#!/usr/bin/python3
"""utf-8 validation module"""


def validUTF8(data):
    """
        Args:
            data (list): List of integers representing bytes.
        Returns:
            bool: True if the data is valid UTF-8, False otherwise.
    """
    num_bytes_expected = 0  # Number of bytes expected for the currentcharacter

    for byte in data:
        """Check the number of leading 1s to determine how many bytes
        are expected"""
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
