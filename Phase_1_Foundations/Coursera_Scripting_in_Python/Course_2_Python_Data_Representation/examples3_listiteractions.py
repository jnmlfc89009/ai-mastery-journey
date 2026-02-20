#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 16:24:13 2026

@author: jnmlfc89009
"""

"""
Iterating over lists.
"""

def print_items(alist):
    """
    Iterate over alist and print all items.
    """
    for item in alist:
        print(item)

def print_items_bad(alist):
    """
    Iterate over alist and print all items.
    List indexing in this way is error prone and unnecessary.
    """
    length = len(alist)
    for index in range(length):
        print(alist[index])

def count_items(alist):
    """
    Count number of items in alist.
    """
    count = 0
    for item in alist:
        count = count + 1
    return count

def count_odd_items(numlist):
    """
    Count number of odd numbers in numlist.
    """
    count = 0
    for num in numlist:
        if num % 2 == 1:
            count += 1
    return count

numbers = list(range(5, 82, 3))
strings = ["python", "is", "fun", "!"]

print("Iterate over lists and print items")
print("")

# print_items(numbers)
# print_items(strings)
# print_items_bad(numbers)

print("")
print("Iterate over lists and process them")
print("")

# print(count_items(numbers))
# print(count_items(strings))
print(count_odd_items(numbers))

#%%

pets = ["cat", "dog", "ferret"]

for animal in pets:
    print(animal)
    
#%%    
numbers = [3, 8, -2, 4, 13]
sumsq = 0

for num in numbers:
    square = num * num
    sumsq += square
    
print(sumsq)

#%%

numbers = [3, 8, -2, 4, 13]
sumsq = 0

# The "Pro" version of your code:
print(sum(n**2 for n in numbers))