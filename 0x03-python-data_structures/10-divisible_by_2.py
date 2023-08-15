#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """identifies whether each integer in the input list is divisible by 2"""
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
