#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 16:52:47 2026

@author: jnmlfc89009
"""

import sys

# 1. Create a list of SGX stocks
my_stocks = ["DBS", "OCBC", "UOB"]

# 2. Add two more name tags
portfolio = my_stocks
watchlist = my_stocks

# 3. Move one name tag to something else
watchlist = ["Apple", "Google"]

# 4. Remove one name tag entirely
del portfolio

# FINAL CHECK:
# How many "tags" are left on the original ["DBS", "OCBC", "UOB"] list?
# (Remember: sys.getrefcount adds 1 temporary tag for itself)
print(sys.getrefcount(my_stocks))

list_a = [1, 2, 3]
list_b = list_a
print(list_a is list_b)  # True (Same bucket)

list_b = [4, 5, 6]
print(list_a is list_b)  # False (list_b moved to a new house!)