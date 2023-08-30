#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

	Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

	Returns:
        The number of elements printed.
    """
    print("".join(map(str, my_list[:x])))
    return min(len(my_list), x)
