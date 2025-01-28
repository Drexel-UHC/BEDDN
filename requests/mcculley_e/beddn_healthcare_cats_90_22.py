# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:58:33 2025

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


#%% EXPORT TO CSV

beddn.to_csv(r'C:\Users\stf45\Documents\BEDDN\requests\mcculley_e\tr10_BEDDN2022_healthcare_90_22.csv', index=False)