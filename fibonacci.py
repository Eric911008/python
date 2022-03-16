#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:13:24 2021

Fibonacci函式
"""
def fibonacci_iterative(n):     #迭代式的Fibonacci函式
    f1, f2 = 1, 1
    for i in range(2, n):  
        f1, f2 = f2, f1 + f2
    return f2

fibonacci_iterative(3)
fibonacci_iterative(10)


def fibonacci_recursive(n):     #遞迴式的Fibonacci函式
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

fibonacci_recursive(3)
fibonacci_recursive(10)


Dict={0:0, 1:1}                #動態程式設計版本的Fibonacci函式
def fibonacci_dynamic(n):
    if n not in Dict:
        x = fibonacci_dynamic(n-1)+fibonacci_dynamic(n-2)
        Dict[n]= x
    return Dict[n]

fibonacci_dynamic(100)
