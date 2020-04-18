from arctic import Arctic
import pandas as pd 
import time 

db = Arctic('localhost')
library = db['Finance']

start = time.time()

df = library.read('Trades').data

elapsed = time.time() - start

print(f'Arctic read took {elapsed} seconds')
