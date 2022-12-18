# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:02:59 2022

@author: cdillon
"""

import os 
import pandas as pd
import plotly.express as px

df = pd.read_csv('AQA04.20221215204045.csv')


print(df.value_counts())


# Total of all years, all crops
# fig = px.histogram(df,x = 'Type of Crop',y = 'VALUE')
# fig.show()


dfTotal = df[df['Type of Crop']=='Total wheat, oats and barley']
dfTotalProd = dfTotal[dfTotal['Statistic Label']=='Crop Yield per Hectare']

fig = px.line(dfTotalProd,x = 'Year',y = 'VALUE')
fig.show()