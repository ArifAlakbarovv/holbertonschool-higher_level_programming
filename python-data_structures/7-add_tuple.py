#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    if len(tuple_a) >= 2:
        a += tuple_a[0]
        b += tuple_a[1]
    elif len(tuple_a) == 1:
        a += tuple_a[0]
    if len(tuple_b) >= 2:
        a += tuple_b[0]
        b += tuple_b[1]
    elif len(tuple_b) == 1:
        a += tuple_b[0]
    tuple = (a, b)
    return tuple
