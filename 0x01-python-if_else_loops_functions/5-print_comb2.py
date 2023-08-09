#!/usr/bin/python3

# Print numbers 0 to 99 with special formatting
for number in range(100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}, ".format(number), end="")
