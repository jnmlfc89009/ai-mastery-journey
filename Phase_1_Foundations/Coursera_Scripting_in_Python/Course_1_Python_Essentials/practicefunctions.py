#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 17:56:12 2025

@author: jnmlfc89009
"""

"""
Template - Compute the number of feet corresponding to a number of miles.
"""
# ##Practice 1##
# ###################################################
# # Miles to feet conversion formula
# # Student should enter function on the next lines.

# def miles_to_feet(num_miles1):
#     """
#     Returns the number of feet in the given number of miles.
#     """
    
#     feet = num_miles1 * 5280
#     return feet

# ###################################################
# # Tests
# # Student should not change this code.


# miles = 13
# print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")
    
# miles = 57
# print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")

# miles = 82.67
# print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")


# ###################################################
# # Expected output
# # Student should look at the following comments and compare to printed output.

# #13 miles equals 68640 feet.
# #57 miles equals 300960 feet.
# #82.67 miles equals 436497.6 feet.

# ##Practice 2##

# """
# Template - Compute the number of seconds in a given number of hours, minutes, and seconds.
# """

# ###################################################
# # Hours, minutes, and seconds to seconds conversion formula
# # Student should enter function on the next lines.

# def total_seconds(hours,minutes,seconds):
    
#     """Returns the total number of seconds for hours, minutes and second"""
    
#     seconds_hours = hours * 3600
#     seconds_minutes = minutes * 60
#     total_seconds = seconds_hours + seconds_minutes + seconds
    
#     return total_seconds

# ###################################################
# # Tests
# # Student should not change this code.

# hours, minutes, seconds = 7, 21, 37
# print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
#       str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
#       " seconds.")

# hours, minutes, seconds = 10, 1, 7
# print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
#       str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
#       " seconds.")

# hours, minutes, seconds = 1, 0, 1
# print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
#       str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
#       " seconds.")

# ###################################################
# # Expected output
# # Student should look at the following comments and compare to printed output.

# #7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.
# #10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.
# #1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.

# ##Practice 3##

# """
# Template - Compute the length of a rectangle's perimeter, given its width and height.
# """

# ###################################################
# # Rectangle perimeter formula
# # Student should enter function on the next lines.

# def rectangle_perimeter(width,height):
    
#     """Returns perimeter of rectangle in inches"""
    
#     side1 = width * 2
#     side2 = height * 2
#     perimeter = side1 + side2
    
#     return perimeter


# ###################################################
# # Tests
# # Student should not change this code.


# width, height = 4, 7
# print("A rectangle " + str(width) + " inches wide and " + str(height) + 
#       " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

# width, height = 7, 4
# print("A rectangle " + str(width) + " inches wide and " + str(height) + 
#       " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")

# width, height = 10, 10
# print("A rectangle " + str(width) + " inches wide and " + str(height) + 
#       " inches high has a perimeter of " + str(rectangle_perimeter(width, height)) + " inches.")


# ###################################################
# # Expected output
# # Student should look at the following comments and compare to printed output.

# #A rectangle 4 inches wide and 7 inches high has a perimeter of 22 inches.
# #A rectangle 7 inches wide and 4 inches high has a perimeter of 22 inches.
# #A rectangle 10 inches wide and 10 inches high has a perimeter of 40 inches.

# ##Practice 4##

# """
# Template - Compute the area of a rectangle, given its width and height.
# """

# ###################################################
# # Rectangle area formula
# # Student should enter function on the next lines.

# def rectangle_area(width,height):
    
#     """ Returns the area of the rectangle in square inches"""
    
#     area = width * height
    
#     return area


# ###################################################
# # Tests
# # Student should not change this code.

# width, height = 4, 7
# print("A rectangle " + str(width) + " inches wide and " + str(height) + 
#       " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")
    
# width, height = 7, 4
# print("A rectangle " + str(width) + " inches wide and " + str(height) + 
#       " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

