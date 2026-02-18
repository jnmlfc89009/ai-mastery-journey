#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 19:50:28 2025

@author: jnmlfc89009
"""

# def cube_root(val):
#     """
#     Given number, return the cube root of the number
#     """
#     return val ** (1 / 3)

# def max_of_2(val1, val2):
#     if val1 > val2:
#         return val1
#     else:
#         return val2

# def max_of_3(val1, val2, val3):
#     return max_of_2(val1, max_of_2(val2, val3))

# def project_to_distance(point_x, point_y, distance):
    
#     dist_to_origin = (point_x ** 2 + point_y ** 2) ** 0.5
   
#     scale = distance / dist_to_origin
    
#     print(point_x * scale, point_y * scale)

# project_to_distance(2, 7, 4)

# def do_stuff():
#     """
#     Example of print vs. return
#     """
#     print("Hello world")
#     return "Is it over yet?"
#     print("Goodbye cruel world!")

# print(do_stuff())

# def function(value):
    
#     answer = -5*(value**5) + 67*(value**2) - 47
    
#     return answer

# print(function(0))
# print(function(1))
# print(function(2))
# print(function(3))

# def future_value(present_value, annual_rate, periods_per_year, years):
#     """
#     Input: the numbers present_value, annual_rate, periods_per_year, years
#     Output: future value based on formula given in question
#     """
#     rate_per_period = annual_rate / periods_per_year
#     periods = periods_per_year * years

#     # Put your code here.
    
#     FV = present_value * (1+rate_per_period)**periods
    
#     return FV

# print("$1000 at 2% compounded daily for 4 years yields $", future_value(500, .04, 10, 10))
# print("$1000 at 2% compounded daily for 4 years yields $", future_value(1000, .02, 365, 4))

# import math Import math module for a potentially more precise sqrt, although 3**0.5 is fine too.

def equilateral_triangle_area(side_length):
  """
  Computes the area of an equilateral triangle given the length of one side.

  Args:
    side_length: The length of a side of the equilateral triangle.

  Returns:
    The area of the equilateral triangle.
  """
  # Using the formula: Area = (sqrt(3) / 4) * side^2
  # Using the hint's method for square root:
  area = (3**0.5 / 4) * (side_length**2)
  # Alternatively, using math.sqrt:
  # area = (math.sqrt(3) / 4) * (side_length**2)
  return area

# Test case provided: side length = 2
test_side = 2
test_area = equilateral_triangle_area(test_side)
print(f"Test: Area for side length {test_side} is {test_area}")
# Output should be close to 1.73205080757

# Calculate area for side length = 5
side = 5
calculated_area = equilateral_triangle_area(side)
print(f"Calculation: Area for side length {side} is {calculated_area}")

# Format the result for the final answer
formatted_area = f"{calculated_area:.7f}" # Format to 7 decimal places to ensure at least 4
print(f"Formatted area for side length {side}: {formatted_area}")