# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 00:14:31 2024

@author: This PC
"""

# Nhập điểm GPA từ bàn phím
gpa = float(input("Nhập điểm trung bình (GPA): "))

# Xếp hạng học lực dựa trên GPA
if gpa < 3.5:
    print("Học lực Kém")
elif 3.5 <= gpa < 5.0:
    print("Học lực Yếu")
elif 5.0 <= gpa < 7.0:
    print("Học lực Trung bình")
elif 7.0 <= gpa < 8.0:
    print("Học lực Khá")
elif 8.0 <= gpa < 9.0:
    print("Học lực Giỏi")
elif 9.0 <= gpa <= 10:
    print("Học lực Xuất sắc")
else:
    print("Điểm GPA không hợp lệ")

