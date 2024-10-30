#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    skip = 0
    for byte in data:
        # Validate byte type and range
        if not isinstance(byte, int) or byte < 0 or byte > 0x10FFFF:
            return False

        # Single-byte character (ASCII)
        if byte <= 0x7F:
            skip = 0
            continue

        # Check for valid continuation bytes
        if skip > 0:
            if (byte & 0b11000000) != 0b10000000:
                return False
            skip -= 1
            continue

        # Multi-byte character handling
        num_bytes_expected = 0
        if (byte >> 7) == 0b0:  # 1-byte handled earlier
            continue
        elif (byte >> 5) == 0b110:
            num_bytes_expected = 1
        elif (byte >> 4) == 0b1110:
            num_bytes_expected = 2
        elif (byte >> 3) == 0b11110:
            num_bytes_expected = 3
        else:
            return False  # Invalid first byte

        # Check if enough bytes are remaining
        if len(data) - byte.bit_length() < (num_bytes_expected + 1):
            return False

        # Validate continuation bytes using bitwise AND
        for i in range(1, num_bytes_expected + 1):
            if (data[byte.bit_length() + i] & 0b11000000) != 0b10000000:
                return False
        skip = num_bytes_expected

    return skip == 0  # No continuation bytes remaining
