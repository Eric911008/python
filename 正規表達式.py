#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正規表達式
活動21

@author: linweicheng
"""

import re

names = ["Xander Harris", "Jennifer Smith", "Timothy Jones", 
         "Amy Alexandrescu", "Peter Price", "Weifung Xu"]

x = re.compile(".*x", re.I)
filtered_list = list(filter(x.match, names))

print(filtered_list)

