# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:09 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 4 Finger Exercises

Using method str.in write a function that takes two strings and returns
True if either is contained inside the other, False othewise
@author: Atanas Kozarev - github.com/ultraasi-atanas
"""
def isIn(str1, str2):
    if (str1 in str2) or (str2 in str1):
        return True
    else:
        return False

print(isIn("Ata","nasAta")) # other test cases isIn("Ata","nas") or isIn("Ata","ta")
