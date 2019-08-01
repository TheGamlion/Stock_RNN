import os
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import csv
import matplotlib.pyplot as plt

API_KEY = 'CX5IL832J9PVYSA0'
plt.close('all')

ts = TimeSeries(key= API_KEY,output_format= 'pandas') 

stocklist = []
with open('stock_Name.csv','r') as f:
    reader = csv.reader(f)
    for name in reader:
        stocklist = name

stock=[] 
for x in name:
    data,meta_data = ts.get_daily(symbol=x,outputsize='full')
    data.to_csv('data/'+x+'.csv',encoding='utf-8', index=False)    
    stock.append(data)

for s in stock:
     s['1. open'].plot()
plt.show()
