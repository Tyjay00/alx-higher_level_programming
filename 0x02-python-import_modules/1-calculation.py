#!/usr/bin/python3

if __name__ == "__main__":
    """Display the add, sub, mul, and div results of values a and b."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, a + b))
    print("{} - {} = {}".format(a, b, a - b))
    print("{} * {} = {}".format(a, b, a * b))
    print("{} / {} = {}".format(a, b, a / b))
