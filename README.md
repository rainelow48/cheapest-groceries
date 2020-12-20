# cheapest-groceries
<h2>Search through Sainsbury's (UK supermarket) website for groceries of your choice!</h2>

<ul>
  <li>Search from more than 25,000 items from 14 different categories</li>
  <li>Get name and price details in a list: No need to scroll through many pages with images</li>
  <li>Only get the item you search for, no sponsored/featured/recommended items</li>
  <li>Order them by ascending price per unit and price per measure</li>
</ul>


<h3>1. Setting up</h3>
<p>You will need to download the following files into the same folder:
  <ol>
    <li>main.py</li>
    <li>sainsvar.py</li>
    <li>updatecsv.py</li>
    <li>searchcsv.py</li>
    <li>userinteraction.py</li>
  </ol>
</p>

<h3>2. Initial run</h3>
<h4>Get all items from Sainsbury's website</h4>
<ol>
  <li>Run main.py</li>
  <p> Run on command prompt `C:\Users\...>python main.py` or on your IDE</p>
  <li>When prompted to select category, select 'All' (enter 0)</li>
  <li>When prompted to update csv files, select 'Y' (enter y)</li>
  <li>When prompted for confirmation, select 'Y' (enter y)</li>
  <p>This process will take about 10-20min</p>
  <li>When all files are updated, search anything you want (or just hit enter)</li>
</ol>
<h4>Get essential items from Sainsbury's website</h4>
<p>In main.py, change `searchAll = True` to `searchAll = False` and repeat steps 1-3 above. This will take less than a minute.</p>

<h3>3. Customize settings </h3>
<p>Under main.py, you can customize the following:
  <ul>
    <li>Search domain</li>
    <p>Set your search domain to Sainsbury's Essentials items or Sainsbury's All items\Or get prompted to choose your search domain using searchDomain() function</p>
    <li>Update csv</li>
    <p>Set a limit on how old your csv files can be\Get prompted to update your csv files if they are too old</p>
    <li>Length of result to print</li>
    <p>Set your desired length of result to print</p>
</p>

<h3>4. Start searching!</h3>
