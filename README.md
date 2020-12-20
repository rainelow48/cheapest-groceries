# cheapest-groceries
## Search through Sainsbury's (UK supermarket) website for groceries of your choice!

<ul>
  <li>Search from more than 25,000 items from 14 different categories</li>
  <li>Get name and price details in a list: No need to scroll through many pages with images</li>
  <li>Only get the item you search for, no sponsored/featured/recommended items</li>
  <li>Order them by ascending price per unit and price per measure</li>
</ul>


### 1. Setting up
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
1. Run main.py\
Run on command prompt `C:\Users\...>python main.py` or on your IDE\
2. When prompted to select category, select 'All' (enter 0)\
`Do you wish to update csv files? (Y/N): y`\
3. When prompted to update csv files, select 'Y' (enter y)\
`This might take a long while (10-15min). Do you wish to proceed? (Y/N): y`\
4. When prompted for confirmation, select 'Y' (enter y)\
This process will take about 10-20min\
```
All csv files are updating...
All csv files has been updated!
---- 652.82 seconds ----
```
5. When all files are updated, search anything you want (or just hit enter)\
`Please enter item to search for:`

#### B. Get essential items from Sainsbury's website
In main.py, change `searchAll = True` to `searchAll = False` and repeat steps 1-3 above. This will take less than a minute.

### 3. Customize settings
Under main.py, you can customize the following:

#### Search domain
Set your search domain to Sainsbury's Essentials items or Sainsbury's All items [OR] Get prompted to choose your search domain using searchDomain() function

#### Update csv
Set a limit on how old your csv files can be [OR] Get prompted to update your csv files if they are too old

#### Length of result
Set your desired length of result to print


### 4. Start searching!
Run main.py and search for any item!
