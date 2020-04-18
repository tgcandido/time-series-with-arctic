from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///sqlite.db', echo=False)

df = pd.read_csv('finance.csv')
df['unix'] = pd.to_datetime(df['unix'])
df.set_index('unix', inplace=True)

df.to_sql('Trades', con=engine)
