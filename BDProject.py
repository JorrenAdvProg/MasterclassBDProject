# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt

data = pd.io.stata.read_stata("GSS2012.DTA")

## create age groups
AGE = {}     
for i in range(10,90):
    AGE[i] = 0
    for ages in data.age:
        if i == ages:
            AGE[i] = AGE[i]+1
agecounts = []
for i in range(10,90):
    agecounts.append(AGE[i])
     
## create race groups     
RACE = {}
for race in data.race:
    if race not in RACE:
        RACE[race] = 1
    else:
        RACE[race] = RACE[race] + 1        

## create sex groups 
male = 0
female = 0
for sex in data.sex:
    if sex == 'male':
        male += 1
    if sex == 'female':
        female += 1
        
## Creating income groups
incomegroups = [0,0,0,0,0,0,0,0,0,0,0,0,0]
for income in data.income:
    if income == 'nan':
        incomegroups[0] += 1
    elif income == 'LT $1000':
        incomegroups[1] += 1
    elif income == '$1000 TO 2999':
        incomegroups[2] += 1
    elif income == '$3000 TO 3999':
        incomegroups[3] += 1
    elif income == '$4000 TO 4999':
        incomegroups[4] += 1
    elif income == '$5000 TO 5999':
        incomegroups[5] += 1
    elif income == '$6000 TO 6999':
        incomegroups[6] += 1
    elif income == '$7000 TO 7999':
        incomegroups[7] += 1
    elif income == '$8000 TO 9999':
        incomegroups[8] += 1
    elif income == '$10000 - 14999':
        incomegroups[9] += 1
    elif income == '$15000 - 19999':
        incomegroups[10] += 1
    elif income == '$20000 - 24999':
        incomegroups[11] += 1
    elif income == '$25000 OR MORE':
        incomegroups[12] += 1
        
        
plt.subplot(4,1,1)
plt.bar(range(10,90), agecounts)
plt.xlabel("age")
plt.ylabel("frequency")
plt.subplot(4,1,2)
plt.bar([1,2], [male, female])
plt.xticks([1.5,2.5], ("Male", "Female"))
plt.ylabel("frequency")
plt.subplot(4,1,3)
plt.bar([1,2,3], [RACE['white'], RACE['black'], RACE['other']], 0.5)
plt.xticks([1.25,2.25,3.25], ('White', 'Black', 'Other'))      
plt.ylabel("frequency")
plt.subplot(4,1,4)
plt.bar(range(1,14), incomegroups, 1)
plt.xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5], ('nan','<1k','1k-3k','3k-4k','4k-5k','5k-6k','6k-7k','7k-8k','8k-10k','10k-15k','15k-20k','20k-25k','>25k'))