#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用迭代,遞迴,動態程式方法完成求兩數之最大公因數並計算時間(2)

"""

a = int(input("First number = "))            #遞迴
b = int(input("Second number = "))

def hcf(a, b):
    if b > a:
        return hcf(b, a)
    if a % b == 0:
        return b
    return hcf(b, a % b)

print("HCF of", a, "and" , b, "is", hcf(a,b))
print()

import timeit                                         #計時
start = timeit.default_timer()
stop = timeit.default_timer()

print('Time: ', stop - start)


