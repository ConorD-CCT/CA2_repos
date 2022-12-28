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

df = df[df['Area'].isin(['Ireland','Netherlands','France','Italy','Spain','Poland','Portugal'])]
df.head()

countries = df['Area'].unique()

plot1 = plt.figure(4)
for i in countries:
    plt.plot(df[df['Area'] == i]['Year'], df[df['Area'] == i]['Value'])
plt.title('Agricultural Expenditure in EU Countries')
plt.legend(countries, shadow=True)
plt.xticks(np.arange(2000, 2022, 2))


df = df[df["Year"].isin([2020]) == False]

gdpDF = pd.read_csv('EU_GDP.csv')
gdpDF = gdpDF[gdpDF['Area'].isin(['Ireland','Netherlands','France','Italy','Spain','Poland','Portugal'])]
gdpDF = gdpDF[gdpDF["Year"].isin([2020]) == False]
gdpDF.head()

plot2 = plt.figure(5)
for i in countries:
    spend = list(df[df['Area'] == i]['Value'])
    gdp = list(gdpDF[gdpDF['Area'] == i]['Value'])
    normalised = [(x / y)*100 for x, y in zip(spend, gdp)]
    plt.plot(gdpDF[gdpDF['Area'] == i]['Year'], normalised)

plt.title('Agricultural Expenditure - Perc. of GDP')
plt.legend(countries, shadow=True)
plt.xticks(np.arange(2000, 2022, 2))

plt.show()



