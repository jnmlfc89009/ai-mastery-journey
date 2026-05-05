#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 17:13:20 2026

@author: jnmlfc89009
"""

"""
Template - Update an item in a list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here

example_list[2] = 0
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 0, 7, 11, 13]

#%%

"""
Template - Update a slice of a list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here

list1 = [0, 0, 0]
example_list[1:3] = list1
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 0, 0, 0, 7, 11, 13]

#%%

"""
Template - Append an item to a list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here

example_list.append(0)
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0]

#%%

"""
Template - Extend a list with another list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here

list1 = [0, 0, 0]
example_list.extend(list1)
print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]

#%%

"""
Template - Concatenate one list onto another
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here

new_list = list(example_list)
new_list.extend([0, 0, 0])

print(example_list)
print(new_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]

#%%

"""
Template - Append several item to a list
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
for number in [0, 0, 0]:
    example_list.append(number)

print(example_list)


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13, 0, 0, 0]

#%%

"""
Template - Convert a list to a tuple
"""

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
example_tuple = tuple(example_list)
    
print(example_tuple)


# Output
#[2, 3, 5, 7, 11, 13]
#(2, 3, 5, 7, 11, 13)

#%%

"""
Template - Shuffle the items in a list
"""
import random

example_list = [2, 3, 5, 7, 11, 13]
print(example_list)

# Enter update code here
random.shuffle(example_list)
print(example_list)


# Output - note that order of second list may vary due to randomness
#[2, 3, 5, 7, 11, 13]
#[11, 2, 7, 5, 13, 3]

#%%

"""
Template - Flatten a nested list
"""

def flatten(nested_list):
    """
    Given a list whose items are list, 
    return the list formed by joining all of these lists
    """
    
    list_item = []
    
    for sub_item in nested_list:
        
        for item in sub_item:
            
            list_item.append(item)
        
    return list_item

# Test code
print(flatten([]))
print(flatten([[]]))
print(flatten([[1, 2, 3]]))
print(flatten([["cat", "dog"], ["pig", "cow"]]))
print(flatten([[9, 8, 7], [6, 5], [4, 3, 2], [1]]))


# Output
#[]
#[]
#[1, 2, 3]
#['cat', 'dog', 'pig', 'cow']
#[9, 8, 7, 6, 5, 4, 3, 2, 1]

#%%

"""
Template - Flatten a nested list
"""

def flatten(nested_list):
    """
    Given a list whose items are list, 
    return the list formed by joining all of these lists
    """
    
    list_item = []
    
    for sub_item in nested_list:
        
        list_item.extend(sub_item)
        
    return list_item

# Test code
print(flatten([]))
print(flatten([[]]))
print(flatten([[1, 2, 3]]))
print(flatten([["cat", "dog"], ["pig", "cow"]]))
print(flatten([[9, 8, 7], [6, 5], [4, 3, 2], [1]]))


# Output
#[]
#[]
#[1, 2, 3]
#['cat', 'dog', 'pig', 'cow']
#[9, 8, 7, 6, 5, 4, 3, 2, 1]

#%%

"""
Template - Remove duplicates from a list while preserving the order of items
"""

myList = [1, 2, 3, 1, 2, 5, 6, 7, 8]
cleanlist = []
[cleanlist.append(x) for x in myList if x not in cleanlist]


def remove_duplicates(items):
    """
    Given a list, return a list with duplicate items removed
    and the remaining items in the same order
    """
    no_duplicates = []
    
    for item in items:
        if item not in no_duplicates:
            no_duplicates.append(item)
    
    return no_duplicates


# Test code
print(remove_duplicates([]))
print(remove_duplicates([1, 2, 3, 4]))
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5, 6, 6]))
print(remove_duplicates(["cat", "dog", "cat", "pig", "cow", "cat", "pig", "pug"]))


# Output
#[]
#[1, 2, 3, 4]
#[1, 2, 3, 4, 5, 6]
#['cat', 'dog', 'pig', 'cow', 'pug']

#%%

#Assignment Practices

# my_list = [1, 3, 5, 7, 9]

# print (my_list[2:4])
# print (my_list[1:4])
# print (my_list[1:-1])
# print (my_list[1:])

# # tup1 = (2)
# tup2 = ([1,2])
# tup3 = (1,)
# tup4 = (2,)

# # print (len(tup1))
# print (len(tup2))
# print (len(tup3))
# print (len(tup4))      

# instructors = ("Scott", "Joe", "John", "Stephen")
# instructors[2 : 4] = []
# print(instructors)

# my_list = [1, 3, 5, 7, 9]
# my_list.reverse()
# print(my_list)
# print(my_list.reverse())


# # Initial list
# fib = [0, 1]

# # Run the loop 10 times as requested
# for i in range(20):
#     # Calculate the sum of the last two items
#     next_value = fib[-1] + fib[-2]
    
#     # Add it to the end of the list
#     fib.append(next_value)

# # Print the final list and the last item
# print("Full List:", fib)
# print("Last Item:", fib[-1])

# """
# Implement the Sieve of Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# """

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    answer = list(range(2, bound))
    
    for divisor in range(2, bound):
        # Only process if the divisor hasn't been removed yet (it's prime)
        if divisor in answer:
            # Multiples start at divisor * 2 and go up to bound
            for multiple in range(divisor * 2, bound, divisor):
                if multiple in answer:
                    answer.remove(multiple)
    return answer

# Test code
print(len(compute_primes(200)))   # Output: 46
print(len(compute_primes(2000)))  # Output: 303

