# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:57 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 5 Structured types, mutability and higher-order functions

Object equality

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""

Techs = ['MIT','Caltech']
Ivys = ['Harvard','Brown','Yale']

Univs = [Ivys, Techs]
Univs_1 = [['Harvard','Brown','Yale'],['MIT','Caltech']]


print('Techs contains', Techs)
print('Ivys contains', Ivys)
print('Univs contains', Univs)
print('Univs_1 contains', Univs_1)
    
print()

print(Univs == Univs_1, ' Test value equality') # True 
print(id(Univs) == id(Univs_1), ' Test object equality') # False
print('Id of Univs =', id(Univs))
print('Id of Univs_1 = ', id(Univs_1))

print()

newTechs = Techs
print('newTechs = Techs')
print(newTechs == Techs, ' Test value equality') # True
print(id(newTechs) == id(Techs), ' Test object equality') # True
print('Id of newTechs =', id(newTechs))
print('Id of Techs = ', id(Techs))

print()
newTechs = list(Techs)  # clone using list()
print('newTechs = list(Techs)')
print(newTechs == Techs, ' Test value equality') # True
print(id(newTechs) == id(Techs), ' Test object equality') # False

print('Id of newTechs =', id(newTechs))
print('Id of Techs = ', id(Techs))