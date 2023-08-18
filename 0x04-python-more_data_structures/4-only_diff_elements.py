#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
        diff_set = (set_1 - set_2) | (set_2 - set_1)
        set_1 = {1, 2, 3, 4, 5}
        set_2 = {3, 4, 5, 6, 7}
        return diff_set
