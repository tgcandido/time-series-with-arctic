from sqlalchemy import create_engine
import pandas as pd
import time

engine = create_engine('sqlite:///sqlite.db', echo=False)

start = time.time()

data = engine.execute("SELECT * FROM Trades WHERE unix > DATE('2020-01-01') AND unix < DATE('2020-01-02');").fetchall()
df = pd.DataFrame(data)

elapsed = time.time() - start

print(f'SQLite took {elapsed} seconds')

print(df.head())
print(df.tail())