# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 17:33:15 2022

@author: Zu
"""

squares=[]
for value in range (1,11):
    square= value**2
    squares.append(square)
    
print(squares)

#krótsza wersja:
squares=[]
for value in range(1,11):
    squares.append(value**2)
    
print(squares)

#jeszcze bardziej krótka wersja:
squares=[value**2 for value in range(1,11)]
print(squares)