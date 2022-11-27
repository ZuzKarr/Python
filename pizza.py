# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 17:22:24 2022

@author: Zu
"""
pizzas=['hawajska', 'pepperoni', 'wiejska', 'sycylijska']

for pizza in pizzas:
    print('I really love ' + (pizza) + " pizza!" )

print('\nI really love pizza!')

friends_pizza=pizzas[:]

pizzas.append('kebab')
friends_pizza.append('amerykanska')

print('\nMoje ulubione rodzaje pizzy to:')
print(pizzas)

    
print('\nUlubione pizzy mojego przyjaciela to:')
print(friends_pizza)