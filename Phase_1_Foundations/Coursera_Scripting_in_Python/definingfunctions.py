#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 16:53:23 2025

@author: jnmlfc89009
"""

"""
Demonstration of defining functions.
"""

def sayhello():
    """
    Prints "hello".
    """
    print("hello")

# Call the function
sayhello()
sayhello()

def double(value):
    """
    Return twice the input value
    """
    return value * 2

# # Call the function and assign the result to a variable
result = double(6)
print(result)

def product(value1, value2, value3):
    """
    Returns the product of the three input values.
    """
    prod = value1 * value2
    prod = prod * value3
    return prod

# Call the function and assign the result to a variable
result = product(7, 13, -2) * 54.4
print(result, result, result)