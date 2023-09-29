# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:23:13 2023

@author: stf45
"""

import pandas as pd

#%%

desc = pd.read_csv(r'\\files.drexel.edu\colleges\SOPH\Shared\UHC\Projects\NETS\Data\NETS2019_Python\CategoryDescriptions20230613.txt', sep='\t')

# assign healthcare columns to usecols to subset beddn upon load
healthdesc = desc['Category'].loc[(desc['Domain'] == 'Healthcare') & (desc['Type'] == 'Base Group')]  
healthcats = list(healthdesc)
counts = [f"t10_net_{cat.lower()}_c" for cat in healthcats]
densities = [f"t10_net_{cat.lower()}_d" for cat in healthcats]
colzip = list(zip(counts, densities))
usecols = list(sum(colzip,()))
usecols.insert(0, 'Year')
usecols.insert(0, 'tract10')

# load beddn
beddn = pd.read_csv(r'\\files.drexel.edu\colleges\SOPH\Shared\UHC\Projects\NETS\Data\NETS2019_Python\BEDDN_tr10_measures20230914.txt', sep='\t', dtype={'tract10':str}, usecols=usecols)

# subset for 2019 
beddn19 = beddn.loc[beddn['Year']==2019]

#%% EXPORT TO CSV

beddn19.to_csv(r'C:\Users\stf45\Documents\NETS\Projects\McCulley_E\tr10_BEDDN2019_healthcare_2019.csv', index=False)
