#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = []
    for i in range(len(set_1)):
        if i in set_2:
            new_set.append(set_1[i])
    return new_set
