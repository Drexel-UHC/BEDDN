# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:33:53 2024

@author: stf45

This is a template script that allows the user to reformat Business Establishment
Data Derived from NETS (BEDDN) in order to link lat/longs to category and year
for spatial processing. Input files are tab delimited, outputs are csv. Outputs 
include files containing the following info for each category-year (n=8,415):
    
    1. DunsYearId (unique id for each DunsNumber-Year, made up at Drexel to 
                   de-identify raw data)
    2. AddressID  (unique id for each address in BEDDN, can be used to link to 
                   spatial dataset)
    3. Year
    4. Category   (this variable will read "BaseGroup" or "HighLevel", depending
                   on whether the file contains establishments that are categorized
                   as Base Groups, or Combination Categories/Thematic Constructs)
"""
#%%

import pandas as pd
import os

#%% ADD FILE PATHS

# file path to classified long with addresses file 
cl_add_file = r'\path\file.txt'

# file path to category descriptions file
desc_file = r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\CategoryDescriptions20231127.txt'

# file path to base group/high level crosswalk file
xwalk_file = r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\BG_CC_TC_Xwalk20231023.txt'

# file path to output FOLDER, which will be populated with years folders, which 
#will contain files for every category in that year
output_folder = r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\JamesPeter'

#%% READ IN FILES

# read in descriptions and xwalk files
desc = pd.read_csv(desc_file, sep='\t')
xwalk = pd.read_csv(xwalk_file, sep='\t', usecols=['BaseGroup', 'HighLevel'])

#%% USER INPUTS

# year of interest
years = range(1990,2023)

# use hierarchy? if unsure, use True
hierarchy = True

#%% READ IN CLASSIFIED LONG

cl_add = pd.read_csv(cl_add_file, sep='\t')

#%% MAKE LISTS OF CATEGORIES

# list base groups
basegroup_cats = desc.loc[desc['Type']=='Base Group']
basegroup_cats = list(basegroup_cats['Category'])
basegroup_cats.sort()

# list combination categories and thematic constructs
highlevel_cats = list(xwalk['HighLevel'].unique())
highlevel_cats.sort()

# list all categories
categories = list(desc['Category'])
categories.sort()

#%% LOOP THROUGH YEARS AND PROCESS BASEGROUPS

for year in years:
    print(f'processing: {year}')
    
    # CREATE YEAR FOLDER IN OUTPUT FOLDER
    outpath = os.path.join(output_folder, f'BEDDN_{year}') 
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    # SUBSET FOR YEAR
    year_sub = cl_add.loc[cl_add['Year'] == year]

    # APPLY HIERARCHY IF TRUE   
    if hierarchy == True:
        # join hierarchy
        year_sub = (year_sub
                       .merge(desc[['Category', 'Hierarchy']], left_on='BaseGroup', right_on='Category')
                       .drop(columns=['Category']))
        
        # sort by hierarchy, then drop all duplicates of dunsyear, keep first instance
        year_sub = (year_sub
                  .sort_values(by='Hierarchy')
                  .drop_duplicates(subset=['DunsYearId', 'Year'], keep='first')
                  .drop(columns=['Hierarchy'])
                  )
    else: 
        pass
        
    
    # LOOP THROUGH BASE GROUP CATEGORIES AND SUBSET/EXPORT
    print('processing base groups')
    for basegroup_cat in basegroup_cats:
        cat_sub = year_sub.loc[year_sub['BaseGroup'] == basegroup_cat]
        outfile = os.path.join(outpath, f'{basegroup_cat}_{year}.csv')
        cat_sub.to_csv(outfile, index=False)
        
    # LOOP THROUGH HIGH LEVEL CATEGORIES AND SUBSET/EXPORT
    print('processing high levels')
    for highlevel_cat in highlevel_cats:
        xwalk_sub = xwalk.loc[xwalk['HighLevel'] == highlevel_cat]
        outfile = os.path.join(outpath, f'{highlevel_cat}_{year}.csv')
        (year_sub
                 .merge(xwalk_sub, how='inner', on='BaseGroup')
                 # drop duplicate dunsyearid/HighLevel combos so they are not counted twice.
                 # this only matters when hierarchy = False
                 .drop_duplicates(subset=['DunsYearId', 'HighLevel'])
                 .drop(columns=['BaseGroup'])
                 .to_csv(outfile, index=False)
                 )
        
        
        
    
        
        