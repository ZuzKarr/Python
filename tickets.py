# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:32:08 2022

@author: Zu
"""

prompt = "Ile masz lat? "
prompt += "\n(Kiedy zakończysz podawanie wieku, wpisz 'koniec') "

while True:
    age = input(prompt)
    if age == 'koniec':
        break
    age = int(age)
    
    if age < 3:
        print(" Bilet jest bezpłatny! ")
    elif age < 13:
        print(" Bilet kosztuje 10 zł! ")
    else:
        print(" Bilet kosztuje 15 zł!")
        
        
        






