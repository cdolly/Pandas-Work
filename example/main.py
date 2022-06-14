import pandas as pd

try:
    df = pd.read_csv('amazon.csv', thousands = '.')
except:
    print("File not found")

#Initial dataset
#print(df.to_string())

#Checking for empty entries
print(df.describe(include = "all"))

for x in df.index:
    if(df.loc[x, "number"] == 0):
        df.drop(labels = [x], axis = 0, inplace = True)
        
    
print(df.describe(include = "all"))