# width, height = 10, 10
# print("A rectangle " + str(width) + " inches wide and " + str(height) + 
#       " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

    
# ###################################################
# # Expected output
# # Student should look at the following comments and compare to printed output.

# #A rectangle 4 inches wide and 7 inches high has an area of 28 square inches.
# #A rectangle 7 inches wide and 4 inches high has an area of 28 square inches.
# #A rectangle 10 inches wide and 10 inches high has an area of 100 square inches.

# ##Practice 5##

# """
# Template - Compute the circumference of a circle, given the length of its radius.
# """

# import math
# PI = math.pi

# ###################################################
# # Circle circumference formula
# # Student should enter function on the next lines.

# def circle_circumference(radius):
    
#     """Returns the the circumference of a circle with radius in inches"""
    
#     circle_circum = 2 * PI * radius
    
#     return circle_circum

# ###################################################
# # Tests
# # Student should not change this code.

# radius = 8
# print("A circle with a radius of " + str(radius) + 
#       " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

# radius = 3
# print("A circle with a radius of " + str(radius) + 
#       " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

# radius = 12.9
# print("A circle with a radius of " + str(radius) + 
#       " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")


# ###################################################
# # Expected output
# # Student should look at the following comments and compare to printed output.

# #A circle with a radius of 8 inches has a circumference of 50.2654824574 inches.
# #A circle with a radius of 3 inches has a circumference of 18.8495559215 inches.
# #A circle with a radius of 12.9 inches has a circumference of 81.0530904626 inches.

# ##Practice 6 ##

# """
# Template - Compute the area of a circle, given the length of its radius.
# """

# # Import the math module to access the exact value of pi
# import math
# PI = math.pi

# ###################################################
# # Circle area formula
# # Student should enter function on the next lines.

# def circle_area(radius):
    
#     """Returns the the area of a circle with radius in squared inches"""
    
#     area_circle = PI * (radius ** 2)
    
#     return area_circle

# ###################################################
# # Tests
# # Student should not change this code.

# radius = 8
# print("A circle with a radius of " + str(radius) + 
#       " inches has an area of " + str(circle_area(radius)) + 
#       " square inches.")

# radius = 3
# print("A circle with a radius of " + str(radius) + 
#       " inches has an area of " + str(circle_area(radius)) + 
#       " square inches.")

# radius = 12.9
# print("A circle with a radius of " + str(radius) + 
#       " inches has an area of " + str(circle_area(radius)) + 
#       " square inches.")


# ###################################################
# # Expected output
# # Student should look at the following comments and compare to printed output.

# #A circle with a radius of 8 inches has an area of 201.06192983 square inches.
# #A circle with a radius of 3 inches has an area of 28.2743338823 square inches.
# #A circle with a radius of 12.9 inches has an area of 522.792433484 square inches.

# ##Practice 7##

# """
# Template - Compute the future value of a given present value, annual rate, and number of years.
# """

# ###################################################
# # Future value formula
# # Student should enter function on the next lines.

# def future_value(present_value,annual_rate, years):
    
#     """Returns the future value of present value of dollars invested at annual rate percent interest, compounded annually for years"""
    
#     FV = present_value * (1 + annual_rate/100)** years
    
#     return FV


# ###################################################
# # Tests
# # Student should not change this code.


# present_value, annual_rate, years = 1000, 7, 10	
# print("The future value of $" + str(present_value) + " in " + str(years) + 
#       " years at an annual rate of " + str(annual_rate) + "% is $" + 
#       str(future_value(present_value, annual_rate, years)) + ".")
    
# present_value, annual_rate, years = 200, 4, 5
# print("The future value of $" + str(present_value) + " in " + str(years) + 
#       " years at an annual rate of " + str(annual_rate) + "% is $" + 
#       str(future_value(present_value, annual_rate, years)) + ".")

