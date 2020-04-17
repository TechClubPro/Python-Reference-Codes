# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:09:13 2020

@author: TechClub
"""

chemicals={"Na":["Sodium",11,"Soft Metal","Silver White"],
           "Cl":["Chlorine",17,"Non Metal","Yellow Green"],
           "Fe":["Iron",26,"Metal","Red"]}


name=input("Enter the Chemical Name : ")

print("Do You want to Know:")

print("1: Name of Chemical")
print("2: Atomic Number")
print("3: Metal or Non-Metal")
print("4: Colour of Chemical")

choice=int(input("Enter choice: "))

print("Here's your info. for "+name)
print(chemicals[name][choice-1])