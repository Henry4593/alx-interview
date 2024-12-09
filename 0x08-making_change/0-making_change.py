#!/usr/bin/python3
"""Module for change making calculations.
"""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet a given
    total amount from a pile of coins of different values.

    Args:
        coins (list): A list of the values of available coins.
        total (int): The total amount to achieve with the coins.

    Returns:
        int: The minimum number of coins needed to meet the total.
             Returns -1 if the total cannot be met by any combination of coins.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
