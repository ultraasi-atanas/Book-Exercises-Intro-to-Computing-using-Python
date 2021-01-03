# -*- coding: utf-8 -*-
"""
Created on Sun Jan 03 2021 - 13:26
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 7 Exceptions and Assertions 

Try, except - def readInt(), def readValPolymorphic()


@author: Atanas Kozarev - github.com/ultraasi-atanas
"""

def readInt():
    while True:
        val = input('Enter an integer: ')
        try:
            return(int(val)) # convert str to int before returning
        except ValueError:
            print(val, 'is not an integer')

# the function readValPolymorphic is polymorphic, works for arguments of many types
def readValPolymorphic(valType, requestMgs, errorMsg):
    while True:
        val = input(requestMgs)
        try:
            return(valType(val)) # convert str to valType before returning
        except ValueError:
            print(val, errorMsg)
                
readInt()

readValPolymorphic(int, "Please enter an integer:", "is not an integer")