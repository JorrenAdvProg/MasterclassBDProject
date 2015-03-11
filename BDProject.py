# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt

data = pd.io.stata.read_stata("GSS2012.DTA")

AGE = {}     
for i in range(10,90):
    AGE[i] = 0
    for ages in data.age:
        if i == ages:
            AGE[i] = AGE[i]+1
agecounts = []
for i in range(10,90):
    agecounts.append(AGE[i])
     

RACE = {}
for race in data.race:
    if race not in RACE:
        RACE[race] = 1
    else:
        RACE[race] = RACE[race] + 1        
whiteprop = float(RACE['white']) / float((RACE['white'] + RACE['black'] + RACE['other']))
blackprop = float(RACE['black']) / float((RACE['white'] + RACE['black'] + RACE['other']))
otherprop = float(RACE['other']) / float((RACE['white'] + RACE['black'] + RACE['other']))

male = 0
female = 0
for sex in data.sex:
    if sex == 'male':
        male += 1
    if sex == 'female':
        female += 1
maleprop = float(male) / float((male+female))
femaleprop = float(female) / float((male+female))        
print femaleprop
print whiteprop    
plt.subplot(3,1,1)
plt.bar(range(10,90), agecounts)
plt.title("Age Distribution")
plt.xlabel("age")
plt.ylabel("frequency")
plt.subplot(3,1,2)
plt.bar([1,2], [maleprop, femaleprop])
plt.ylim(1)
plt.title("Gender Distribution")
plt.xticks([1.5,2.5], ("Male", "Female"))
plt.ylabel("frequency")
plt.subplot(3,1,3)
plt.bar([1,2,3], [whiteprop, blackprop, otherprop], 0.5)
plt.xticks([1.25,2.25,3.25], ('White', 'Black', 'Other'))
plt.ylim(1)
plt.title("Race Distribution")      
plt.ylabel("frequency")
#plt.tight_layout