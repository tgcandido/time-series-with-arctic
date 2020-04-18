import pymongo
import pandas as pd 
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["Finance"]
trades= db["Trades"]

df = pd.read_csv('finance.csv')
df['unix'] = pd.to_datetime(df['unix'])

trades.create_index([ ("unix", 1) ])
trades.insert_many(df.to_dict('records'))