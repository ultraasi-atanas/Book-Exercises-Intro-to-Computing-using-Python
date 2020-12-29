# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:59 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 5 Structured types, Mutability and Higher-Order Functions

Dictionaries 

Key - Value pairs
Tuples can be keys
Dict is mutable

One of the great things about Python. The problem in other languages,
where programmers have to use other types to provide similar functionality
(e.g. using a list, each element is a key/value pair), 
is that searching/key-retrieval is computationally inefficient.
In worst case, its linear complexity, having to examine each element.
In Python dicts built-in retrieval is implemented using a hashing
which is quite fast, in time that's nearly independent of the size of the dict

@author: Atanas Kozarev - github.com/ultraasi-atanas

"""

months = {'Jan' : 1, 'Feb' :2, 'Mar' : 3, 'Apr' : 4, 
          'May' : 5, 'Jun' : 6}

# print(months[1]) # KeyError: 1

print(type(months)) # <class 'dict'>
print(months['Jan'])
# Substraction of two pairs gives us the distance between them
print('Apr and Jan are', months['Apr'] - months['Jan'], 'months apart')\
    
# ADDING AN ENTRY

months['Jul'] = 7

# SEARCHING IN A LIST IMPLEMENTATION of dict, see docstring
L = [['Jan',1], ['Feb',2], ['Mar',3], ['Apr',4], ['May',5], ['Jun',6]]
def keySearch(L,k):
    for elem in L:
        if elem[0] == k:
            return elem[1]
    return None

print(keySearch(L,'Feb'))

