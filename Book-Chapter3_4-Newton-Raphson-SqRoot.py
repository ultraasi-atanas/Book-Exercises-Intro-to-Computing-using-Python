# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:09 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 3 Finger Exercises

Newton-Raphson for square root

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""
# Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
count = 0
k = 24.0
guess = k/2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    count += 1
print("Count is",count)
print('Square root of', k, 'is about', guess)