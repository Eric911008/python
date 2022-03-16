#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
teacher's instruction

@author: linweicheng
"""
# most used database
import pandas as pd

import numpy as np

from sklearn.linear_model import LinearRegression #ssk = scikit 用於線性回歸

from sklearn.metrics import mean_squared_error

from sklearn.model_selection import train_test_split #訓練＿測試＿切割

housing_df = pd.read_csv('train.csv')
print(housing_df)
print(type(housing_df))
print(housing_df.head())
housing_df = housing_df.dropna()

