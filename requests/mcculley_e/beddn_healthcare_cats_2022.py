# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 08:11:57 2025

@author: stf45
"""

import pandas as pd

#%%

desc = pd.read_csv(r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\CategoryDescriptions20231127.txt', sep='\t')

# assign healthcare columns to usecols to subset beddn upon load
healthdesc = desc['Category'].loc[(desc['Domain'] == 'Healthcare')]  
healthcats = list(healthdesc)
counts = [f"t10_net_{cat.lower()}_c" for cat in healthcats]
densities = [f"t10_net_{cat.lower()}_d" for cat in healthcats]
colzip = list(zip(counts, densities))
usecols = list(sum(colzip,()))
usecols.insert(0, 'Year')
usecols.insert(0, 'tract10')

# load beddn
beddn = pd.read_csv(r"Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\Tract_ZCTA_Hierarchy\BEDDN_t10_measures_hier20240506.txt", sep='\t', dtype={'tract10':str}, usecols=usecols)

# subset for 2020
beddn22 = beddn.loc[beddn['Year']==2022]

#%% EXPORT TO CSV

beddn22.to_csv(r'C:\Users\stf45\Documents\BEDDN\requests\mcculley_e\tr10_BEDDN2022_healthcare_2022.csv', index=False)