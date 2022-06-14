import pandas as pd

df = pd.read_csv('data.csv')


#Basic Pandas functions

print(df.info()) #Prints informtaion about the dataset, including number of columns, rows, data types, and non null counts.
print(df.head(10)) #Prints the first 10 entries in the DataFrame.
print(df.tail(10)) #Prints the last 10 entries in the DataFrame.
