#!/usr/bin/python3

def generate_pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle


def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
    return triangle


if __name__ == "__main__":
    print_triangle(generate_pascal_triangle(5))
