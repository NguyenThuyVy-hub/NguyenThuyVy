# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:26:33 2024

@author: This PC
"""
import math
print("Giai phương trình ax^2+bx+c")
a = float(input("Nhập a: "))
b = float(input("Nhập b: ")) 
c = float(input("Nhập c: "))
if(a!=0):
    delta = b**2 - 4*a*c
    if (delta<0):
        print("Phương trình vô nghiệm ")
    elif (delta==0):
        x = -b/ (2*a)
        print("Có nghiệm khép x1=x2=" , x)
    else:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = ( -b+math.sqrt(delta))/(2*a)
        print("có nghiệm kép x1={0} và x2+{1}".format(x1,x2))
else:
    print("Không phải là phương trình bậc 2")
        
    
