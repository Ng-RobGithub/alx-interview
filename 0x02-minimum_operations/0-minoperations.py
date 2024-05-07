#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to result in exactly n H
characters in the file.
"""

import math


def minOperations(n):
    """Calculates the fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    if n <= 1:
        return 0

    ops = 0
    divisor = 2
    while n > 1 and divisor <= math.isqrt(n):
        while n % divisor == 0:
            ops += divisor
            n //= divisor
        divisor += 1

    if n > 1:
        ops += n

    return ops
