# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 00:18:39 2024

@author: This PC
"""

# Nhập 3 số a, b, c từ bàn phím
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện tam giác
if a + b > c and a + c > b and b + c > a:
    print("Ba số này là ba cạnh của một tam giác.")
else:
    print("Ba số này không phải là ba cạnh của một tam giác.")
