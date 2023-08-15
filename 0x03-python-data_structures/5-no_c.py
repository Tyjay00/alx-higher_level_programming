#!/usr/bin/python3
# Removing the specified characters from the input string.

def no_c(my_string):
    """Remove all characters c and C from a string."""
    new_string = ''.join([char for char in my_string if char.lower() != 'c'])
    return new_string

