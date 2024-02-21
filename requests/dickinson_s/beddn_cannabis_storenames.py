# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:31:39 2023

@author: stf45
"""

import pandas as pd
import time
from datetime import datetime
#%%

print(f"Start Time: {datetime.now()}")
time_list = [0]
tic = time.perf_counter()

chunksize = 60000000
n = 303014511
compnames_reader = pd.read_csv(r'D:\NETS\NETS_2022\ProcessedData\BusinessInfo20231025.txt', sep='\t', usecols=['DunsNumber','Company','TradeName','SIC'], dtype={'DunsNumber':str,'SIC':str}, chunksize=chunksize)

cannafull = pd.DataFrame()
for c,chunk in enumerate(compnames_reader):
    canna = chunk.loc[chunk['SIC'].isin(['59939905', '59990909'])]
    cannafull = pd.concat([cannafull,canna])
    
    toc = time.perf_counter()
    t = toc - (sum(time_list) + tic)
    time_list.append(t)
    print('{}: chunk {} completed in {} minutes! {} chunks to go'.format(datetime.now().strftime("%H:%M:%S"),c+1, round(t/60, 2), round(n/chunksize-(c+1),2)))
    
runtime = 'total time: {} minutes'.format(round(sum(time_list)/60,2))
print(runtime)

#%%

cannagrouped = cannafull.loc[~cannafull.duplicated(['DunsNumber','Company','TradeName'])]

# do string search, grab dunsnumbers, find most recent sics of those dunsnumbers
# create new dataframe with the company names, dunsnumbers, and sics
regex = r"D?EL?IV?ER|(TO)? ?-?\bGO\b|TRANSPORT"
deliveryname = cannagrouped.loc[(cannagrouped['Company'].str.contains(regex)) | (cannagrouped['TradeName'].str.contains(regex))]

cannagrouped.to_csv(r'C:\Users\stf45\Documents\BEDDN\requests\dickinson_s\allcannabis_sic.csv', index=False)
deliveryname.to_csv(r'C:\Users\stf45\Documents\BEDDN\requests\dickinson_s\canna_deliverynames.csv', index=False)
