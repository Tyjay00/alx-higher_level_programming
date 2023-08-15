#!/usr/bin/python3
# This code effectively deletes an item at a specified index from a list, 
# if the index is within the valid range.

def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
