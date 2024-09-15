# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:01:20 2024

@author: nguyenthuythaovy
"""

a=int(input("Nhập bảng cửu chương bạn muốn:"))
if 1<a<10:
    s=1
    print("Bảng cửu chương
           ",a)
    for i in range (1,11):
        s=a*i
        print(i,"*",a,"=",s)
else:
    print("Không xác định")
    