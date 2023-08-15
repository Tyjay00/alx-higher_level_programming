#!/usr/bin/python3
# The function checks whether the index is valid 

def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    copy = [x for x in my_list]
    copy[idx] = element
    return (copy)
