#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 17:11:52 2025

@author: jnmlfc89009
"""

def sum_of_squares(num1, num2):
    """
    Return the sum of the squares of the two inputs.
    """
    sq1 = num1 * num1
    sq2 = num2 * num2
    sumsq = sq1 + sq2
    return sumsq

number = 3
value = sum_of_squares(number, 5)
print(value)