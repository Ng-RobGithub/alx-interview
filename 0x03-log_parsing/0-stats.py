#!/usr/bin/python3
"""Log Parser"""

import sys


def print_stats(file_size, status_codes):
    """Print statistics."""
    print('File size: {}'.format(file_size[0]))
    for key in sorted(status_codes.keys()):
        if status_codes[key]:
            print('{}: {}'.format(key, status_codes[key]))


def parse_line(line, file_size, status_codes):
    """Parse a single line of input and update metrics."""
    try:
        parts = line.split()
        # File size is the last parameter
        file_size[0] += int(parts[-1])
        # Status code is the second-to-last parameter
        status_code = int(parts[-2])
        # Update status code count if it exists in the dictionary
        if status_code in status_codes:
            status_codes[status_code] += 1
    except (IndexError, ValueError):
        pass


def main():
    file_size = [0]
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_num = 0

    try:
        for line in sys.stdin:
            parse_line(line, file_size, status_codes)
            line_num += 1
            if line_num % 10 == 0:
                print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
    print_stats(file_size, status_codes)


if __name__ == "__main__":
    main()