# present_value, annual_rate, years = 1000, 3, 20
# print("The future value of $" + str(present_value) + " in " + str(years) + 
#       " years at an annual rate of " + str(annual_rate) + "% is $" + 
#       str(future_value(present_value, annual_rate, years)) + ".")


# ###################################################
# # Expected output
# # Student should look at the following comments and compare to printed output.

# #The future value of $1000 in 10 years at an annual rate of 7% is $1967.15135729.
# #The future value of $200 in 5 years at an annual rate of 4% is $243.33058048.
# #The future value of $1000 in 20 years at an annual rate of 3% is $1806.11123467.

# ##Practice 8##

# """
# Template - Compute a name tag, given the first and last name.
# """

# ###################################################
# # Name tag formula
# # Student should enter function on the next lines.

# def name_tag(first_name,last_name):
    
#     """
#     Returns the name tag, given the first and last name.
#     """
    
#     return "My name is " + first_name + " " + last_name
    
# ###################################################
# # Tests
# # Student should not change this code.
    
    
# first_name, last_name = "Joe", "Warren"
# print(name_tag(first_name, last_name))

# first_name, last_name = "Scott", "Rixner"
# print(name_tag(first_name, last_name))

# first_name, last_name = "John", "Greiner"
# print(name_tag(first_name, last_name))


# ###################################################
# # Expected output
# # Student should look at the following comments and compare to printed output.

# #My name is Joe Warren.
# #My name is Scott Rixner.
# #My name is John Greiner.

# ##Practice 9##

# """
# Template - Compute the statement about a person's name and age, given the person's name and age.
# """

# ###################################################
# # Name and age formula
# # Student should enter function on the next lines.

# def name_and_age(name,age):
    
#     """Compute the statement about a person's name and age, given the person's name and age."""
    
#     age = str(age)
    
#     return name + " is " + age + " years old."

# ###################################################
# # Tests
# # Student should not change this code.

    
# name, age = "Joe Warren", 56
# print(name_and_age(name, age))

# name, age = "Scott Rixner", 40
# print(name_and_age(name, age))

# name, age = "John Greiner", 46
# print(name_and_age(name, age))


# ###################################################
# # Expected output
# # Student should look at the following comments and compare to printed output.

# #Joe Warren is 56 years old.
# #Scott Rixner is 40 years old.
# #John Greiner is 46 years old.

##Practice 10##

# """
# Template - Compute the distance between the points (x0, y0) and (x1, y1).
# """

###################################################
# Distance formula
# Student should enter function on the next lines.

# Hint: You need to use the power operation ** .

# def point_distance(x_0,y_0,x_1,y_1):
    
#     """
#     Template - Compute the distance between the points (x0, y0) and (x1, y1).
#     """
    
#     dist_point1 = (x_0 - x_1) ** 2
#     dist_point2 = (y_0 - y_1) ** 2
#     PD = (dist_point1 + dist_point2) ** 0.5
    
#     return PD


# ###################################################
# # Tests
# # Student should not change this code.


# x_0, y_0, x_1, y_1 = 2, 2, 5, 6
# print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
#       str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")

# x_0, y_0, x_1, y_1 = 1, 1, 2, 2
# print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
#       str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")

# x_0, y_0, x_1, y_1 = 0, 0, 3, 4
# print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
#       str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")


# ###################################################
# # Expected output
# # Student should look at the following comments and compare to printed output.

# #The distance from (2, 2) to (5, 6) is 5.0.
# #The distance from (1, 1) to (2, 2) is 1.41421356237.
# #The distance from (0, 0) to (3, 4) is 5.0.

# ##Practice 11##

# """
# Template - Compute the area of a triangle (using Heron's formula),
#     given its side lengths.
# """

# ###################################################
# # Triangle area (Heron's) formula
# # Student should enter function on the next lines.
# # Hint:  Use point_distance as a helper function.

# def point_distance(x_0,y_0,x_1,y_1):
    
#     """
#     Returns the Euclidian distance between two points (x0,y0) and (x1,y1).
#     """
    
