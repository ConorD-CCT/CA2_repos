# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 23:21:06 2022

@author: cdillon
"""

import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
pio.renderers.default='browser'

df = pd.read_csv('EU_Agri_expenditure.csv')

df.head()
df = df[df["Year"].isin([2019]) == True]
df = df[df["Value"].isin([0]) == False]
countries = df['Area'].unique()
plt.bar(df['Area'],df['Value'])

gdpDF = pd.read_csv('EU_GDP.csv')
gdpDF = gdpDF[gdpDF['Area'].isin(countries)]
gdpDF = gdpDF[gdpDF["Year"].isin([2019]) == True]

df['GDP'] = list(gdpDF['Value'])




#%%

gdpDF.head()
fig = plt.figure(4,figsize=(10,3))
plt.scatter(df['Value'],df['GDP'])

#%%

fig = plt.figure(5,figsize=(10,5))
df['%ofGDP'] = [(x / y)*100 for x, y in zip(df['Value'],df['GDP'])]
dfSorted = df.sort_values(by=['%ofGDP'])
plt.ylabel('%')
plt.xticks(rotation='vertical')
plt.gcf().subplots_adjust(bottom=0.25)
plt.bar(dfSorted['Area'],dfSorted['%ofGDP'])
plt.title('2019 Agricultural Expenditure - Perc. of GDP')


#%%
fig = plt.figure(6,figsize=(10,5))
yield2019 = pd.read_csv('cropProduction.csv')
yield2019 = yield2019[yield2019["Year"].isin([2019]) == True]
yield2019 = yield2019[yield2019['Area'].isin(countries)]
yield2019 = yield2019[yield2019["Value"].isin([0]) == False]
yield2019 = yield2019[yield2019["Element"].isin(['Yield']) == True]

mergedDF = pd.merge(dfSorted,yield2019[['Value','Area']],on='Area')

plt.scatter(mergedDF['Value_x'],mergedDF['Value_y'])
mergedDF['Value_x'].corr(mergedDF['Value_y'])

