#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 13:22:03 2021

@author: linweicheng
"""

import csv

lines = []

with open('W6_活動13.csv') as csv_file :
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        lines.append(line)
        
data = lines[1:]
passengers = []
headers = lines[0]

for d in data:
    p = {}
    for i in range(0,len(headers)):
        key = headers[i]
        value = d[i]
        p[key] = value
    passengers.append(p)     
    
survived = [p['Survived'] for p in passengers]
pclass = [p['Pclass'] for p in passengers]
age = [float(p['Age']) for p in passengers if p['Age'] != '']
gender_survived = [p['Sex'] for p in passengers if int(p['Survived']) == 1]




import pandas as pd
import matplotlib.pyplot as plt


train_data = pd.read_csv('W6_活動13.csv',index_col='PassengerId')
train_data[:4]

plt.figure(figsize=(5,5))
train_data.Sex.value_counts().plot(kind = 'pie')

train_data.Sex.value_counts()
train_data.groupby('Sex').Survived.mean().plot(kind='bar')
print (train_data.groupby('Sex').Survived.value_counts())


labels = ['0' , '1']
num = [549 , 342]
import matplotlib.pyplot as plt
plt.title('Survived' , fontdict = {'fontsize' :20})
plt.pie(num,labels=labels , autopct = '%1.1f%%' , colors = ['lightblue' , 'lightgreen'])
plt.show()

label1 = ['female' , 'male']
num2 = [233 , 109]
import matplotlib.pyplot as plt
plt.title('surving passengers count by gender')
plt.bar(label1 , num2 , color = ['blue' , 'blue'])
plt.show()



















