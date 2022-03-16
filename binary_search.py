#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 15:30:14 2021

@author: linweicheng
"""

array = [1,5,7,8]

search_for = 7

slice_start = 0
slice_end = len(array)-1

found = False

while slice_start <= slice_end and not found :
    location = (slice_start + slice_end) // 2
    if array[location] == search_for:
        found = True
    else:
        if search_for < array[location] :
            slice_end = location - 1
        else:
            slice_start = location + 1
            
print(found)
print(location)           
            