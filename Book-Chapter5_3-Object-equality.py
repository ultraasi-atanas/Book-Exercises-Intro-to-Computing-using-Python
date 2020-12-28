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

idUnivs = id(Univs)
idUnivs_1 = id(Univs_1)


print(Univs == Univs_1) # True - Test value equality
print(idUnivs == idUnivs_1) # False - Test object equality
print('Id of Univs =', idUnivs)
print('Id of Univs_1 = ', idUnivs_1)
