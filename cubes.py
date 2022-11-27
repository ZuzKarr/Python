# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 17:41:46 2022

@author: Zu
"""

#numbers= list(range(1,1000001))
#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))

thirds=[]
for value in range(1,20,2):
    thirds.append(value)
       
print(thirds)

thirds=[value for value in range(1,20,2)]
print(thirds)




cube=[value**3 for value in range(3,30)]
print(cube)

cube=[value**3 for value in range(1,11)]
print(cube)