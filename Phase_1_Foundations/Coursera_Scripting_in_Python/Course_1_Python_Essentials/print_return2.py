#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 17:48:05 2025

@author: jnmlfc89009
"""

"""
Comparing print vs. return - version two
Print a string from inside a function call
"""

# def welcome(location):
#     """
#     Given a string location, print a string of the form
#     "Welcome to location"
#     """
#     answer = "Welcome to " + location
#     print(answer) #no "return" function, instead used print


# welcome("Python Scripting")

"""
Comparing print vs. return - version three
Print a string from inside a function call and
erroneously also print the returned result
"""

# def welcome(location):
#     """
#     Given a string location, print a string of the form
#     "Welcome to location"
#     """
#     answer = "Welcome to " + location
#     print(answer)


# print(welcome("Python Scripting")) #there is an extra print resulting and there was no return statement and the function execution stopped

def tricky():
    """ What does this function return? """
    return

print(tricky())