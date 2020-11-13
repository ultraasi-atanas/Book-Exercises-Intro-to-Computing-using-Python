# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:15:03 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 3 Finger Exercises

Cube root

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""

# Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
# try x = 1957816251 it finishes almost instantly, and 7406961012236344616 too
ans = 0
while ans ** 3 < abs(x):
    ans = ans + 1
    # author: Atanas Kozarev - github.com/ultraasi-atanas
if ans ** 3 != abs(x):
    print(x, "is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)
