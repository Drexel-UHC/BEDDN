# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 11:54:28 2025

@author: stf45
"""

import pandas as pd

#%% LOAD BEDDN, SUBSET FOR 2020

desc = pd.read_csv(r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\CategoryDescriptions20231127.txt', sep='\t')
basegroups = desc['Category'].loc[(desc['Type'] == 'Base Group')]  
basegroups = list(basegroups)
densities = [f"t10_net_{cat.lower()}_d" for cat in basegroups]

usecols = ['tract10', 'Year'] + densities


beddn = pd.read_csv(r"Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\Tract_ZCTA_Hierarchy\BEDDN_t10_measures_hier20240506.txt", 
                    sep='\t', 
                    dtype={'tract10':str}, 
                    usecols=usecols)

beddn20 = (beddn.loc[beddn['Year']==2020]
           .drop(columns=['Year'])
           .set_index('tract10')
           ) 

#%% SUM ALL DENSITY COLS TO GET TOTAL ESTABLISHMENT DENSITY PER TRACT


sumcol = beddn20.iloc[:,2:].sum(axis=1)
sumcol.name = 't10_beddn_all_estab_d'
sumcol.to_csv(r'D:\scratch\t10_beddn_all_estab_d.csv')
