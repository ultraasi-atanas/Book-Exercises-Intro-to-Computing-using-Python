# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:43:49 2020

Python Type Oddities

These statements return a 0 or True and it was very strange to witness!
Result is sometimes Bool, sometimes Int, it's bizzare.

@author: Atanas Kozarev - github.com/ultraasi-atanas

"""

print(1%2 and True)
# Out[16]: True

print(2%2 and True)
# Out[17]: 0

print(3%2 and True)
# Out[18]: True

print(4%2 and True)
# Out[19]: 0

print(0 and True)
# Out[20]: 0