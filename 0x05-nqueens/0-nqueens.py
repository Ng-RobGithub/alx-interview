#!/usr/bin/python3
""" N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP) """
import sys


class NQueen:
    """ Class for solving N Queen Problem """

    def __init__(self, n):
        """ Initialize the board size and other variables """
        self.n = n
        self.x = [0 for _ in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """ Check if k-th Queen can be placed in i-th column """
        for j in range(1, k):
            # Check if a queen is in the same column or diagonal
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
        return True

    def nQueen(self, k):
        """ Place queens on the board using backtracking """
        for i in range(1, self.n + 1):
            if self.place(k, i):
                self.x[k] = i
                if k == self.n:
                    # A solution is found
                    solution = []
                    for idx in range(1, self.n + 1):
                        solution.append([idx - 1, self.x[idx] - 1])
                    self.res.append(solution)
                else:
                    # Place the next queen
                    self.nQueen(k + 1)
        return self.res


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    queen = NQueen(N)
    res = queen.nQueen(1)

    for solution in res:
        print(solution)


if __name__ == "__main__":
    main()
