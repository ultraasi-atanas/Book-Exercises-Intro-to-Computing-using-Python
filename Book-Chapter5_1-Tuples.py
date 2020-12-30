# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 09:42 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 5 Structured types, mutability and higher-order functions

Tuples - intersection of two tuples

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""

def intersect(t1,t2):
    """Assumes t1 and t2 are tuples
        Returns a tuple containing elements that are in
        both t1 and t2"""
        
    result = ()  # empty tuple
    for e in t1:
        if e in t2:
            result += (e,) # tupple addition, (e,) tuple is added to result tuple
    
    return result

intersection = intersect((1,'two',3), (3,(1,'two',3),3.25))
print(intersection)  # prints (3,)
    