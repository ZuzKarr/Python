# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 17:35:22 2022

@author: Zu
"""

guests=['sebastian vettel', 'charles leclerc', 'yuki tsunoda']

name= guests[0].title()
print(name + ", please come to dinner.")

name= guests[1].title()
print(name + ", please come to dinner.")

name= guests[2].title()
print(name + ", please come to dinner.\n")

#do zrobienia przerw miedzy linijkami mozna uzyc \n, print() albo print("")

print(guests[1].title() +" can't come to dinner\n")
#charles can't come, let's invite carlos 

del guests[1]
guests.insert(1, 'carlos sainz')

name= guests[0].title()
print(name + ", please come to dinner.")

name= guests[1].title()
print(name + ", please come to dinner.")

name= guests[2].title()
print(name + ", please come to dinner.")

print('\nWe got a bigger table!\n')

#dodajemy wiecej osob. insert pozwala dodac w konkretne miejsce, 
#append dodaje na koniec listy

guests.insert(0, 'pierre gasly')
guests.insert(2, 'mick schummacher')
guests.append('max verstappen')
print(guests)


name= guests[5].title()
print(name)

name= guests[0].title()
print(name + ", please come to dinner.")

name= guests[1].title()
print(name + ", please come to dinner.")

name= guests[2].title()
print(name + ", please come to dinner.")

name= guests[3].title()
print(name + ", please come to dinner.")

name= guests[4].title()
print(name + ", please come to dinner.")

name= guests[5].title()
print(name + ", please come to dinner.")





