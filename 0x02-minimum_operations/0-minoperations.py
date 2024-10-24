#!/usr/bin/python3
'''Module for computing the minimum number of operations to achieve
    exactly n 'H' characters in a text file.
'''


def minOperations(n):
    '''Calculates the minimum number of operations required to get
     exactly n 'H' characters using copy and paste operations.

     Args:
          n (int): The target number of 'H' characters.

     Returns:
          int: The minimum number of operations needed, or 0 if n is not a
          valid integer.
    '''
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            # Initialize with the first copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            # Copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            # Paste
            done += clipboard
            ops_count += 1
    return ops_count
