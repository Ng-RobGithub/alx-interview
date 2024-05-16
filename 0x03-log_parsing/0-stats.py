#!/usr/bin/python3
import sys


def print_statistics(total_size, status_counts):
    print("File size: {}".format(total_size))
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def parse_line(line, status_counts):
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[8]
        try:
            status_code = int(status_code)
            if status_code in status_counts:
                status_counts[status_code] += 1
        except ValueError:
            pass


def main():
    total_size = 0
    status_counts = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parse_line(line, status_counts)
            parts = line.split()
            if len(parts) >= 10:
                try:
                    total_size += int(parts[9])
                except ValueError:
                    pass
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
