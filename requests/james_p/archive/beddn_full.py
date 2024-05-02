# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:07:28 2024

@author: stf45

This script creates a file containing:
    DunsYearId
    AddressID
    Year
    BaseGroup

Had to do this in an unusual way because I couldn't simply get the DunsYearId
with the classified long file due to the azure db being down for the moment. 
"""

import pandas as pd

#%% ADD FILE PATHS

dm_file = r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\JamesPeter\DunsMove_WithId.txt'
cl_file = r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\ClassifiedLong20231127.txt'
desc_file = r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\CategoryDescriptions20231127.txt'

#%% READ IN DUNSMOVE, CREATE DUNSYEAR 

dm = pd.read_csv(dm_file, sep='\t', usecols=['DunsYearId', 'DunsNumber', 'AddressID', 'Year'], dtype={'DunsNumber':str, 'Year':str})
dm['DunsYear'] = dm['DunsNumber'] + '_' + dm['Year']

dm = dm.drop(columns=['DunsNumber'])

#%% READ IN CLASSIFIED LONG, MERGE WITH DUNSMOVE

cl = pd.read_csv(cl_file, sep='\t', usecols=['DunsYear', 'BaseGroup'])

dm = (dm
      .merge(cl)
      .drop(columns=['DunsYear'])
      )

del cl

# export to file
dm.to_csv(r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\ClassifiedLongWithAddresses.txt', sep='\t', index=False)

