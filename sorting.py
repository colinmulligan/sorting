#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.
Every function in this file takes a comparator `cmp` as input which controls how the elements of the list should be compared against each other.
If cmp(a,b) returns -1, then a<b;
if cmp(a,b) returns  1, then a>b;
if cmp(a,b) returns  0, then a==b.
'''

import random

def cmp_standard(a,b):
    '''
    used for sorting from lowest to highest
    '''
    if a<b:
        return -1
    if b<a:
        return 1
    return 0


def cmp_reverse(a,b):
    '''
    used for sorting from highest to lowest
    '''
    if a<b:
        return 1
    if b<a:
        return -1
    return 0


def cmp_last_digit(a,b):
    '''
    used for sorting based on the last digit only
    '''
    return cmp_standard(a%10,b%10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.
    '''
    a = len(xs)
    b = len(ys)

    sorted_list = []
    j = 0
    k = 0

    while j < a and k < b:
        if (cmp == cmp_standard and xs[j] < ys[k]) or (cmp == cmp_reverse and xs[j] > ys[k]):
            sorted_list.append(xs[j])
            j += 1
        elif (cmp == cmp_standard and xs[j] >= ys[k]) or (cmp == cmp_reverse and xs[j] <= ys[k]):
            sorted_list.append(ys[k])
            k += 1

    if j == a and k == b:
        return sorted_list
    elif j == a:
        for x in range(k, b):
            sorted_list.append(ys[x])
        return sorted_list
    elif j == b:
        for x in range(i, a):
            sorted_list.append(xs[x])
        return sorted_list



def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:
        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves
    You should return a sorted version of the input list xs
    '''

    if len(xs) <= 1:
        return xs
    else:
        ctr = len(xs)//2
        left = xs[:ctr]
        right = xs[ctr:]

        merge_sorted(left, cmp)
        merge_sorted(right, cmp)

        return _merged(merge_sorted(left, cmp=cmp), merge_sorted(right, cmp=cmp), cmp = cmp)

def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected, 
    and the list is split into a "less than" sublist and a "greater than" sublist.
    The pseudocode is:
        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            sort both lists recursively
            return the concatenation of (less than, p, and greater than)
    You should return a sorted version of the input list xs
    '''

    low = []
    high = []
    equal = []

    if len(xs) <= 1: 
        return xs

    else:
        val = xs[0]
        for x in xs:
            if x > val:
                high.append(x)
            elif x < val:
                low.append(x)
            else:
                equal.append(x)

        lower = quick_sorted(low, cmp = cmp)
        higher = quick_sorted(high, cmp = cmp)

    if cmp == cmp_standard:
        return lower + equal + higher 

    if cmp == cmp_reverse:
        return higher + equal + lower
