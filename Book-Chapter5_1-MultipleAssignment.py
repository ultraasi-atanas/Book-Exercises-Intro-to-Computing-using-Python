# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 09:25 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 5 Structured types, mutability and higher-order functions

Multiple Assignment

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""


def findExtremeDivisors(n1,n2):
    """ Assumes that n1 and n2 are positive ints
        Returns a tuple containing the smallest common divisor > 1 and
        the largest common divisor of n1 and n2. If no common divisor, 
        returns (None, None) """
        
    minVal, maxVal = None, None
    for i in range (2,min(n1,n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return (minVal,maxVal)

minDivisor, maxDivisor = findExtremeDivisors(100,200)
print(minDivisor,maxDivisor)