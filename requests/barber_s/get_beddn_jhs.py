# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:55:54 2024

@author: stf45
"""

import pandas as pd

#%% FILL IN REQUESTED PARAMETERS

# assign requested columns
basegroups = ['KCT', 'URG', 'REL', 'LIB', 'SCN', 'BNK', 'CCH', 'DLR', 'POS', 'FIR', 'POL']
highlevels = ['CNA', 'SMA', 'AEC', 'AMB', 'CMB', 'HOS', 'SRV', 'PBN']

# assign requested years
years = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2022]

#%% assign requested geographic boundaries

counties = ['28089', '28049', '28121']

#%%

desc = pd.read_csv(r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\CategoryDescriptions20231127.txt', sep='\t')
xwalk = pd.read_csv(r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\BG_CC_TC_Xwalk20231023.txt', sep='\t')

# check conflicts
for highlevel in highlevels:
    check = xwalk.loc[xwalk['HighLevel'] == highlevel]
    conflicts = set(check['BaseGroup']).intersection(basegroups)
    if len(conflicts) > 0:
        print(f'conflict: {highlevel} contains {conflicts}')

# assign columns to usecols to subset beddn upon load
cats = basegroups + highlevels
counts = [f"t10_net_{cat.lower()}_c" for cat in cats]
densities = [f"t10_net_{cat.lower()}_d" for cat in cats]
colzip = list(zip(counts, densities))
usecols = list(sum(colzip,()))
usecols.insert(0, 'Year')
usecols.insert(0, 'tract10')

#%% LOAD BEDDN

beddn = pd.read_csv(r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\Tract_ZCTA_Hierarchy\BEDDN_t10_measures_hier20240506.txt', sep='\t', dtype={'tract10':str}, usecols=usecols)

#%% SUBSET FOR REQUESTED YEARS

beddnsubset = beddn.loc[beddn['Year'].isin(years)]
beddnsubset = beddnsubset.loc[beddnsubset['tract10'].str[:5].isin(counties)]

#%% pivot to wide

# Pivot the dataframe by 'Year', creating a multi-index column
beddnsubwide = beddnsubset.pivot_table(index='tract10', columns='Year', aggfunc='first')
    
# Flatten the multi-index columns and append the year to the variable names
beddnsubwide.columns = [f'{col[0]}_{col[1]}' for col in beddnsubwide.columns]

#%% EXPORT TO CSV

beddnsubset.to_csv(r'C:\Users\stf45\Documents\BEDDN\requests\barber_s\tr10_BEDDN2022_jhs.csv', index=False)
beddnsubwide.to_csv(r'C:\Users\stf45\Documents\BEDDN\requests\barber_s\tr10_BEDDN2022_jhs_wide.csv')
