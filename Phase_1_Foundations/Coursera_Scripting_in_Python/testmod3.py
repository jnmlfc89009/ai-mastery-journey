#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 18 10:45:58 2025

@author: jnmlfc89009
"""

# #Question 2

# p = False

# q = False

# print(not (p or not q))

# #Question 3

# bool1 = True
# bool2 = False

# print (not (bool1 == bool2))
# print (bool1 == bool2)
# print (bool1 != bool2)
# print (not bool1)

# #Question 4

# num1 = 100
# num2 = 99

# print (num1 >= num2)
# print (not (num1 < num2))
# print (not (num1 <= num2))
# print (num2 < num1)
# print ((num1 > num2) and (num1 != num2))

# #Question 6

# def nand(bool1, bool2):
#     """
#     Take two Boolean values bool1 and bool2
#     and return the specified Boolean values
#     """
    
#     if bool1:
#         if bool2:
#             return False
#         else:
#             return True
#     else:
#         return True
    
# bool1 = True
# bool2 = True

# print(nand(bool1, bool2))
# print (bool1 and bool2)
# print (bool1 or bool2)
# print (not (bool1 and bool2))
# print (not (bool1 or bool2))

#Question 7

def f(n):
  """
  Implements the core function of the Collatz conjecture.

  If n is even, returns n / 2 (integer division).
  If n is odd, returns 3*n + 1.

  Args:
    n: A positive integer.

  Returns:
    The result of applying the Collatz rule to n.
  """
  if n % 2 == 0:
    return n // 2
  else:
    return 3 * n + 1

# Test the implementation with the first expression: f(f(f(f(f(f(f(674)))))))
# Expected result: 190
result_674 = 674
result_674 = f(result_674) # 1
result_674 = f(result_674) # 2
result_674 = f(result_674) # 3
result_674 = f(result_674) # 4
result_674 = f(result_674) # 5
result_674 = f(result_674) # 6
result_674 = f(result_674) # 7

print(f"Result of f(f(f(f(f(f(f(674))))))): {result_674}")

# Compute the value of the expression f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071))))))))))))))
# This involves applying the function f 14 times to 1071.
result_1071 = 1071
result_1071 = f(result_1071) # 1
result_1071 = f(result_1071) # 2
result_1071 = f(result_1071) # 3
result_1071 = f(result_1071) # 4
result_1071 = f(result_1071) # 5
result_1071 = f(result_1071) # 6
result_1071 = f(result_1071) # 7
result_1071 = f(result_1071) # 8
result_1071 = f(result_1071) # 9
result_1071 = f(result_1071) # 10
result_1071 = f(result_1071) # 11
result_1071 = f(result_1071) # 12
result_1071 = f(result_1071) # 13
result_1071 = f(result_1071) # 14

print(f"Result of f applied 14 times to 1071: {result_1071}")