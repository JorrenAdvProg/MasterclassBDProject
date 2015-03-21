# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:33:33 2015

@author: Matthijsmeijers
"""
import matplotlib.pyplot as plt

def NumberofBelievers(Religionlist, belief):
    year = 1972
    Believers = []
    for i in range(28):
        if year == 1979 or year == 1981 or year == 1984 or year == 1986 or year ==1992:
            year += 1
        number = len(Religionlist[str(year)][Religionlist[str(year)] == belief])
        Believers.append(number)
        
        year += 1
        if year > 1994:
            year += 1
            
    return Believers
    
def listofyears():
    year = 1972
    listofyears = []
    for i in range(28):
        if year == 1979 or year == 1981 or year == 1984 or year == 1986 or year ==1992:
            year += 1
        listofyears.append(year)
        year += 1
        if year > 1994:
            year += 1
    return listofyears

def Retrievedistribution(column):
    dictionary = {}
    population = 0
    for value in column:
        if value in dictionary:
            dictionary[value] += 1
        else:
            dictionary [value] = 1
        if value != 0 and value != 'nan':
            population += 1            
        
    
    listoffrequencies = dictionary.values()
        
    
        
    

def Loopoveryears(Religionlist, belief, others):
    year = 1972
    Distribution = []
    for i in range(28):
        if year == 1979 or year == 1981 or year == 1984 or year == 1986 or year ==1992:
            year += 1
        population = 0
        believers = 0
        for believer in Religionlist[str(year)]:
            if believer == belief:
                believers += 1
            if believer != 0:
                population += 1
            
            if belief == 'other':
                if believer in others:
                    believers +=1
                    
                        
        
        Distribution.append(float(believers)/float(population))
        
        year += 1
        if year > 1994:
            year += 1
            
    return Distribution
                
def Religionplots(Religionlist, beliefs, listofyears, others):
    Numberofbeliefs = len(beliefs)
    for i, belief in enumerate(beliefs):
        Distribution = Loopoveryears(Religionlist, belief, others)
        plt.figure(1,(8,25))
        plt.subplot(Numberofbeliefs,1,i+1)
        plt.plot(listofyears, Distribution)
        plt.ylabel("Probability")
        plt.xlabel("Year")
        plt.title(belief)
        plt.tight_layout()
        
        
    
        
def plotrates(listoflist, names):
    
    for i in range(len(listoflist)):
        for j in range(1, len(listoflist[i])):
            listoflist[i][j-1] = listoflist[i][j]-listoflist[i][j-1]
        plt.figure(1,(8,10))
        plt.subplot(len(listoflist),1,i+1)
        plt.plot(listoflist[i])
        plt.title(names[i])
            
        