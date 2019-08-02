import numpy as np
import pandas as pd 
import csv
import yfinance as yf
import matplotlib as plt
import tensorflow as tf


#Paramter:
details = 6
stocks = 27
days = 762
start = '2016-01-01'
end = '2019-01-01'


dataSet = np.zeros((days,details,1))
print(dataSet.shape)
stocklist = []                                                                                                 
with open('stock_Name.csv','r') as f:
    reader = csv.reader(f)
    for name in reader:
         stocklist = name
print(stocklist)



for x in name:
    try:
        data = yf.download(x,start,end)
        temp = data.to_numpy()
        try:
            dataSet = np.dstack((dataSet,temp))
        except:
            print('append went wrong')
    except:
        print('no data for' +x+ 'found!') 

test_dataset  = tf.placeholder(tf.in32, [batch_size, num_steps])

lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size) 
