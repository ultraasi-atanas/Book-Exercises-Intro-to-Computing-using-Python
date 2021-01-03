# -*- coding: utf-8 -*-
"""
Created on Sun Jan 03 2021 - 13:36
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 7 Exceptions and Assertions 

Exceptions as a Control Flow Mechanism

def findAnEven(L):
    '''Assumes L is a list of integers
        Returns the first even number in L
        Raises ValueError if L does not contain an even number
    '''
    

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""

def findAnEven(L):
    '''Assumes L is a list of integers
        Returns the first even number in L
        Raises ValueError if L does not contain an even number'''
# =============================================================================
#     
#     for elem in L:
#         if elem%2 == 0:
#             return elem
#         
#     raise ValueError("L does not contain an even number")
#    
# =============================================================================

# Internal exception handling but we could assume that's not needed, it will be handled
# at the level of which the function is being called
    try:
        for elem in L:
            if elem%2 == 0:
                return elem
        raise ValueError("L does not contain an even number")
    except ValueError as myerror:
        print("See this: ", myerror)

print(findAnEven([1,3,5]))