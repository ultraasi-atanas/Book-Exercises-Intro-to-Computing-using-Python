# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:09 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 3 Finger Exercises

Bisection search for square root

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""
# Find x such that x**2 - 24 is within epsilon of 0
x = 24
epsilon = 0.01
count = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    count +=1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('Count is', count)
print(ans, 'is close to square root of', x)
