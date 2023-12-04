#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= len(element) or idex < 0:
        return my_list.copy()

    cp = my_list.copy()
    cp[idx] = element
    return cp