#     dist_point1 = (x_0 - x_1) ** 2
#     dist_point2 = (y_0 - y_1) ** 2
#     PD = (dist_point1 + dist_point2) ** 0.5
    
#     return PD

# def triangle_area(x_0, y_0, x_1, y_1, x_2, y_2):
    
#     """
#     Returns the area of a triangle with vertices (x0,y0), (x1,y1), and (x2,y2). Heron's formula
#     """
#     # Compute the lengths of the three sides.
#     dista = point_distance(x_0,y_0,x_1,y_1)
#     distb = point_distance(x_0,y_0,x_2,y_2)
#     distc = point_distance(x_1,y_1,x_2,y_2)
    
#     # Compute the semi-perimeter length, i.e., half of the perimeter length.
#     s = (dista + distb + distc)/2
    
#     # Compute the area according to Heron's formula.
#     area = (s * (s-dista) * (s-distb) * (s-distc)) ** 0.5
    
#     return area


# ###################################################
# # Tests
# # Student should not change this code.

# def test(x_0, y_0, x_1, y_1, x_2, y_2):
#     """Tests the triangle_area function."""
    
#     print("A triangle with vertices (" + str(x_0) + "," + str(y_0) + "),")
#     print("(" + str(x_1) + "," + str(y_1) + "), and")
#     print("(" + str(x_2) + "," + str(y_2) + ") has an area of")
#     print(str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

# x_0, y_0, x_1, y_1, x_2, y_2 = 0, 0, 3, 4, 1, 1
# print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
#       str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
#       ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

# x_0, y_0, x_1, y_1, x_2, y_2 = -2, 4, 1, 6, 2, 1
# print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
#       str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
#       ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

# x_0, y_0, x_1, y_1, x_2, y_2 = 10, 0, 0, 0, 0, 10
# print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
#       str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
#       ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")


# ###################################################
# # Expected output
# # Student should look at the following comments and compare to printed output.

# #A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
# #A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
# #A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.

# ##Practice 12##

# """
# Template - Compute and print tens and ones digit of an integer in [0,100).
# """

# ###################################################
# # Digits function
# # Student should enter function on the next lines.

# def print_digits(value):
    
#     """Compute and print tens and ones digit of an integer in [0,100)."""
    
#     tens_01 = str(value // 10)
#     ones_01 = str(value % 10)
    
#     message = "The tens digit is " + tens_01 + ", and the ones digit is " + ones_01 + "."
    
#     return print(message)
    
# ###################################################
# # Tests
# # Student should not change this code.
    
# print_digits(42)
# print_digits(99)
# print_digits(5)


# ###################################################
# # Expected output
# # Student should look at the following comments and compare to printed output.

# #The tens digit is 4, and the ones digit is 2.
# #The tens digit is 9, and the ones digit is 9.
# #The tens digit is 0, and the ones digit is 5.


##Practice 13##

"""
Solution - Compute and print powerball numbers.
"""

import random

###################################################
# Powerball function
# Student should enter function on the next lines.

def powerball():
    """
    Prints Powerball lottery numbers.
    """
    
    # Note that including the optional argument end = "" to print() cause
    # print to NOT generate a newline
    
    print("Today's numbers are " + str(random.randrange(1, 60)) + ", ", end = "")
    print(str(random.randrange(1, 60)) + ", ", end = "")
    print(str(random.randrange(1, 60)) + ", ", end = "") 
    print(str(random.randrange(1, 60)) + ", and ", end = "")
    print(str(random.randrange(1, 60)) + ". The Powerball number is ",  end = "") 
    print(str(random.randrange(1, 36)) + ".")

    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()

###################################################################
# Some sample output appears below.  Note that numbers need not match
#Today's numbers are 46, 25, 49, 54, and  8. The Powerball number is 26.
#Today's numbers are 14, 11, 17, 6, and  30. The Powerball number is 16.
#Today's numbers are 58, 59, 39, 2, and  29. The Powerball number is 19.
