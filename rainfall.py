# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 15:57:16 2022

@author: cdillon
"""

import os
import pandas as pd
import numpy as np
import csv
import pycountry

#%%
# determine station ID's
# countries = ['Ireland','Netherlands','France','Italy','Spain','Poland','Portugal']
countries = ['Slovenia']

# List to store the country codes


def getCodes(countries):
    codes = []
    # Iterate over the list of countries
    for country in countries:
        # Get the country object for the current name
        country_obj = pycountry.countries.get(name=country)
    
        # Extract the alpha-2 code from the country object
        code = country_obj.alpha_2
    
        # Add the code to the list
        codes.append(code)
    return codes 

countryCodes = getCodes(countries)

#%%

# Open the text file in read mode
with open('ECA_blend_rr/stations.txt', 'r',encoding='utf-8') as f:
    # Read the contents of the file
    text = f.read()

# Split the text into a list of lines
lines = text.split('\n')

# Remove the first n lines
n = 19
for i in range(n):
    lines.pop(0)
    
# Split each string on the comma character to create a list of lists
data_lists = [row.split(',') for row in lines]

# Create a DataFrame from the list of lists
df = pd.DataFrame(data_lists, columns=['STAID', 'STANAME', 'CN','LAT','LON','HGHT'])

#%%
# Build dictionary of countries containing station IDs. Build list of all stations.
stationDict = {}

for i in countryCodes:
    stationDict[i] = df[df['CN'] == i+'  ']

stationIDList = []
for i in stationDict:
    stationIDList.extend(stationDict[i]['STAID'])
stationIDList = [s.replace(' ', '') for s in stationIDList]  

#%%
dataDir = os.listdir('ECA_blend_rr')
for i in ['elements.txt','sources.txt','stations.txt']:
    dataDir.remove(i)
dataDirKeep = []    
for i in range(len(dataDir)):
    for j in stationIDList:
        if dataDir[i].endswith(j+'.txt'):
            dataDirKeep.append(dataDir[i])

            
#%%

#Load data into Python environment
rainfallDict = {}        
for j in dataDirKeep:  
# Open the text file in read mode
    with open('ECA_blend_rr/'+j, 'r',encoding='utf-8') as f:
        # Read the contents of the file
        text = f.read()
    
    # Split the text into a list of lines
    lines = text.split('\n')
    
    # Remove the first n lines
    n = 21
    for i in range(n):
        lines.pop(0)
        
    # Split each string on the comma character to create a list of lists
    data_lists = [row.split(',') for row in lines]
    
    # Create a DataFrame from the list of lists
    rainDF = pd.DataFrame(data_lists, columns=['STAID', 'SOUID', 'DATE','RR','Q_RR'])
    rainfallDict[j] = rainDF

#%%
# Remove dates before 1961
for i in rainfallDict:
    rainfallDict[i]['DATE'] = pd.to_datetime(rainfallDict[i]['DATE'],format='%Y%m%d')

    rainfallDict[i]['RR'] = rainfallDict[i]['RR'].replace(['-9999',None], np.nan)
    # rainfallDict[i]['RR'] = list(rainfallDict[i]['RR']).convert_objects(convert_numeric=True)
    rainfallDict[i].dropna(axis=0,how='any')
 

