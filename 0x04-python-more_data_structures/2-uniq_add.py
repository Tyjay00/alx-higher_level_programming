#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    """adds all unique integers in a list """
    unique_sum = 0

    for i in uniq_list:
        unique_sum += i

    return (unique_sum)
