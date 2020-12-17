# Import required variables
from sainsessvar import categories, fileNames

# Import libraries
import pandas as pd

# Function to read csv and seach for an item 
# eg. item = 'taste the difference cookies'
# searchValues = ['taste', 'the', 'difference', 'cookies']

def searchEssentials(cat, searchValues):

    # Search all categories
    if (cat == 0):
        for i in categories:
            searchEssentials(i, searchValues)

    # Search specific category
    else:
        # Read csv file
        filename = fileNames[categories[cat]] + '.csv'
        data = pd.read_csv(filename)

        # Apply filter, case insensitive
        filter = data['Description'].apply(lambda desc: all(word in desc.lower() for word in searchValues))
        
        # Obtain filtered items
        result = data[filter]
        
        if (result.empty):
            print("\nNothing was found in", categories[cat])
        else:
            print("\nFound", len(result), "items in", categories[cat])
            print(result)
            