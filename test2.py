#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:58:18 2021

3種演算法的程式碼
"""

def linear_Search(array, n, x):   #linear search
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
    print('-'*30)
    
        
def BubbleSort(array):         # bubble sort
    n = len(array)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
 
BubbleSort(array)
 
for i in range(len(array)):
    print ("%d" %array[i])
   
    
search_for = 7               # binary search

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
            
print('-'*30)            
print(location)
                