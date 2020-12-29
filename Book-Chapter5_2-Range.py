# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:57 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 5 Structured types, mutability and higher-order functions

Ranges

@author: Atanas Kozarev - github.com/ultraasi-atanas

RANGE the Theory

The range function takes three parameters - start, stop, step

Returns the progression of integers - start, start + step, start + step*2 etc

If step is positive, the last integer is the largest start + step*i smaller than stop

If step is negative, the last integer is the smallest integer start + step*i greater then stop

If two arguments are supplied, step is 1

If one argument is supplied, step is 1, stop is taken from arg, start is 0 

All of the operations on tuples apply on ranges, except concatenation and repetition
"""

rangeSlice = range(10)[2:6][2] # returns 4

print(rangeSlice)