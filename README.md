# cheapest-groceries
## Search through Sainsbury's (UK supermarket) website for groceries of your choice!

<ul>
  <li>Search from more than 25,000 items from 14 different categories</li>
  <li>Get name and price details in a list: No need to scroll through many pages with images</li>
  <li>Only get the item you search for: No sponsored/featured/recommended items</li>
  <li>Order them by ascending price per unit and price per measure</li>
</ul>


### 1. Setting up
The following packages are required: `bs4`, `requests`, `csv`, `datetime`, `time`, `pandas`, `os`
You will need to download the following files into the same folder:
  <ul>
    <li>main.py</li>
    <li>sainsvar.py</li>
    <li>updatecsv.py</li>
    <li>searchcsv.py</li>
    <li>userinteraction.py</li>
  </ul>


### 2. Initial run
Follow the steps below to get data from Sainsbury's webpage as csv files:

#### A. Get all items from Sainsbury's website
1. Run main.py: On command prompt `C:\Users\...>python main.py` or on your IDE
2. When prompted to select category, select 'All'
```
*** Welcome to Sainsbury's search function! ***


Please select a category to search item:
0 : All
1 : Fruits and Vegetables
2 : Meat and Fish
3 : Dairy, eggs and Chilled
4 : Bakery
5 : Frozen
6 : Food Cupboard
7 : Household
8 : Drinks
9 : Beauty and Cosmetics
10 : Toiletries
11 : Home
12 : Baby and Toddler
13 : Pet
14 : Price Lock

Your selection (0-14): 0
```
3. When prompted to update csv files, select 'Y': 
`Do you wish to update csv files? (Y/N): y`
4. When prompted for confirmation, select 'Y': 
`This might take a long while (10-15min). Do you wish to proceed? (Y/N): y`

This process will take about 10-20min.
```
All csv files are updating...
All csv files has been updated!
---- 652.82 seconds ----
```
5. When all files are updated, search any item you want (or just hit enter):
`Please enter item to search for: crisps`

#### B. Get essential items from Sainsbury's website
In main.py, change `searchAll = True` to `searchAll = False` and repeat steps 1-3 above. This will take less than a minute.
```
*** Welcome to Sainsbury's search function! ***


Please select a category to search item:
0 : All
1 : Fruits and Vegetables
2 : Meat and Fish
3 : Dairy, eggs and Chilled
4 : Bakery
5 : Frozen
6 : Food Cupboard
7 : Household

Your selection (0-7): 0

You have selected: All
Do you wish to update csv files? (Y/N): y
Updating file(s)...
All csv files has been updated!
---- 28.96 seconds ----
```

### 3. Customize settings
Under main.py, you can customize the following:

#### A. Search domain
Set your search domain to Sainsbury's Essentials items, Sainsbury's All items or get prompted to choose your search domain every time you search.
```
searchAll = True              # Sets search domain to All items
searchAll = False             # Sets search domain to Essential items
searchAll = searchDomain()    # Let user set search domain
```

#### B. Update csv
Set a limit on how old your csv files can be (in days) and get prompted to update your csv files if they are too old:
```
days = 0                     # Set to 0 to get a prompt every time you run main.py
```

#### C. Length of result
Set your desired length of result to print: 
`length = 150`

### 4. Start searching
Run main.py and search for any item!
```
Please enter item to search for: crisps
Found  151 items in All
                                            Description  Price/Unit  Unit  Price/Measure Measure
32    Kiddylicious Apple Fruit Crisps Snack 12g 12 M...        0.60  unit           5.00    100g
2639          Walkers Baked Cheese & Onion Crisps 37.5g        0.75  unit           2.00    100g
2852            Walkers Baked Ready Salted Crisps 37.5g        0.75  unit           2.00    100g
2383           Popchips Barbeque Potato Chip Crisps 23g        0.75  unit           3.26    100g
7178                       Rymut Corn Sticks Crisps 80g        0.80  unit           1.00    100g
...                                                 ...         ...   ...            ...     ...
1488              Walkers Classic Variety Crisps 24x25g        3.00  unit           0.50    100g
4112                Walkers Meaty Variety Crisps 24x25g        3.00  unit           0.50    100g
576                    Hula Hoops Variety Crisps 12x24g        3.00  unit           1.04    100g
1764                  Hula Hoops Original Crisps 12x24g        3.00  unit           1.04    100g
1769          Pom-Bear Original Multipack Crisps 12x13g        3.00  unit           1.92    100g

[151 rows x 5 columns]
```
