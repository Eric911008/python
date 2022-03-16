#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:32:40 2021

@author: linweicheng
"""

#計算字元數，字數，行數

def wordcount(filename):
    result = {
        'Characters': 0,
        'Words': 0,
        'Unique words': 0,
        'Lines': 0,
        }
    unique_words = set()
 
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            result['Lines'] += 1
            result['Characters'] += len(line)
            result['Words'] += len(words)
            unique_words.update(words)
 
        result['Unique words'] = len(unique_words)
 
    for key, value in result.items():
        print(f'{key}: {value}')

wordcount(r'.\data\text.txt')



# 讀出檔案最後一行字的四種方法

f = open(filename, 'r')

#readlines()列印出全部檔案後，看最後一行
for line in f.readlines():
    print(line)

#readline()以無窮迴圈讀檔案，只記錄當下讀到的一行
while True:
    line=f.readline()
    if not line:
        break
    lastline=line
print(lastline)


#直接走訪檔案物件，讀出檔案每一行，只記錄當下讀到的一行
for line in f:
    lastline=line
print(lastline)


#直接走訪檔案物件，讀出檔案每一行
for line in f:
    pass
print(line)   

f.close()
    
