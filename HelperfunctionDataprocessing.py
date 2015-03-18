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
        
        
def plotrates(listoflist, names):
    
    for i in range(len(listoflist)):
        for j in range(1, len(listoflist[i])):
            listoflist[i][j-1] = listoflist[i][j]-listoflist[i][j-1]
        plt.figure(1,(8,10))
        plt.subplot(len(listoflist),1,i+1)
        plt.plot(listoflist[i])
        plt.title(names[i])
            
        