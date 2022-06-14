import pandas as pd

df = pd.read_csv('data.csv')

print(df.info())
print(df.head(10))
print(df.tail(10))
