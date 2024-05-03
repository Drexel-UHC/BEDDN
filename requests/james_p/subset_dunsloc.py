# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:05:13 2024

@author: stf45

Subset columns of DunsLocation for Peter James group.
"""

import pandas as pd

df = pd.read_csv(r'Z:\UHC_Data\NETS_UHC\NETS2022\Data\Final\DunsLocation20231207.txt', sep='\t', usecols=['AddressID', 'DisplayX', 'DisplayY', 'UHCMatchCodeRank'])

df.to_csv(r'D:\scratch\BEDDN_addressid_latlong20240503.csv', index=False)
