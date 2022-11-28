# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:32:08 2022

@author: Zu
"""

prompt = "Podaj jakie dodatki chcesz na swojej pizzy! "
prompt += "\n(Gdy zakończysz podawanie dodatków, napisz 'koniec'.) "

while True:
    dodatek = input(prompt)
    
    if dodatek == 'koniec':
        break
    else:
        print("Chciałbym dodac do swojej pizzy " + dodatek + ".")


