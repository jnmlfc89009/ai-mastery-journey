#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 14:31:55 2026

@author: jnmlfc89009
"""

"""
Template- Create a list of the first six primes and print the 2nd, 4th, and 6th
"""

# Enter code here

primelist = (2, 3, 5, 7, 11, 13)

print(primelist[1], primelist[3], primelist[5])

pass

# Output
#3 7 13

#%%

"""
Template - Create a list formed by the first and last items of example_list
"""

example_list = [2, 3, 5, 7, 11, 13]

# Uncomment and complete

firstlast_list = [example_list[0], example_list[-1]]
print(firstlast_list)


# Output
#[2, 13]

#%%

"""
Template - Create a list formed by excluding the first and last items of example_list
"""

# Enter code here

example_list = [2, 3, 5, 7, 11, 13]

# Uncomment and complete
middle_list = example_list[1:-1]
print(middle_list)


# Output
#[3, 5, 7, 11]

#%%

"""
Template - Create a list formed by 8 copies of True and 8 copies of False
"""

# Uncomment and enter code here

truefalse_list = 8 * [True] + 8 * [False]
print(truefalse_list)


# Output
#[True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False]

#%%

"""
Template - Create a list of words form a string consisting of words separated by spaces
"""

# Uncomment and enter code here

quote = "Bring me a shrubbery"
word_list = quote.split()
print(word_list)


# Output
#['Bring', 'me', 'a', 'shrubbery']

#%%

"""
Template - Count the number of times that a word appears in string of text
"""

def word_count(text, word):
    """
    Given a string text consist of words separate by spaces and a string word
    (with no spaces), return the number of times that word appears in the text
    """
    
    word_list = text.split(" ")
    return word_list.count(word)


# Tests

print(word_count("this pigdog is a fine pigdog", "pigdog"))
print(word_count("this pigdog is not a dog", "dog"))
print(word_count("this pigdog is not a pig", "pigdog"))

# Output
#2
#1
#1

#%%

"""
Template - Analyze an example of a list reference situation
"""

# Initial list
list1 = [2, 3, 5, 7, 11, 13]

# Another reference to list1
list2 = list1

# Print out both lists
print(list1)
print(list2)

# Update the first item in second list to zero
list2[0] = 0

# Print out both lists
print(list1)
print(list2)
print(id(list1))
print(id(list2))

# Explain what happens to list1 in a comment

# Answer - list1 and list2 are references to the same list
# Updating an item in one list mutates the other list


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[0, 3, 5, 7, 11, 13]
#[0, 3, 5, 7, 11, 13]

#%%

"""
Template - Analyze another example of a list reference situation
"""

# Initial list
list1 = [2, 3, 5, 7, 11, 13]

# Make a copy of list1
list2 = list(list1)

# Print out both lists
print(list1)
print(list2)

# Update the first item in second list to zero
list2[0] = 0

# Print out both lists
print(list1)
print(list2)
print(id(list1))
print(id(list2))

# Explain what happens to list1 in a comment

# Answer - list1 and list2 are two references to distinct lists
# Updating an item in one list does not affect the second list


# Output
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[2, 3, 5, 7, 11, 13]
#[0, 3, 5, 7, 11, 13]

#%%

"""
Template - Compute the largest number in a list
"""

def list_max(numbers):
    """
    Given a list of numbers, return the maximum (largest) number
    in the list
    """
    
    max_num = numbers[0]
    
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
            
    return max_num


# Tests
print(list_max([4]))
print(list_max([-3, 4]))
print(list_max([5, 3, 1, 7, -3, -4]))
print(list_max([1, 2, 3, 4, 5]))


# Output
#4
#4
#7
#5

#%%

"""
Template - Take a list of integers and concatenate their digits
"""

def concatenate_ints(int_list):
    """
    Given a list of integers int_list, return the integer formed by
    concatenating their decimal digits together
    """
    
    value1 = ""
    
    for value2 in int_list:
        value1 += str(value2)
        
    return int(value1)
    
    
    pass

# Tests
print(concatenate_ints([4]))
print(concatenate_ints([4, 0, 4]))
print(concatenate_ints([123, 456, 789]))
print(concatenate_ints([32, 796, 1000]))


# Output
#4
#404
#123456789
#327961000

#%%

#Quiz Usages

# print (list(range(6)))
# print (list(range(0,5,1)))
# print (range(6))
# print (list(range(0,6)))

# my_list = ["This", "course", "is", "great"]
# print (len(my_list))
# print (my_list[3])

# my_list = ["This", "course", "is", "really", "great"]

# print (my_list[0: len(my_list) // 2-1])
# print (my_list[len(my_list) // 2 : len(my_list)])

# m = 14
# n = 20
       
# init_list = list(range(1, n))
# final_list = init_list * m

# print (len(final_list))

# n = 20

# test_string = "xxx" + " " * n + "xxx"
# split_list = test_string.split(" ")

# print (len(split_list))

# list1 = list(range(1, 10))
# list2 = [] + list1

# print (id(list1))
# print (id(list2))

# def strange_sum(numbers):
    
#     """ 
#     Write a function strange_sum(numbers) that takes a list of integers 
#     and returns the sum of those items in the list that are
#     not divisible by 3. When you are done, test your function using the code snippet below.
#     """
#     total = 0
    
#     for num in numbers:
#         if num % 3 != 0:
#             total += num
            
#     return total

# print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
# print(strange_sum(list(range(123)) + list(range(77))))
            
            
    
    
    
    
    
    
    
    
    
    
    

