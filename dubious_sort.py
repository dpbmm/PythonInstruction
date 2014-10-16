#! /usr/bin/env python3
# dubious_sort.py
# 20141015
# David Prager Branner

"""Implement quicksort, but if broken=True then do not sort correctly."""

import random

def sort(the_list, broken=False):
    '''Quicksort: choose pivot, divide as > or <= pivot; call recursively.'''
    # Recursion returns
    if not the_list:
        return the_list
    #
    # Divide, using the_list[0] as pivot
    # Note: no particular speed improvement using array.array instead of list.
    first_half = []
    second_half = []
    for item in the_list[1:]:
        if item < the_list[0]:
            first_half.append(item)
        else:
            second_half.append(item)
    #
    # Recursive call and recombination
    if broken:
        # Wreck the sort
        random.shuffle(the_list)
        # In case we accidentally shuffled it into sorted order:
        while the_list == sorted(the_list):
            random.shuffle(the_list)
        return the_list
    return (sort(first_half, broken) +
            list([the_list[0]]) +
            sort(second_half, broken))
