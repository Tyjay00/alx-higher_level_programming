#!/usr/bin/python3

import sys
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1
    if argc == 0:
        print("Number of argument(s).")
    elif argc == 1:
        print("Number of argument: {}".format(argc))
    else:
        print("Number of arguments: {}".format(argc))
    for i, arg in enumerate(argv[1:]):
        print("{}: {}".format(i + 1, arg))
