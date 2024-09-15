# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:10:11 2024

@author: nguyenthuythaovy
"""

import random
a=random.randint(20,30)
print(a)
ds=[]
for i in range(a):
    b=random.uniform(18,99)
    c=b**2
    ds.append(c)
print("Danh sách:")
print(ds) 