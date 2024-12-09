# Making Change

## Description
This project is part of the ALX Interview preparation curriculum. The goal is to determine the minimum number of coins needed to make change for a given amount of money.

## Files
- `0-making_change.py`: Contains the function `makeChange(coins, total)` that calculates the minimum number of coins needed to make change for a given amount.

## Function Prototype
```python
def makeChange(coins, total):
```

### Parameters
- `coins` (list of integers): A list of the values of the coins available.
- `total` (integer): The total amount of money to make change for.

### Returns
- The minimum number of coins needed to make change for the given amount.
- If the total is 0 or less, return 0.
- If the total cannot be met by any combination of the coins, return -1.

## Example
```python
coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3 (5 + 5 + 1)
```

## Usage
To use the `makeChange` function, import it into your script and call it with the appropriate arguments.

```python
from 0-making_change import makeChange

coins = [1, 2, 5]
total = 11
result = makeChange(coins, total)
print(f"Minimum coins needed: {result}")
```

## Author
This project is authored by Joseph Otieno as part of the ALX Interview preparation program.
