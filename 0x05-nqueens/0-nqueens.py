#!/usr/bin/python3
"""N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP)"""
import sys


class NQueen:
    """Class for solving N Queen Problem"""

    def __init__(self, n):
        """Initialize global variables"""
        self.n = n
        self.x = [0 for _ in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """
        Check if k-th Queen can be placed in i-th column (True)
        or if there are attacking queens in row or diagonal (False)
        """
        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
        return True

    def solve(self, k):
        """
        Recursively try to place queens on the board
        Args:
        k: starting queen from which to evaluate (should be 1)
        """
        for i in range(1, self.n + 1):
            if self.place(k, i):
                self.x[k] = i
                if k == self.n:
                    # Placed all n Queens (A solution was found)
                    solution = []
                    for row in range(1, self.n + 1):
                        solution.append([row - 1, self.x[row] - 1])
                    self.res.append(solution)
                else:
                    # Need to place more Queens
                    self.solve(k + 1)
        return self.res


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueen(N)
solutions = queen.solve(1)

for solution in solutions:
    print(solution)
