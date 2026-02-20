#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 15:52:09 2026

@author: jnmlfc89009
"""

"""
List indexing and slicing.
"""

# print("List Indexing")
# print("=============")

# groceries = ["butter", "milk", "bacon", "spaghetti", "asparagus"]
# print(groceries)

# # first item
# print(groceries[0])

# # third item
# print(groceries[2])

# # length of list
# numitems = len(groceries)
# print(numitems)

# # last item
# print(groceries[-1])
# print(groceries[numitems - 1])

# # third from last item
# print(groceries[-3])

# # Out of bounds
# print(groceries[numitems])
# print(groceries[-17])

# Indices
# list = [7, 8, 3, 2, 9, 4]
# item        7  8  3  2  9  4
# pos index   0  1  2  3  4  5
# neg index  -6 -5 -4 -3 -2 -1

print("")
print("List Slicing")
print("============")

numbers = list(range(72, 5, -12))
print(numbers)

# Sublists
print(numbers[2:3])
print(numbers[1:4])

# Open ended slices
print(numbers[1:])
print(numbers[:3])

# Using negative indices
print(numbers[-2:])
print(numbers[1:-4])

# Empty slices
print(numbers[3:2])
print(numbers[10:12])

#%%

lst1 = [1, 5, 9, -32]
print(lst1)

lst2 = ["dog", "cow", "horse"]
print(lst2)

emptylst = []
print(emptylst)

#%%

lst = list(range(10))

# First element
print(lst[0])

# Third element
print(lst[2])

# Length
print(len(lst))

# Last element
print(lst[9])
print(lst[len(lst) - 1])
print(lst[-1])


#%%

lst = list(range(10))

print(lst)

# Slice with 3 elements
print(lst[4:7])

# Slice with the last 2 elements of the list
print(lst[8:10])
print(lst[8:])
print(lst[-2:])

# Slice with the first 4 elements of the list
print(lst[0:4])
print(lst[:4])

# Empty slices
print(lst[20:25])
print(lst[7:3])
