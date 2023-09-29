# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:49:21 2023

@author: stf45
"""

import pandas as pd

#%% LOAD DATA, SUBSET
df = pd.read_csv(r'\\files.drexel.edu\colleges\SOPH\Shared\UHC\Projects\NETS\Data\NETS2019_Python\BEDDN_tr10_measures20230914.txt', sep='\t', dtype={'tract10':str})

subset = df.loc[df['Year']==2019]
subset = subset[['tract10', 'Year', 't10_net_fsr_c', 't10_net_fsu_c']]

#%% EXPORT TO CSV
subset.to_csv(r'C:\Users\stf45\Documents\BEDDN\requests\akbar_nejad_yadzi_r\BEDDN2019_tr10_fsu_fsr_2019.csv', index=False)
