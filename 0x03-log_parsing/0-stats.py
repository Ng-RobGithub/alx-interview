#!/usr/bin/python3
import sys
import signal


def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def parse_line(line, status_counts):
    try:
        parts = line.split()
        if len(parts) < 9:
            return 0

        status_code = int(parts[-2])
        file_size = int(parts[-1])

        if status_code in status_counts:
            status_counts[status_code] += 1

        return file_size
    except (IndexError, ValueError):
        return 0


def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    def handle_sigint(sig, frame):
        print_statistics(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_sigint)

    try:
        for line in sys.stdin:
            total_size += parse_line(line, status_counts)
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)
        raise

    print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
