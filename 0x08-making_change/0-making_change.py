#!/usr/bin/python3
"""
Module for making change problem using dynamic programming
"""

def makeChange(coins, total):
    if total < 0:
        return -1
    if total == 0:
        return 0
    
    # Initialize dp array with infinity for all amounts from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Iterate over each coin denomination
    for coin in coins:
        # Update dp array for all amounts from coin value to total
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # The result will be dp[total]
    if dp[total] == float('inf'):
        return -1  # It's not possible to make the total amount with given coins
    else:
        return dp[total]

# Testing the function with provided test cases
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
