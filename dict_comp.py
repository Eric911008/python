#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dict綜合表達式
活動19

@author: linweicheng
"""

student = ["Joy" , "Chole" , "Ting" , "Nate"]

score = [70, 82, 80, 79]

scores = {i:j for (i,j) in zip(student, score)}

print(scores)
