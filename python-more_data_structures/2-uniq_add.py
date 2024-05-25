#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    a = 0
    for i in range(len(my_list)):
        if not my_list[i] in new_list:
            a += my_list[i]
            new_list.append(my_list[i])
    return a
