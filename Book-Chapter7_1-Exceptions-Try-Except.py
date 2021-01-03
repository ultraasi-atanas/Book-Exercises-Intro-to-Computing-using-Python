# -*- coding: utf-8 -*-
"""
Created on Sun Jan 03 2021 - 11:55
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 7 Exceptions and Assertions 

Try, except

Finger exercise - Implement  а function that meets the specification 
using a try-except block

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""

def sumDigits(s):
    """ Assumes s is a string
        Returns the sum of the decimal digits in s
        For example, if s is 'a2b3c' it returns 5"""
        
    sum = 0
    letters = 0

    for char in s:
        try:
            d = int(char) # throws ValueError: invalid literal for int() with base 10: 'a'
            sum += d
        except:
            letters = letters + 1
     
# =============================================================================
#     # Debug
#     print(sum)
#     print(letters)
#     
# =============================================================================
    return sum
        

print(sumDigits("a2b3c"))