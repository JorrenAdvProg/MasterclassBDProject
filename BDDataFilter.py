# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:56:46 2015

@author: jorrenbosga
"""
import pandas as pd

def Filter(startyear, category):
    '''This function loads all complete files from a certain period, filters
    them on a certain category and saves the result as a Dataframe file.'''
    year = startyear
    filtered_data = {}
    years = []
    for i in range(28):
        if year == 1979 or year == 1981 or year == 1984 or year == 1986 or year ==1992:
            year += 1
        years.append(str(year))
        print years
        data = pd.io.stata.read_stata("GSS" + str(year) + ".DTA")
        if category == "religion":
            religlist  = list(data.relig)
            filtered_data[str(year)] = religlist
        if category == "beliefstrength":
            
            belistrlist = list(data.reliten)
            filtered_data[str(year)] = belistrlist

        if category == "premarsex":
            premarsxlist  = list(data.premarsx)
            filtered_data[str(year)] = premarsxlist

        # in case of more categories, add them here.
        year += 1
        if year > 1994:
            year += 1
        
    #Make the lists in the dictionary of equal length works at least for religion
    lengths = []
    for values in filtered_data.values():
        lengths.append(len(values))
    maxlength = max(lengths)    
    for values in filtered_data.values():
        if len(values) < maxlength:
            for i in range(maxlength - len(values)):
                values.append(0)
                
    # the code below writes the dictionary to a .pkl file           
    filtered = pd.DataFrame(filtered_data, columns = years)
    filtered.to_pickle("DATA" + str(startyear) + '_' + str(year) + '_' + str(category))
        
    return
        
## load with pandas.io.pickle.read_pickle(pathfile)

