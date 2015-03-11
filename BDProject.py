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
def AgeGroup(data):
    AGE = {}     
    for i in range(10,90):
        AGE[i] = 0
        for ages in data.age:
            if i == ages:
                AGE[i] = AGE[i]+1
    agecounts = []
    for i in range(10,90):
        agecounts.append(AGE[i])
        
    return agecounts
     
## create race groups 
def RaceGroup(data):
    RACE = {}
    for race in data.race:
        if race not in RACE:
            RACE[race] = 1
        else:
            RACE[race] = RACE[race] + 1        
    # Proportions
    total = float((RACE['white'] + RACE['black'] + RACE['other']))
    whiteprop = float(RACE['white']) / total
    blackprop = float(RACE['black']) / total
    otherprop = float(RACE['other']) / total

    return whiteprop, blackprop, otherprop

## create sex groups
def SexGroup(data): 
    male = 0
    female = 0
    for sex in data.sex:
        if sex == 'male':
            male += 1
        if sex == 'female':
            female += 1
    # Proportions        
    maleprop = float(male) / float((male+female))
    femaleprop = float(female) / float((male+female))

    return maleprop, femaleprop        

        
## Creating income groups
def IncomeGroup(data):
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
            
    return incomegroups

def PlotAgeSexRace(data): 
    '''Returns 3 plots with age, sex, and race distributions.
        TO DO: make the y-axis go up to 1.0 '''
    age = AgeGroup(data)
    sex = SexGroup(data)
    race = RaceGroup(data)
    
    # Figure size
    plt.figure(1,(5,8))
        
<<<<<<< HEAD
    ageplot = plt.subplot(3,1,1)
    ageplot.bar(range(10,90), age)
    # Labels for age plot
    ageplot.title("Age Distribution")
    ageplot.xlabel("age")
    ageplot.ylabel("frequency")
    
    sexplot = plt.subplot(3,1,2)
    sexplot.bar([1,2], [sex[0], sex[1]])
    # labels for sex plot
    sexplot.title("Gender Distribution")
    sexplot.xticks([1.5,2.5], ("Male", "Female"))
    sexplot.ylabel("frequency")
    
    raceplot = plt.subplot(3,1,3)
    raceplot.bar([1,2,3], [race[0], race[1], race[2]], 0.5)
    raceplot.xticks([1.25,2.25,3.25], ('White', 'Black', 'Other'))
    raceplot.title("Race Distribution")      
    raceplot.ylabel("frequency")

def PlotIncome(data):
    '''Returns a plot with income distribution.
        TO DO: clear up x-axis labeling '''
    incomegroups = IncomeGroup(data)
    
    # Figure size
    plt.figure(2,(9,5))
    
    plt.bar(range(0,13,1), incomegroups, 1)
    plt.xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5], ('nan','<1k','1k-3k','3k-4k','4k-5k','5k-6k','6k-7k','7k-8k','8k-10k','10k-15k','15k-20k','20k-25k','>25k'))

PlotAgeSexRace(data)
PlotIncome(data)
=======
## Marital status
marriage = [0,0,0,0,0]
for marital in data.marital:
    if marital == 'NEVER MARRIED':
        marriage[0] += 1
    if marital == 'divorced':
        marriage[1] += 1
    if marital == 'married':
        marriage[2] += 1
    if marital == 'separated':
        marriage[3] += 1
    if marital == 'widowed':
        marriage[4] += 1
## Sexual orientation
orientation = [0,0,0,0]
for ornt in data.sexornt:
    if ornt == 'nan':
        orientation[0] +=1
    if ornt == 'Bisexual':
        orientation[1] +=1
    if ornt == 'Gay, lesban, or homosexual':
        orientation[2] +=1
    if ornt == 'Heterosexual or straight':
        orientation[3] +=1        



plt.figure(1,(5,8))        
plt.subplot(3,1,1)
plt.bar(range(10,90), agecounts)
plt.title("Age Distribution")
plt.xlabel("age")
plt.ylabel("frequency")
plt.subplot(3,1,2)
plt.bar([1,2], [maleprop, femaleprop])
##plt.ylim(1)
plt.title("Gender Distribution")
plt.xticks([1.5,2.5], ("Male", "Female"))
plt.ylabel("frequency")
plt.subplot(3,1,3)
plt.bar([1,2,3], [whiteprop, blackprop, otherprop], 0.5)
plt.xticks([1.25,2.25,3.25], ('White', 'Black', 'Other'))
##plt.ylim(1)
plt.title("Race Distribution")      
plt.ylabel("frequency")
#plt.tight_layout
plt.figure(2,(9,5))
plt.bar(range(0,13,1), incomegroups, 1)
plt.xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5], ('nan','<1k','1k-3k','3k-4k','4k-5k','5k-6k','6k-7k','7k-8k','8k-10k','10k-15k','15k-20k','20k-25k','>25k'))

plt.figure(3, (5,7))
plt.subplot(2,1,1)
plt.title("Marital Status")
plt.bar([0, 1, 2, 3, 4], marriage)
plt.xticks([0.5,1.5,2.5,3.5,4.5],("Never married","divorced","married","separated","widowed"))
plt.subplot(2,1,2)
plt.title("Sexual orientation")
plt.bar([0,1,2,3],orientation)
plt.xticks([0.5,1.5,2.5,3.5], ("nan","Bi","gay","straigt"))

>>>>>>> 4461a460928fe804c06933f110bbd2ffa1a00a99
