# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:33:16 2024

@author: nguyenthuythaovy
"""

while True:
    a=input('Nhập số nguyên trong khoảng [-99,99]:')
    if a.isdigit() and -99<=int(a)<=99:
        break
    print("Số bạn nhập không nằm trong khoảng cho phép. Nhập lại!")

        