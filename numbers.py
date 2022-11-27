# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 19:52:25 2022

@author: Zu
"""

numbers=list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) +"th")