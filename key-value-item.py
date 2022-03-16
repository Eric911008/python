#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:14:44 2021

@author: linweicheng
"""

dict1 = {"gold":26 , "silver":34 , "bronze":30}
listkey = list(dict1.keys())
listvalue = list(dict1.values())

for i in range(len(listkey)):
    print("得到的 %s 數目為 %d 面" % (listkey[i],listvalue[i]))
    
    
item1 = list(dict1.items())
print(item1)
