#!/usr/bin/python3

import sys

if __name__ == "__main__":
    """Print the sum of all the command line arguments."""

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
