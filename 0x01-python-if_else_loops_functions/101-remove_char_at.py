#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(s, n):
    """    
    Create a new string from the input string.
    :@ s: The input string from which the character should be removed.
    :@ n: The index of the character to be removed.
    :return: A new string with the specified character removed.
    """
    if n < 0 or n >= len(s):
        return s[:n] + s[n + 1:]
