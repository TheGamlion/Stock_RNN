import os
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import csv

API_KEY = 'CX5IL832J9PVYSA0'

ts = TimeSeries(key= API_KEY,output_format= 'pandas') 

#fetch data
# 1 file load needed stocks -> save into list
# export the data as name.csv

with open('stock_Name.csv','r') as f:
    reader = csv.reader(f)
    for name in reader:
        print(name)




#data,meta_data = ts.get_daily(symbol = 'NVDA',outputsize='compact')

