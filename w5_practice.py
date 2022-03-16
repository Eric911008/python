#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 23:39:33 2021

@author: linweicheng
"""

def sum_first_n(n):  #for 迴圈函式
    result = 0
    for i in range (n):
        result += i +1
    return result
sum_first_n(100)
    



def print_the_next_number(start): #遞迴函式
    print(start+1)
    return print_the_next_number(start+1)

print_the_next_number(100)



def countdown(n):      #遞迴倒數 ??????
    if n ==0:
        print("liftoff!")
    else:
        print(n)
        return(n-1)

countdown(3)    


def factorial_iterative(n):    #帶有迭代和遞迴的階乘
    result = 1
    for i in range(n):
        result *= i+1
    return result

factorial_iterative(5)    




def factorial_iterative(n):    #帶有迭代和遞迴的階乘(2)
    if n ==1:
        return 1
    else:
        return n * factorial_iterative(n-1)
                                  
factorial_iterative(5)



import time
stored_results = {}
def sum_to_n(n):
    start_time = time.perf_counter()
    result = 0
    for i in reversed(range(n)):
        if i+1 in stored_results:
            print('Stopping sum at %s because we have previously computed it'
                  % str(i+1))
            result += stored_results[i+1]
            break
        else:
            result += i+1
    stored_results[n] = result
    print(time.perf_counter()-start_time, "seconds")   
    
sum_to_n(1000000)















































