#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
        """takes a dictionary and a key as input"""
    return (a_dictionary)
