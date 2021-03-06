from pymongo import MongoClient
import pandas as pd 
import time 
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["Finance"]
trades= db["Trades"]

start = time.time()

cursor = trades.find({})
df =  pd.DataFrame(list(cursor))

elapsed = time.time() - start

print(f'PyMongo query took {elapsed} seconds')
print(df.head())
print(df.tail())