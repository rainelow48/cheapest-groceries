import pandas as pd

# Dictionary of categories
categories = {
    1 : 'Fruits and Vegetables',
    2 : 'Meat and Fish',
    3 : 'Dairy, eggs and Chilled',
    4 : 'Bakery',
    5 : 'Frozen',
    6 : 'Food Cupboard',
    7 : 'Household'
    # 8 : 'Drinks'
}

# Dictionary of filenames
fileNames = {
    'Fruits and Vegetables': 'fruitandveg',
    'Meat and Fish': 'meatandfish',
    'Dairy, eggs and Chilled': 'dairyeggsandchilled',
    'Bakery': 'bakery',
    'Frozen': 'frozen',
    'Food Cupboard': 'foodcupboard',
    'Household': 'household',
    'Drinks': 'drinks'
}

# Search items
search_values = ['Chicken', 'Breast', 'Thigh']

# Column names
col1 = 'Description'
col2 = 'Price per Unit'
col3 = 'Unit'
col4 = 'Price per Measure'
col5 = 'Measure'


for i in categories:
    fileName = fileNames[categories[i]] + '.csv'

    # Read csv file into pandas dataframe
    result = pd.read_csv(fileName)

    print(result.Unit.unique())
    print(result.Measure.unique())

    # # Filter items
    # filtered = result[col1].str.contains('|'.join(search_values))
    # print(result[filtered])

    # # Sort items by Price per Unit and Price per Measure
    # sortByPPU = result[filtered].sort_values(by = [col2])
    # sortByPPM = result[filtered].sort_values(by = [col4])


    # print(sortByPPU.head(10))
    # print(sortByPPM.head(10))
