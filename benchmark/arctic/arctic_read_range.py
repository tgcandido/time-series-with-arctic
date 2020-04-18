from arctic import Arctic
import pandas as pd 
import time 
from arctic.date import DateRange

db = Arctic('localhost')
library = db['Finance']

start = time.time()

df = library.read('Trades', date_range=DateRange('2020-01-01', '2020-01-02')).data

elapsed = time.time() - start

print(f'Arctic read  took {elapsed} seconds')

print(df.head())
print(df.tail())