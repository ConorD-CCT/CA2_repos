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

# countries = ['Ireland','Netherlands','France','Italy','Spain','Poland','Portugal','Germany','Lithuania','Latvia','Sweden','Finland','Norway']
countries = ['Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Czech Republic', 'Germany', 'Denmark', 'Spain', 'Estonia', 'Finland', 'France', 'United Kingdom', 'Greece', 'Croatia', 'Hungary', 'Ireland', 'Italy', 'Lithuania', 'Luxembourg', 'Latvia', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Sweden']


# df = df[df['Area'].isin(['Ireland','Netherlands','France','Italy','Spain','Poland','Portugal','Germany'])]


crop = 'Blueberries'
# List of options



area = df[(df['Element'] == 'Area harvested') & (df['Item'] == crop)]
yieldd = df[(df['Element'] == 'Yield') & (df['Item'] == crop)]
prod = df[(df['Element'] == 'Production') & (df['Item'] == crop)]
df.head()

fig = plt.figure(1,figsize=(10,3))
[sns.lineplot(x=yieldd[yieldd['Area'] == i]['Year'], y=yieldd[yieldd['Area'] == i]['Value'], label=i) for i in countries]
plt.title('Yield')

# fig2 = plt.figure(2,figsize=(10,3))
# [sns.lineplot(x=prod[prod['Area'] == i]['Year'], y=prod[prod['Area'] == i]['Value'], label=i) for i in countries]
# plt.title('Production')

# fig3 = plt.figure(3,figsize=(10,3))
# [sns.lineplot(x=area[area['Area'] == i]['Year'], y=area[area['Area'] == i]['Value'], label=i) for i in countries]
# plt.title('Area')


#%%

df2019 = df[df["Year"].isin([2019]) == True]
df2019 = df2019[df2019["Value"].isin([0]) == False]
yield2019 = df2019[(df2019["Element"] == 'Yield') & (df2019['Item'] == crop)]



#%%

import geopandas as gpd
import plotly.express as px
import pycountry

def getCodes(countries):
    codes = []
    # Iterate over the list of countries
    for country in countries:
        # Get the country object for the current name
        country_obj = pycountry.countries.get(name=country)
    
        # Extract the alpha-2 code from the country object
        code = country_obj.alpha_3
    
        # Add the code to the list
        codes.append(code)
    return codes 

countryCodes = getCodes(yield2019['Area'])

fig = px.choropleth(yield2019,
                     locations=countryCodes,
                     color='Value',
                     hover_name='Area')
fig.update_layout(
    title_text=crop+' yield per country in 2019',
    geo_scope='europe')
fig.show()







#%%






#%%

rainfallDF = pd.read_csv('average-precipitation-per-year.csv')
rainfallDF = rainfallDF.groupby(['Entity']).max()

rainfallDF = rainfallDF[rainfallDF.index.isin(countries) == True]
rainfallDF['Area'] = rainfallDF.index

#%%

yieldVSRain = pd.merge(rainfallDF[['Area','Average precipitation in depth (mm per year)']],yield2019[['Area','Value']], on='Area')
fig4 = plt.figure(4)
plt.scatter(yieldVSRain['Average precipitation in depth (mm per year)'],yieldVSRain['Value'])

for i, label in enumerate(yieldVSRain['Area']):
    plt.annotate(label,(yieldVSRain['Average precipitation in depth (mm per year)'][i],yieldVSRain['Value'][i]))
    
plt.show()

print(yieldVSRain['Average precipitation in depth (mm per year)'].corr(yieldVSRain['Value']))



