import numpy as np
import pandas as pd
import requests
from datetime import datetime
import csv
import glob
import os

path = 'D:/MIT Coursework/Thesis/DataFiles/'

#this makes some datasets super large - market cap, transactions per second, mempool count and size
url_list=['https://api.blockchain.info/charts/transaction-fees?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/transactions-per-second?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/cost-per-transaction?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/miners-revenue?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/market-price?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/avg-block-size?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/median-confirmation-time?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/mempool-size?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/mempool-count?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/market-cap?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/n-transactions?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/n-transactions-per-block?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/output-volume?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/my-wallet-n-users?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/hash-rate?timespan=15years&format=csv&sampled=false',
'https://api.blockchain.info/charts/difficulty?timespan=15years&format=csv&sampled=false']


filename_list = ['Transaction-Fees.csv',
'Transactions-Per-Second.csv',
'Cost-Per-Transaction.csv',
'Miners-Revenue.csv',
'Market-Price.csv',
'Avg-Block-Size.csv',
'Median-Confirmation-Time.csv',
'Mempool-Size.csv',
'Mempool-Count.csv',
'Market-Cap.csv',
'Number-of-Transactions.csv',
'Number-of-Transactions-Per-Block.csv',
'Output-Volume.csv',
'Wallet-User-Numbers.csv',
'Hash-Rate.csv',
'Difficulty.csv']

for i in range(0,len(url_list)):
    with requests.Session() as s:
        download = s.get(url_list[i])
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        data_list = list(cr)
    fieldname=filename_list[i][:-4]
    df = pd.DataFrame(data_list,columns=['DateTime',fieldname])
    df['DateTime'] = pd.to_datetime(df['DateTime']).apply(lambda x: x.date())
    df[fieldname]=pd.to_numeric(df[fieldname]) 
    df=df.groupby('DateTime').mean()
    df.to_csv(path+filename_list[i])

csv_files = glob.glob(os.path.join(path, "*.csv"))

all_data = pd.DataFrame(columns = ['DateTime'])

for f in csv_files:
    df = pd.read_csv(f)
    all_data=pd.merge(all_data,df,on='DateTime',how='outer')

all_data.DateTime = pd.to_datetime(all_data.DateTime)

energy=pd.read_csv('D:/MIT Coursework/Thesis/DataFiles/Energy/bitcoin-energy-consumption-index.csv')

energy.DateTime = pd.to_datetime(energy.DateTime)

all_data=pd.merge(all_data,energy,on='DateTime',how='outer')

all_data=all_data.sort_values(by=['DateTime'])
all_data=all_data.reset_index(drop=True)

all_data.to_csv(path+'ConsolidatedData.csv')
