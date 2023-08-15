#!/usr/bin/python3
# Adds 2 tuples.

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = validate_tuple(tuple_a)
    tuple_b = validate_tuple(tuple_b)
    
    sum_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum_tuple

def validate_tuple(_tuple=()):
    if len(_tuple) < 2:
        _tuple = _tuple + (0,) * (2 - len(_tuple))
    elif len(_tuple) > 2:
        _tuple = _tuple[:2]
    
    return _tuple

