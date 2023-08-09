#!/usr/bin/python3
# 8-uppercase.py


def uppercase(str):
    """Print a string in uppercase."""
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            a = chr(ord(a) - 32)
        print("{}".format(a), end="")
    print("")
