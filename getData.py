import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import csv

start = '2016-01-01'
end = '2019-01-01'

stocklist = []                                                                                                 
with open('stock_Name.csv','r') as f:
    reader = csv.reader(f)
    for name in reader:
         stocklist = name
print(stocklist)

for x in name:
    try:
        data = yf.download(x,start,end)
        data.Close.plot()
        data.to_csv('data/'+x+'.csv',encoding='utf-8', index=False)
#        if bool(int(input('save?'))):
#            data.to_csv('data/'+x+'.csv',encoding='utf-8', index=False)
#            print('saved')
#        else: 
#            print('not saved')
    except:
        print('no data for' +x+ 'found!') 
plt.show()
