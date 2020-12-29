# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:20 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 5 Structured types, mutability and higher-order functions

Object equality - Deep clone

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""
import copy

print()
Techs = ['MIT','Caltech']
Ivys = ['Harvard','Brown','Yale']
Univs = [Ivys, Techs]

# COPY with LIST()
newUnivs = list(Univs) # clone with list()
print('Techs contains', Techs)
print('Ivys contains', Ivys)
print('Univs contains', Univs)
print('newUnivs = list(Univs)')
print('newUnivs contains ', newUnivs, '\n')


print('Id of Univs =', id(Univs))
print('Id of newUnivs = ', id(newUnivs))
print(Univs == newUnivs, ' Test value equality') 
print(id(Univs) == id(newUnivs), ' Test object equality') 
print('However...')
print(id(Univs[0]) == id(newUnivs[0]), ' Test object equality on [0] element', '\n') 
print('Id of Univs[0] = ', id(Univs[0]))
print('Id of newUnivs[0] = ', id(newUnivs[0]))
print('Id of Ivys = ', id(Ivys), '\n')

# DEEP COPY 
print('The list cloned contains mutable objects, we want to copy those as well not only the list shell, containing alises or paths to those same mutable objects')
print('We then import copy and use copy.deepcopy', '\n')

newUnivs = copy.deepcopy(Univs)
print(Univs == newUnivs, ' Test value equality') 
print(id(Univs) == id(newUnivs), ' Test object equality') 
print(id(Univs[0]) == id(newUnivs[0]), ' Test object equality on [0] element')
print('Id of Univs[0] = ', id(Univs[0]))
print('Id of newUnivs[0] = ', id(newUnivs[0]))
print('Id of Ivys = ', id(Ivys), '\n')
