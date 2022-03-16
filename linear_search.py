#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:20:37 2021

@author: linweicheng
"""

def linear_Search(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [1,5,8,7]
x = 7
n = len(array)
result = linear_Search(array, n, x)
if(result == -1):
    print(" 無 ")
else:
    print(result)
