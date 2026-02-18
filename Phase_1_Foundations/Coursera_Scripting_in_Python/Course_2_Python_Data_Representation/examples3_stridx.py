#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 14:34:46 2026

@author: jnmlfc89009
"""

"""
String indexing examples.
"""

phrase = "Python is great!"

# first character
print(phrase[10])

# fourth character
fourth = phrase[3]
print(fourth)
print(type(phrase))
print(type(fourth))

# length of string
phraselen = len(phrase)
print(phraselen)

# last character
print(phrase[phraselen - 1])
print(phrase[-1])

# thirteenth from last (fourth) character
print(phrase[-13])

# # Out of bounds
# print(phrase[phraselen])
# print(phrase[-20])

# Indices
# string = "abcde"
# character   a  b  c  d  e
# pos index   0  1  2  3  4
# neg index  -5 -4 -3 -2 -1