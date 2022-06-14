import sys
import pandas as pd
import googletrans

def printDataset(data):
    print(data.to_string())

def describeDataset(data):
    print(data.describe(include = "all"))

def deleteEmpty(data):
    for x in data.index:
        if(data.loc[x, "number"] == 0):
            data.drop(labels = [x], axis = 0, inplace = True)
        
    
def createSubset(data):
    fpm = data.groupby('month')['number'].sum()
    months_unique = list(data.month.unique())
    fpm = fpm.reindex(months_unique, axis=0)
    fpm = fpm.to_frame()
    fpm.reset_index(level = 0, inplace = True)
    translateMonths(data)

def translateMonths(data):
    translator = Translator() #create an object of Translator 
    for month in months_unique: 
        detected = translator.detect(month)     
        translated = translator.translate(month)     
        print(detected)     
        print(translated)     
        print("...")
        
    translator2 = Translator() #create a another new object of translator
    for x, m in enumerate(fpm['month']):
        translated = translator2.translate(m)  
        month1 = translated.text    
        fpm.at[i, 'month'] = month1
    print(fpm)

#Call functions below this point 
try: 
    df = pd.read_csv('amazon.csv', thousands = '.') #Try to read file and convert to DataFrame, throw error if not possible.
except:
    print("File not found")
    
deleteEmpty(df) #Delete the non-important data, aka months with zero fires.

createSubset(df) #Creates a subset of the DataFrame with only months and number of fires, translates them from portuguese to english, and then prints the DataFrame.

    
    
