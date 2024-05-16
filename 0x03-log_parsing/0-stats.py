#!/usr/bin/python3

import sys

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0,
                      500: 0}

try:
    line_count = 0
    for line in sys.stdin:
        # Split the input line by spaces
        parts = line.split()

        # Check if the input format matches the expected format
        if len(parts) == 10 and parts[5].isdigit():
            status_code = int(parts[8])
            file_size = int(parts[9])

            # Update metrics
            total_file_size += file_size
            status_code_counts[status_code] += 1

            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print(f"Total file size: File size: {total_file_size}")
                for code, count in sorted(status_code_counts.items()):
                    if count > 0:
                        print(f"{code}: {count}")

except KeyboardInterrupt:
    # Handle Ctrl+C interruption
    print(f"Total file size: File size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
