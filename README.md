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
Follow the steps below to get data from Sainsbury's webpage as csv files

#### Get all items from Sainsbury's website
<ol>
  <li>Run main.py</li>
Run on command prompt `C:\Users\...>python main.py` or on your IDE
  <li>When prompted to select category, select 'All' (enter 0)</li>
  <li>When prompted to update csv files, select 'Y' (enter y)</li>
  <li>When prompted for confirmation, select 'Y' (enter y)</li>
This process will take about 10-20min
  <li>When all files are updated, search anything you want (or just hit enter)</li>
</ol>
#### Get essential items from Sainsbury's website
In main.py, change `searchAll = True` to `searchAll = False` and repeat steps 1-3 above. This will take less than a minute.

### 3. Customize settings
Under main.py, you can customize the following:
  <ul>
    <li>Search domain</li>
    Set your search domain to Sainsbury's Essentials items or Sainsbury's All items [OR] Get prompted to choose your search domain using searchDomain() function
    <li>Update csv</li>
    Set a limit on how old your csv files can be [OR] Get prompted to update your csv files if they are too old
    <li>Length of result</li>
    Set your desired length of result to print


### 4. Start searching!
Select your search domain, category and search for any item!
