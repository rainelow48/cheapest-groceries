# Import libraries
import pandas as pd
import os

# Function to read csv and seach for an item 
# eg. item = 'taste the difference cookies'
# searchValues = ['taste', 'the', 'difference', 'cookies']

def searchItem(cat, categories, fileNames, searchValues):
    
    # Search all categories
    if (cat == 0):
        
        # Create empty dataframe
        df = pd.DataFrame({'Description': [],'Price/Unit': [],'Unit': [],'Price/Measure': [],'Measure': []})
        
        for i in categories:
            result = searchItem(i, categories, fileNames, searchValues)
            
            # Concatenate dataframe from different categories
            df = pd.concat([df, result])

        # Obtain duplicated items and length
        # duplicate = df.duplicated()
        # print(len(df[duplicate]))

        # Return list without duplicates
        return df.drop_duplicates()

    # Search specific category
    else:
        # Read csv file
        filename = fileNames[categories[cat]] + '.csv'
        data = pd.read_csv(os.getcwd()+ '\\csv files\\' + filename)

        # Apply filter, case insensitive (requires values in searchValues to be lower case too)
        filter = data['Description'].apply(lambda desc: all(word in desc.lower() for word in searchValues))
        
        # Obtain filtered items
        result = data[filter]
        
        # Print result out to user
        # if (result.empty):
        #     print("\nNothing was found in", categories[cat])
        # else:
        #     print("\nFound", len(result), "items in", categories[cat])
        #     print(result)
        
        return result

# Function to change price from xxp to 0.xx pounds
def toPounds(price):
    if ('p' in price):
        newprice = int(price[:-1])/100
        return float(newprice)
    else:
        return float(price)

# Function to convert all prices to pounds and sort in acending order
def sortItems(data):
    ppu = data['Price/Unit'].apply(lambda item: toPounds(item))     # Convert ppu to pounds
    data['Price/Unit'] = ppu        # Replace original ppu column with pound values

    ppm = data['Price/Measure'].apply(lambda item: toPounds(item))  # Convert ppm to pounds
    data['Price/Measure'] = ppm     # Replace original ppm column with pound values

    return data.sort_values(['Price/Unit', 'Price/Measure'])
