from sqlalchemy import create_engine
import pandas as pd
import time

engine = create_engine('sqlite:///sqlite.db', echo=False)

start = time.time()

data = engine.execute("SELECT * FROM Trades").fetchall()
df = pd.DataFrame(data)

elapsed = time.time() - start

print(f'SQLite took {elapsed} seconds')
