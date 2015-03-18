# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:56:46 2015

@author: jorrenbosga
"""
import pandas as pd

def Filter(startyear, category):
    '''This function loads all complete files from a certain period, filters
    them on a certain category and saves the result as a csv file.'''
    year = startyear
    filtered_data = {}
    for i in range((2014 - startyear) / 2 + 1):
        data = pd.io.stata.read_stata("GSS" + str(startyear) + ".DTA")
        if category == religion:
            religlist  = list(data.relig)
            filtered_data[str(year)] = religlist
        if category == beliefstrength:
            belistrlist = list(data.reliten)
            filtered_data[str(year)] = belistrlist
        # in case of more categories, add them here.
        year += 2
        

    # the code below writes the dictionary to a .pkl file           
    filtered = pd.DataFrame(filtered_data, columns = ["2010", "2012", "2014"])
    filtered.save("DATA" + str(startyear) + '_' + str(year) + '_' + str(category))
        
    return
        

