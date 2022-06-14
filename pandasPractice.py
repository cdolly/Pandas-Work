import pandas as pd

#Basic Pandas functions
def basicFunctionsExample(): #Prints the DataFrame with some basic Pandas functions.
  df = pd.read_csv('data.csv') #Reads the comma seperated value file and transforms it into a Pandas DataFrame named df.
  #This dataset was obtained from W3Schools and can be found on their website.
  
  print(df.info()) #Prints informtaion about the dataset, including number of columns, rows, data types, and non null counts.
  print(df.head(10)) #Prints the first 10 entries in the DataFrame.
  print(df.tail(10)) #Prints the last 10 entries in the DataFrame.
  


  
#Cleaning datasets
def cleaningExample(num): #Num represents which example you'd like to view.
  
  if(num < 1 or num > 8):
    print("Please choose a correct example to view")
    return
 
  df = pd.read_csv('data.csv') #Reads the comma seperated value file and transforms it into a Pandas DataFrame named df.
  #This dataset was obtained from W3Schools and can be found on their website.
  
  ddf = pd.read_csv('dirtydata.csv') #Reads the comma seperated value file of error-filled data and transforms it into a Pandas DataFrame named ddf.
  #This dataset was obtained from W3Schools and can be found on their website.
  
  if(num == 1):
    new_df = df.dropna() #Creates a new DataFrame with the empty cells and their rows removed.
    print(new_df.to_string()) #Prints the new DataFrame.
  
  if(num == 2):
    df.fillna(130, inplace = True) #Replaces empty values in the DataFrame with the value 130, does not return a NEW DataFrame, only changes the original.
    print(df.to_string()) #Prints the modified DataFrame.
    
  if(num == 3):
    df["Calories"].fillna(130, inplace = True) #Replaces empty values in the "Calories" column with the value 130, does not return a new DataFrame.
    print(df.to_string()) #Prints the modified DataFrame.
    
  if(num == 4):
    x = df["Calories"].mean() #Creates a variable, X, that is the mean of all values in the "Calories" column. The same can be done with median and mode funtions.
    df["Calories"].fillna(x, inplace = True) #Replaces all empty cells in the "Calories" column with the value of x, which is the average of the "Calories" column.
    print(df.to_string()) #Prints the modified DataFrame.
    
  if(num == 5):
    ddf['Date'] = pd.to_datetime(ddf['Date']) #Attempts to convert all cells in the "Date" column into dates.
    print(ddf.to_string()) #Prints the modified DataFrame. 
    #The resulting output will contain "NaT" meaning "Not a Time", due to the intentional errors in the dataset.
    
#Call any functions below this line in order to avoid non defined function errors during compilation.


