# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:57 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 5 Structured types, mutability and higher-order functions

Functions as Objects, Higher Order Functions, higher-order programming

In Python, functions are a first class object, like int or list
Functions can appear in expressions, as an argument to a funtion, elements of lists

type(abs) has value <class 'built-in_function_or_method'

type(myFunction) has value <class 'function'>



@author: Atanas Kozarev - github.com/ultraasi-atanas

"""

def myFunction(a,b):
    return a + b

def myFunction2(a,b):
    return a + b

print(type(abs))
print(type(myFunction))
print(type(myFunction2) == type(myFunction)) # That yields True

# RANDOM
print('') # found the apple symbol! 

def applyToEach(L,f):
    """Assumes L is a list, f a function
    Mutates L by replacing each element, e, of L by f(e)
    """
    for i in range(len(L)):
        L[i] = f(L[i])
        
L = [1, -2, 3.33]
print('L is', L)
print('Apply abs to each element of L.')
applyToEach(L,abs)
print('L is', L)
print('Apply int to each element of L.')
applyToEach(L,int)
print('L is', L)

