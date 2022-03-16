"""
期末專題___回歸題

@author: linweicheng
"""

import pandas as pd                    #匯入檔案
import numpy as np                     #引入 numpy 模組
import matplotlib.pyplot as plt        #資料視覺化
import seaborn as sns             
import warnings
warnings.filterwarnings('ignore')      #忽略匹配的警告
from sklearn.preprocessing import LabelEncoder                     #把每個類別對應到某個整數
from sklearn.model_selection import train_test_split as holdout    #將資料切割為訓練及測試集


df = pd.read_csv('insurance.csv')      #匯入檔案(insurance.csv)

sns.set(style='whitegrid')
f, ax = plt.subplots(1,1, figsize=(12, 8))
ax = sns.distplot(df['charges'], kde = True, color = 'c')
plt.title('Distribution of Charges')

f, ax = plt.subplots(1, 1, figsize=(12, 8))
ax = sns.barplot(x='region', y='charges', hue='sex', data=df, palette='cool')


f, ax = plt.subplots(1,1, figsize=(12,8))
ax = sns.barplot(x = 'region', y = 'charges',
                 hue='smoker', data=df, palette='Reds_r')


ax = sns.lmplot(x = 'age', y = 'charges', data=df, hue='smoker', palette='Set1')
ax = sns.lmplot(x = 'bmi', y = 'charges', data=df, hue='smoker', palette='Set2')

##Converting category labels into numerical using LabelEncoder
label = LabelEncoder()
label.fit(df.sex.drop_duplicates())
df.sex = label.transform(df.sex)
label.fit(df.smoker.drop_duplicates())
df.smoker = label.transform(df.smoker)
label.fit(df.region.drop_duplicates())
df.region = label.transform(df.region)
df.dtypes

x = df.drop(['charges'], axis = 1)
y = df['charges']

x = x.dropna(axis = 1, how = 'any')
print(x.shape)  #(1338, 6)

x_train, x_test, y_train, y_test = holdout(x, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
Lin_reg = LinearRegression()
Lin_reg.fit(x_train, y_train)

score1 = Lin_reg.score(x_test, y_test)                  
print("LinearRegression:")
print('Score: ', score1)
print('Accuracy: ' + str(score1*100) + '%')
print("--"*20) 


from sklearn.linear_model import Ridge
Ridge = Ridge(alpha=0.5)
Ridge.fit(x_train, y_train)
score2 = Ridge.score(x_test, y_test)                 
print("Ridge:")
print('Score: ', score2)
print('Accuracy: ' + str(score2*100) + '%')
print("--"*20)


from sklearn.linear_model import Lasso
Lasso = Lasso(alpha=0.2, fit_intercept=True, normalize=False, precompute=False, max_iter=1000,
              tol=0.0001, warm_start=False, positive=False, random_state=None, selection='cyclic')
Lasso.fit(x_train, y_train)
score3 = Lasso.score(x_test, y_test)                 
print("Lasso:")
print('Score: ', score3)
print('Accuracy: ' + str(score3*100) + '%')
print("--"*20)


from sklearn.preprocessing import PolynomialFeatures
x = df.drop(['charges', 'sex', 'region'], axis = 1)
y = df.charges
pol = PolynomialFeatures (degree = 2)
x_pol = pol.fit_transform(x)
x_train, x_test, y_train, y_test = holdout(x_pol, y, test_size=0.2, random_state=0)
Pol_reg = LinearRegression()
Pol_reg.fit(x_train, y_train)
y_train_pred = Pol_reg.predict(x_train)
y_test_pred = Pol_reg.predict(x_test)

score4 = Pol_reg.score(x_test, y_test)                 
print("Polynomial:")
print('Score: ', score4)
print('Accuracy: ' + str(score4*100) + '%')
print("--"*20)

