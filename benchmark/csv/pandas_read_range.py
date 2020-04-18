import pandas as pd
import time 

start = time.time()

df = pd.read_csv('finance.csv')

df['unix'] = pd.to_datetime(df['unix'])
df.set_index('unix', inplace=True)

new_df = df[(df.index > '2020-01-01') & (df.index < '2020-01-02')]

elapsed = time.time() - start

print(f'read_csv took {elapsed} seconds')
