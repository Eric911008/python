#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 23:16:15 2021

@author: linweicheng
"""
from customer import customer_format

def customer_format(first_name,last_name,location):
    return first_name+last_name+location
customer_format('Muse',' Chen',location=' (Taiwan)')

customer_format="Joy Liao"
print(customer_format)


     

    