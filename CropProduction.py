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
import seaborn as sns

df = pd.read_csv('cropProduction.csv')





df = df[df['Area'].isin(['Ireland','Netherlands','France','Italy','Spain','Poland','Portugal','Germany'])]
area = df[df['Element'] == 'Area harvested']
yieldd = df[df['Element'] == 'Yield']
prod = df[df['Element'] == 'Production']
df.head()

countries = df['Area'].unique()

fig = plt.figure(1,figsize=(10,3))
[sns.lineplot(x=yieldd[yieldd['Area'] == i]['Year'], y=yieldd[yieldd['Area'] == i]['Value'], label=i) for i in countries]
plt.title('Yield')

fig2 = plt.figure(2,figsize=(10,3))
[sns.lineplot(x=prod[prod['Area'] == i]['Year'], y=prod[prod['Area'] == i]['Value'], label=i) for i in countries]
plt.title('Production')

fig3 = plt.figure(3,figsize=(10,3))
[sns.lineplot(x=area[area['Area'] == i]['Year'], y=area[area['Area'] == i]['Value'], label=i) for i in countries]
plt.title('Area')






