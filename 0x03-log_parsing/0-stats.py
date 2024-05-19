#!/usr/bin/python3
"""Log Parser"""
import sys


def print_stats(file_size, status_codes):
    """Print statistics"""
    print('File size: {}'.format(file_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key]:
            print('{}: {}'.format(key, status_codes[key]))


def parse_line(line, file_size, status_codes):
    """Checks the line for matches and updates file size and
    status code counts
    """
    try:
        parts = line.split()
        file_size += int(parts[-1])
        status_code = int(parts[-2])
        if status_code in status_codes:
            status_codes[status_code] += 1
    except Exception:
        pass
    return file_size


def main():
    file_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    linenum = 1

    try:
        for line in sys.stdin:
            file_size = parse_line(line, file_size, status_codes)
            if linenum % 10 == 0:
                print_stats(file_size, status_codes)
            linenum += 1
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
    print_stats(file_size, status_codes)


if __name__ == '__main__':
    main()
