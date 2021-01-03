# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 09:42 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 5 Structured types, mutability and higher-order functions

Ranges

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""
print(range(10))
print()  # empty line 

for i in range(10):
    print(i)
    
print();  # empty line 
print(range(10)[2:6][2])  # prints 4, the slice [2:6] is (2,3,4,5) and index [2] equals 4