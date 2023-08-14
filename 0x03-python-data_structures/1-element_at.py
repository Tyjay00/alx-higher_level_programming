#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieve an element from a list at a given index."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
