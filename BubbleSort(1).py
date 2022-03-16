#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:55:49 2021

@author: linweicheng
"""

def BubbleSort(array):
    n = len(array)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
 
array = [1,5,8,7]
 
BubbleSort(array)
 
for i in range(len(array)):
    print ("%d" %array[i])
