import sys
import pandas as pd
import googletrans

def printDataset(data):
    print(data.to_string())

def describeDataset(data):
    print(data.describe(include = "all"))

def deleteEmpty(data):
    for x in data.index: #Loops through all entries in the DataFrame, deleting all rows which the number of fires is equal to 0.
        if(data.loc[x, "number"] == 0):
            data.drop(labels = [x], axis = 0, inplace = True)
        
    
def createSubset(data):
    fpm = data.groupby('month')['number'].sum() #Creates the subset containing the months and the amount of fires per month.
    months_unique = list(data.month.unique()) #Creates a series of the unique months
    fpm = fpm.reindex(months_unique, axis=0) #reorders the months in the correct order, instead of alphabetically.
    fpm = fpm.to_frame() #Converts the Series to a DataFrame.
    fpm.reset_index(level = 0, inplace = True) #Resets the index to 0-11 instead of using the Months as the index.
    translateMonths(data)

def translateMonths(data):
    translator = Translator() #create a  new object of translator
    for x, m in enumerate(fpm['month']): #For every index, x, and month, m.
        translated = translator.translate(m)  #Translates the month, m, from portuguese to english
        month1 = translated.text    #Saves the value of translated to a variable
        fpm.at[x, 'month'] = month1 #Sets the value at index x, to the correct translated value
    printDataset(fpm) #Prints the subset

#Call functions below this point 
try: 
    df = pd.read_csv('amazon.csv', thousands = '.') #Try to read file and convert to DataFrame, throw error if not possible.
except:
    print("File not found")
    
deleteEmpty(df) #Delete the non-important data, aka rows containing months with zero fires.

createSubset(df) #Creates a subset of the DataFrame with only months and number of fires, translates them from portuguese to english, and then prints the DataFrame.

    
    
