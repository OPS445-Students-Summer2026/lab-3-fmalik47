#!/usr/bin/env python3

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(list_to_add):
    list_to_add.append(list_to_add[-1] + 1)
    return list_to_add

def remove_items_from_list(list_to_remove, items_to_remove):
    for item in items_to_remove:
        if item in list_to_remove:
            list_to_remove.remove(item)
    return list_to_remove
