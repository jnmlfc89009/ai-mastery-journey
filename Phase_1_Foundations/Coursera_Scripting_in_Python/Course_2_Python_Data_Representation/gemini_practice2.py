#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 22:15:17 2026

@author: jnmlfc89009
"""

def process_lego_inventory(my_sets):
    """
    Takes a list of LEGO set names, removes duplicates, 
    and returns a sorted list.
    """
    # Step 1: Remove duplicates
    unique_sets = list(set(my_sets))
    
    # Step 2: Sort them alphabetically
    sorted_inventory = unique_sets.sort()
    
    # Step 3: Add a header for the video
    print("MY LEGO COLLECTION:")
    
    return sorted_inventory

# Testing the code

collection = ["Hogwarts", "Dobby", "Hogwarts", "X-Wing"]

final_list = process_lego_inventory(collection)

print(final_list)