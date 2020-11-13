# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:09 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 3 Finger Exercises

Write a program that prints the sum of the numbers in s = '1.23,2.4,3.123'

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""
s = '1.23,2.4,3.123'
floatNumChars = ''
sumFloats = 0
# until we finish the string we iterate
# each time we reach a comma, then we know it's a float-end.
# if the character is a comma, we do something:
# - we float() the number
# - and make the sum of the floats and clear the temp var

for c in s:
    if c == ',':
        # we convert, add to sum and wipe floatNumChars
        sumFloats += float(floatNumChars)
        floatNumChars = ''
    else:
        floatNumChars = floatNumChars + c

# somehow we miss the last number if we don't do this once, outside the loop
sumFloats += float(floatNumChars)
print(sumFloats)