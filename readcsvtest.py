import pandas as pd

# CSV filename
fileName = 'meatandfish.csv'

# Search items
search_values = ['Chicken', 'Breast', 'Thigh']

# Column names
col1 = 'Description'
col2 = 'Price per Unit'
col3 = 'Unit'
col4 = 'Price per Measure'
col5 = 'Measure'

# Read csv file into pandas dataframe
result = pd.read_csv(fileName)

print(result.Measure.unique())

# Filter items
filtered = result[col1].str.contains('|'.join(search_values))
print(result[filtered])

# Sort items by Price per Unit and Price per Measure
sortByPPU = result[filtered].sort_values(by = [col2])
sortByPPM = result[filtered].sort_values(by = [col4])


# print(sortByPPU.head(10))
# print(sortByPPM.head(10))
