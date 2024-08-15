# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 00:25:28 2024

@author: This PC
"""

# Nhập các hệ số a, b, c từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Xử lý phương trình
if a == 0:
    if b == c:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = (c - b) / a
    print(f"Phương trình có nghiệm x = {x:.2f}")