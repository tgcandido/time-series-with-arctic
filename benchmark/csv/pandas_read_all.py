import pandas as pd
import time 

start = time.time()

df = pd.read_csv('finance.csv')

df['unix'] = pd.to_datetime(df['unix'])
df.set_index('unix', inplace=True)

elapsed = time.time() - start

print(f'read_csv took {elapsed} seconds')
