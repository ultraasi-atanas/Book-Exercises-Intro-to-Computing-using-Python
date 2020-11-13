# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:05:03 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 2 Finger Exercises

Using While Loop

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
# concatenate X to toPrint numXs times
while numXs > 0:
    toPrint = toPrint + 'X'
    numXs -= 1
print(toPrint)