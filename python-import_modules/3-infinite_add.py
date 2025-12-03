#!/usr/bin/python3
import sys

def main():
    # Sum all command-line arguments casted to integers
    total = sum(int(arg) for arg in sys.argv[1:])
    print(total)

if __name__ == "__main__":
    main()
