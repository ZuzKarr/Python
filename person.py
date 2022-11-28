# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:30:02 2022

@author: Zu
"""

person_0 = {
    'first_name': "beri",
    'last_name': 'ronikier',
    'age': 27,
    'city': 'warsaw'                  
    }

person_1 = {
    'first_name': "zuzia",
    'last_name': 'plawska',
    'age': 19,
    'city': 'gdansk'                  
    }

person_2 = {
    'first_name': "antek",
    'last_name': 'plawski',
    'age': 23,
    'city': 'warsaw'                  
    }
  
people = [person_0, person_1, person_2]

for person in people:
    print(person)

for person in people:
    name = person['first_name'].title() + '' + person['last_name'].title()
    age = person['age']
    city = person['city'].title()
    
    print(name +', of city ' +city +' is ' +str(age) +' years old.')












