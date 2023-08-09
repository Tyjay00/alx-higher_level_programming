#!/usr/bin/python3
# 100-print_tebahpla.py
# Print the reversed alphabet with uppercase and lowercase characters.
# Initialize a variable `i` to control the alternating case.
# Loop through lowercase letters from 'z' to 'a' in reverse order.
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0
