#These 3 imports allow for the compiler to be able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

#Basic Pandas functions
def basicFunctionsExample(): #Prints the DataFrame with some basic Pandas functions.
    df = pd.read_csv('data.csv') #Reads the comma seperated value file and transforms it into a Pandas DataFrame named df.
    #This dataset was obtained from W3Schools and can be found on their website.

    print(df.info()) #Prints informtaion about the dataset, including number of columns, rows, data types, and non null counts.
    print(df.head(10)) #Prints the first 10 entries in the DataFrame.
    print(df.tail(10)) #Prints the last 10 entries in the DataFrame.



#Cleaning datasets
def cleaningExample(num): #Num represents which example you'd like to view.

    if(num < 1 or num > 11):
      print("Please choose a correctly numbered example to view")
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

    if(num == 6):
      ddf['Date'] = pd.to_datetime(ddf['Date']) #Attempts to convert all cells in the "Date" column into dates.
      df.dropna(subset=['Date'], inplace = True)
      print(ddf.to_string()) #Prints the modified DataFrame. 
      #Same as prior example except removes all rows in the "Date" column containg "NaT".

    if(num == 7):
      ddf.loc[7,'Duration'] = 45 #Sets the incorrect value found in index position 7 from 450 to 45.
      print(ddf.to_string()) #Prints the modified DataFrame. 

    if(num == 8):
        
        for x in ddf.index: #Loops through every entry in the dirty DataFrame and if the duration is greater than 120,             it replaces said value with 120.
          if (ddf.loc[x, "Duration"] > 120):
            ddf.loc[x, "Duration"] = 120
        print(ddf.to_string()) #Prints the modified DataFrame

    if(num == 9):
        for x in ddf.index: #Loops through every entry in the dirty DataFrame and if the duration is greater than 120, deletes the row.
          if ddf.loc[x, "Duration"] > 120:
            ddf.drop(x, inplace = True)
          print(ddf.to_string()) #Prints the modified DataFrame


    if(num == 10):
      print(ddf.duplicated()) #Prints true for all rows which are duplicates of another row.

    if(num == 11):
      ddf.drop_duplicated(inplace = True) # Removes all duplicate entries from the DataFrame.
      print(ddf.to_string()) #Prints the modified DataFrame

#Analyzing datasets
def AnalyzingExample(num):
     if(num > 1 or num < 10):
        print("Please choose a correctly numbered example")
        return
     df = pd.read_csv('data.csv') #Reads the comma seperated value file and transforms it into a Pandas DataFrame named df.
     #This dataset was obtained from W3Schools and can be found on their website.

     ddf = pd.read_csv('dirtydata.csv') #Reads the comma seperated value file of error-filled data and transforms it into a Pandas DataFrame named ddf.
     #This dataset was obtained from W3Schools and can be found on their website.
                    
                    
     if(num == 1):
       print(df.corr()) #Prints the r values representing correlation between the columns.
     
     if(num == 2): #Draws a plot of the DataFrame
       df.plot()
       plt.show()
                    
       #Two lines to make the compiler to be able to draw:
       plt.savefig(sys.stdout.buffer)
       sys.stdout.flush()
      
     if(num == 3): #Prints a scatter plot of the DataFrame
       df.plot(kind = 'scatter', x = 'Duration', y = 'Calories') #Selects a Scatter plot and the Duration as the X and Calories as the Y.

       plt.show()

       #Two lines to make the compiler to be able to draw:
       plt.savefig(sys.stdout.buffer)
       sys.stdout.flush()
      
     if(num == 4): # Prints a histogram of the DataFrame
       df["Duration"].plot(kind = 'hist') # Selects a hisogram and plots the frequency of the Duration column.

       plt.show()

       #Two lines to make the compiler to be able to draw:
       plt.savefig(sys.stdout.buffer)
       sys.stdout.flush()

#Call any functions below this line in order to avoid non defined function errors during compilation.


