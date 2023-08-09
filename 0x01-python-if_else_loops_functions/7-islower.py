#!/usr/bin/python3
# 7-islower.py

def islower(c):
    """Check if the given character is lowercase."""
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
