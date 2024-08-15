# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 23:11:28 2024

@author: This PC
"""

a, b, c = map(float, input().split())
if a + b > c or a + c > b or b + c > a:
    if a*a==b*b +c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        loaitamgiac = 'Vuông'
    elif a==b and b==c :
        loaitamgiac = 'Đều'
    elif a==b or a==c or b==c:
        loaitamgiac = 'Cân'
    elif a*a>b*b + c*c or b*b > a*a+c*c or c*c > a*a+b*b:
        loaitamgiac = 'Tù'
    else:
        loaitamgiac = 'Nhọn'
    print('{}, {}, {} là ba cạnh của tam giác {}'.format(a,b,c,loaitamgiac))
else:
    print('({}, {}, {} không là ba cạnh của tam giác' .format (a,b, c))
    
        
        
        
 
 
