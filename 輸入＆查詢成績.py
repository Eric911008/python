#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:20:27 2021

@author: linweicheng
"""

dict1 = {"林小明": 85 , "曾山水": 93 , "黃明土": 67}
name = input("請輸入學生姓名:")
if name in dict1:
    print(name + "的成績為" + str(dict1[name]))
else:
    score = input("輸入學生成績:")
    dict1[name] = score
    print("字典內容:" + str(dict1))
         
