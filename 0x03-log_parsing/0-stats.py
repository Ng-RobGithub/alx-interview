#!/usr/bin/python3
import sys


def print_statistics(file_sizes, status_codes):
    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_line(line, file_sizes, status_codes):
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[8]
        try:
            file_size = int(parts[9])
            file_sizes.append(file_size)
        except ValueError:
            pass
        if status_code.isdigit():
            status_codes[int(status_code)] += 1


def main():
    file_sizes = []
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0,
                    500: 0}
    line_count = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            parse_line(line, file_sizes, status_codes)
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(file_sizes, status_codes)
    except KeyboardInterrupt:
        print_statistics(file_sizes, status_codes)


if __name__ == "__main__":
    main()
