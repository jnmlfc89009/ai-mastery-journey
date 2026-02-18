#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 17:42:23 2025

@author: jnmlfc89009
"""

"""
Comparing print vs. return - version one
Return a string from a function that is printed outside the function
"""

def welcome(location):
    """
    Given a string location, return a string of the form
    "Welcome to location"
    """
    answer = "Welcome to " + location
    return answer
    print("Free your mind") #This is not executred because "return" has terminated the function


print(welcome("the Matrix"))