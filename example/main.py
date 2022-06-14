import pandas as pd

try:
    df = pd.read_csv('amazon.csv', thousands = '.')
except:
    print("File not found")

#Initial dataset
#print(df.to_string())

#Checking for empty entries
print(df.isna().sum())

