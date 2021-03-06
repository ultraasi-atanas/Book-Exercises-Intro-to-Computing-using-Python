# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:38 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 5 Structured types, mutability and higher-order functions

List Comprehension

Provides a conscise way to apply an operation to the values in a sequence. 
It creates a new list. 

A word of warning:
"Some Python programmers use list comprehension in marvelous and subtle ways.
That is not always a great idea. Remember that somebody else may need to 
read your code, and 'subtle' is not usually a desired property"

@author: Atanas Kozarev - github.com/ultraasi-atanas

"""

L = [x**2 for x in range(10)]
print('L = [x**2 for x in range(10)]')
print('L is :', L)

L2 = [x**2 for x in range(10) if x%2 == 0]
print('L2 = [x**2 for x in range(10) if x%2 == 0]')
print('L2 is :', L2)

L3 = []
for x in range(1000):
    if x%2 == 0:
        L3.append(x**2)
print('L3 is -- see code')
print('L3[:10] is :', L3[:10])

L4mixed = [1,2,3,'a','b','c',5.0]
print('L4mixed is :', L4mixed)
print('e**2 for e in L4mixed if type(e)== int] is :', [e**2 for e in L4mixed if type(e)== int])