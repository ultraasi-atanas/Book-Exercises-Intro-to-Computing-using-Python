# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:50 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 5 Structured types, mutability and higher-order functions

Functions as Objects, Higher Order Functions, higher-order programming

In Python, functions are a first class object, like int or list
Functions can appear in expressions, as an argument to a funtion, elements of lists

MAP
map(argF,arg1,arg2,..argN) Python 3.x
The first argument can be a function of n arguments, in which case it must
be followed by n consequent ordered collections (each of the same length)
<map object at 0x7ff5f22babe0>
Help on map()
map(func, *iterables) --> map object
Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
It behaves like a range object, you have to iterate over it

LAMBDA
Lambda expressions are frequently used as arguments to higher-order functions
Synonymous with anonymous functions, functions without a name
lambda <sequence of variable names> : <expression>

@author: Atanas Kozarev - github.com/ultraasi-atanas

"""

# EXAMPE OF MAP
for i in map(abs,[-1,2,-3]):
    print(i)
    

    
# LOOKING 'UNDER THE HOOD'
mapObj1 = map(abs,[-1,2,-3])

print(mapObj1) # <map object at 0x7ff5f22babe0>

print(id(mapObj1)) # 140694306661904



# YOU HAVE TO ITERATE OVER THE MAP OBJECT
for one in mapObj1:
    print(one)
    
    

# SLICING AND INDEXING OF AN MAP OBJECT

# TypeError: 'map' object is not subscriptable
# print(mapObj1[1:3]) 

# TypeError: 'map' object is not subscriptable
# print(mapObj1[1]) 

# TypeError: object of type 'map' has no len()
# print(len(mapObj1))


# LAMBDA Example
L = []
for i in map(lambda x,y: x*y, [1,2,3,4],[3,2,1,0]): # almost like a matrix product
    L.append(i)
    
print(L)



