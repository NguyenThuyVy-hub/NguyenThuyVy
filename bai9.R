#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:29:04 2024

@author: nguyenthuyvy
"""

import math
a = float(input("Nhập vào số thực a: "))
b = float(input("Nhập vào số thực b: "))
a =(((math.sqrt(a)) - (math.sqrt(b)))/((math.pow(a,0.25)) - (math.pow(b,0.25)))) 
b = ((math.sqrt(a)) + (math.pow(a*b,0.25)))/((math.pow(a,0.25)) + (math.pow(b,0.25)))
result = a - b
print("ket qua la: ", round(result,3))
          