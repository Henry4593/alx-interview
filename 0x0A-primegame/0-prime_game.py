#!/usr/bin/python3
"""Module for the Prime Game.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.

    Args:
        x (int): The number of rounds to be played.
        nums (list): A list of integers representing the upper limit for each
            round.

    Returns:
        str: The name of the player who won the most rounds, or None if it's a
            tie or invalid input.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # Generate primes up to the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # Filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
