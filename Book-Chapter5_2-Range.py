# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:48 2020
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

The numbers of the progression are generated on an "as needed" basis, so even
expressions such as range(10000) consume little memory (Python3.x) 

The arguments of the range function are evaluated just before the first iteration
of the loop and not reevaluated for subsequent iteration

"""
# RANGE SLICE
rangeSlice = range(10)[2:6][2] # returns 4

print('RangeSlice of range(10)[2:6][2] is ', rangeSlice, '\n')

# RANGE COMPARISON
range2 = range(0,7,2)
range3 = range(0,8,2)

print('Range 2 is equal to Range 3?', range2 == range3)
print('Range 2 is', range2)
print('Range 3 is', range3)

print("Range2: ")
for e in range2: 
      print(e)
      
print("Range3:")
for e in range3:
    print(e)
      
      
# NEGATIVE STEP
range4 = range(40,-10,-10)
print('\n', 'Range4 is', range4)
for i in range4:
    print('\n', i)
    
    
# EXECUTING RANGE INSIDE A FOR LOOP
x = 5
for i in range(0,x):
    print(i)
    x = 8 # it doesnt change the range set in the loop condition



x = 5
y = range(0,x)
for i in y:
    print('\n', y)
    print(i)
    x = 8 # it doesnt change the range set in the loop condition



