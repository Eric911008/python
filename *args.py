#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 15:02:34 2021

@author: linweicheng
"""

def prnSum(name,*args):
    print(name,args,'=',sum(args))
    
prnSum('加總',1,2,3,4)






def prnPrice (name,*kwargs):
    print(name,kwargs)
    
prnPrice('飲料','紅茶50','咖啡80')    