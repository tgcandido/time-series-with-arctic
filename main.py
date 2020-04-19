from arctic import Arctic
import pandas as pd 

df = pd.read_csv('finance.csv')

df['unix'] = pd.to_datetime(df['unix'])
df.set_index('unix', inplace=True)

db = Arctic('localhost')
db.initialize_library('Finance')

library = db['Finance']
library.write('Trades', df)

new_ df = library.read('Trades').data

range_df = library.read('Trades', date_range=DateRange('2020-01-01', '2020-01-02')).data