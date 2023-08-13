#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

def perform_calculations(a, b):
    """Print the sum, difference, multiple and quotient of a and b."""
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

    if __name__ == "__main__":
        a = 10
        b = 5
    perform_calculations(a, b)
