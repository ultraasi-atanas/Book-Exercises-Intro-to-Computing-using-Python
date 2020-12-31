# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:59 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 5 Structured types, Mutability and Higher-Order Functions

Dictionaries 

The View Object
Hashable types as keys

@author: Atanas Kozarev - github.com/ultraasi-atanas

"""

months = {'Jan' : 1, 'Feb' :2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6}

# The view object

keysView = months.keys()

print(keysView,'\n')

# If we change the dict now, the View obj also updates

months["Dec"] = 12 # associates the value 12 with the key "Dec" in months. If there is already a value associated with k, that value is replaced

print(keysView,'\n') # now prints a changed view
print(type(keysView),'\n') # <class 'dict_keys'>

# We only get the keys if we iterate over a dict with a For loop, not the values
for e in months:
    print(e)
        
# An object of type <class 'dict_keys'> can be converted to a list
print(list(months),'\n')    

# We can also get out the Values
valuesView = months.values()
print(type(valuesView),'\n') # <class 'dict_values'>
for v in valuesView:
    print(type(v), '\n')

# We want to get out all the keys that have a certain value

students = { "Ana":"A", "John":"C", "Mike": "A", "Greg": "B", "Serena":"C" }
keyResults = []
searchValue = "A"
for d in students:
    if students[d] == "A":
        keyResults.append(d)
        
print(keyResults,'\n')
    
# Tuples as keys, a timetable for a small airport with three fights a week, implemented with tuples as keys
flights = {('FA1234','Mon'):'12:30', ('EZ1676','Tue'): '09:45', ('ZZ9881','Wed') : '08:34'}

print(flights.keys(),'\n')



# Hashable types
# __hash__ method
# __eq__ method

# =============================================================================
# all of pythons built-in immutable types are hashable. 
# none of the python mutable types are hashable.
# It is often convenient to use tuples as keys
# Example
# It's like keys in a database table, you can have multiple keys, here represented by
# a tuple, to uniquely identify a row in the database table
# =============================================================================

