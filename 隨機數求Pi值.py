#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用隨機數球pi值（蒙地卡羅方法）
活動20

@author: linweicheng
"""

from random import random
from math import sqrt

point = int(input("輸入次數:"))
point_center = 0

for i in range(point):
    x = random()
    y = random()
    distance = sqrt( x**2 + y**2 )
    if distance <= 1:
        point_center += 1
        
Pi = 4 * point_center / point    
print(Pi)    
print(Pi - 3.141592653589793238462643383)
        
