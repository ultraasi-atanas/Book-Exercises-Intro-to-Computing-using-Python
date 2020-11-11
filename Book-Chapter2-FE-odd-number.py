#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 09:54:53 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 2 Finger Exercises - Find the largest odd number

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""

# edge cases 100, 2, 3 and 100,2,-3 and 2,2,2
x = 301
y = 2
z = 1

# what if the largest number is not odd? We need to discard any non-odd numbers

# if none of them are odd - go straight to else
if (x % 2 != 0) or (y % 2 != 0) or (z % 2 != 0):
    
    #codeblock if we have some odd numbers
    print("ok")
    
    # initialising the variable with one odd number, so we check each in turn
    if (x % 2 != 0):
        largest = x
    elif (y % 2 != 0):
        largest = y
    elif (z % 2 != 0):
        largest = z
        
        
    # here we check each against the largest
    # no need to check for x as we did already
        
    if (y % 2 != 0):
        if y > largest:
            largest = y
    
    if (z % 2 != 0):
        if z > largest:
            largest = z
    
    print("The largest odd number is:", largest)
    print("The numbers were", x, y, z)
        
else: 
    print("No odd number found")

