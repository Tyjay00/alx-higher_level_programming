#!/usr/bin/python3
# Retrive an element from a list

def element_at(my_list, index):
    if index >= 0 or index >(len(my_list) - 1):
        return None
    return (my_list[index])
