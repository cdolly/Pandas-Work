import pandas as pd


#Basic Pandas functions


def basicFunctionsExample():
  df = pd.read_csv('data.csv') #Reads the comma seperated value file and transforms it into a Pandas DataFrame named df.
  #This dataset was obtained from W3Schools and can be found on their website.
  
  print(df.info()) #Prints informtaion about the dataset, including number of columns, rows, data types, and non null counts.
  print(df.head(10)) #Prints the first 10 entries in the DataFrame.
  print(df.tail(10)) #Prints the last 10 entries in the DataFrame.

  
#Cleaning datasets
def cleaningExample():
    
#Call any functions below this line in order to avoid non defined function errors during compilation.
