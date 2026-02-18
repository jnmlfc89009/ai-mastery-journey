#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 17:27:54 2025

@author: jnmlfc89009
"""

# """ Define points (x0, y0) and (x1, y1) """

# x_0, y_0 = 2, 2

# x_1, y_1 = 5, 6

# print("First point is", x_0, y_0)
# print("Second point is", x_1, y_1)

""" Compute the distance between the points (x0, y0) and (x1, y1) """

def point_distance(x_0, y_0, x_1, y_1):
    """ Return distance between two points (x0,y0) and (x1,y1) """
    x_dist = x_0 - x_1
    y_dist = y_0 - y_1
    return (x_dist ** 2 + y_dist ** 2) ** 0.5

# Compute distance between (2, 2) and (5, 6). Should be 5.0
x_0, y_0 = 2, 2
x_1, y_1 = 5, 6
print(point_distance(x_0, y_0, x_1, y_1))