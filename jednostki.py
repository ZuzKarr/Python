# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:19:15 2022

@author: Zu
"""

import math as mt

a=float(input("Podaj liczbe "))
b=str(input("Podaj jednostke "))

if b=="mm":
    a1=a/25.4
    
    print("Miara w calach wynosi " +str(a1))
    
else:
    a2=a*25.4
    
    print("Miara w milimetrach wynosi " +str(a2))
    