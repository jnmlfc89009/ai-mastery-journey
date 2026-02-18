#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 17 17:41:14 2025

@author: jnmlfc89009
"""

"""
Demonstration of if statements.
"""

def greet(friend, money):
    """
    Greet people.  Say hi if they are your friend and give them
    $20 if you have enough money.
    """
    if friend:
        print("Hi!")

    if money > 20:
        money = money - 20

    return money


money = 100

money = greet(False, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()