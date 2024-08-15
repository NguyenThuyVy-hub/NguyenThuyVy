# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 22:19:13 2024

@author: Nguyen Thuy Vy
"""
#tính quãng đường
d = float (input ("nhập quãng đường đã đi (km)") )
if d <=1:
    print("gía là 20k")
elif d > 1 and d <= 4:
    print("giá là:", d*13000)
elif d>= 4 and d <= 8:
    print("giá là:", (3*13000)+ (d-3)*12000)
else:
    print("giá là:", 39000 + 60000 + (d-8)*10000)
    m= 39000 + 60000 + (d-8)*10000
    if m>= 10000:
        print("giá là sau khi giảm:", m*0.92)
    
          