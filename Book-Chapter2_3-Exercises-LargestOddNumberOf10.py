# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 14:15:03 2020
Introduction to Computation and Programming Using Python. John V. Guttag, 2016, 2nd ed
Book Chapter 2 Finger Exercises

Largest Odd number of 10, using user input
Prints the largest odd number that was entered
If no odd number was entered, it should print a message to that effect

@author: Atanas Kozarev - github.com/ultraasi-atanas
"""
# big goal is to handle and compare negative numbers entered

# we will build in a logic that start with an initial value of 0
# and then the first odd value entered by the user is

largest = 0
userPromptsRemaining = 10
print("You will be asked to enter a number 10 times")
while userPromptsRemaining > 0:
    # get a number in
    newNumber = int(input("Please enter a number: "))
    # check if it's odd
    if (newNumber % 2) != 0:
        # check if that's the first registered number
        if largest == 0:
            largest = newNumber
        elif newNumber > largest:
            # do we have found a new largest
            largest = newNumber
    userPromptsRemaining -= 1

if largest == 0:
    print("No odd numbers entered")
else:
    print("Largest odd number entered ", largest)


