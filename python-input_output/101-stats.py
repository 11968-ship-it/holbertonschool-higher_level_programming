#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:

- Total file size
- Number of lines by status code

Prints statistics every 10 lines and on keyboard interruption (CTRL+C)
"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

total_size = 0
status_count = {code: 0 for code in status_codes}
line_count = 0


def print_stats():
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_count):
        if status_count[code]:
            print("{}: {}".format(code, status_count[code]))


try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        try:
            status = int(parts[-2])
            size = int(parts[-1])
        except (IndexError, ValueError):
            continue

        if status in status_count:
            status_count[status] += 1
        total_size += size
        line_count += 1

        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    pass
finally:
    print_stats()
