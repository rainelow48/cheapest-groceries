from bs4 import BeautifulSoup
import requests
import csv 


# Function to update csv for category of choice, update all by default
def updateEssentials(cat = 0):

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

    # URL to be scrapped
    mainurl = 'https://www.sainsburys.co.uk/shop/CategoryDisplay'

    # URL parameters
    urlParams = {
        'listId': '',
        'catalogID': '10241',
        'searchTerm': '',
        'beginIndex': '',  # To adjust to get next page of items
        'pageSize': '120',
        'orderBy': 'TOP_SELLERS|SEQUENCING',
        'top_category': '', # To input from parentCatIDs
        'langId': '44',
        'storeId': '10151',
        'categoryId': '',   # To input from categoryIDs
        'promotionId': '',
        'parent_category_rn': '' # To input from parentCatIDs
    }

    # Category IDs
    categoryIDs = {
        'Fruits and Vegetables': '474593',
        'Meat and Fish': '474595',
        'Dairy, eggs and Chilled': '474592',
        'Bakery': '474594',
        'Frozen': '474596',
        'Food Cupboard': '442361',
        'Household': '478352',
        'Drinks': '' #drinks has no essentials
    }

    # Parent Category IDs
    parentCatIDs = {
        'Fruits and Vegetables': '12518',
        'Meat and Fish': '13343',
        'Dairy, eggs and Chilled': '428866',
        'Bakery': '12320',
        'Frozen': '218831',
        'Food Cupboard': '12422',
        'Household': '12564',
        'Drinks': '12192'
    }

    # Update all categories
    if (cat == 0):
        for i in categories:
            updateEssentials(i)

        print("\nAll csv files has been updated!")

    # Update specific category
    else:
        # Open csv file to write
        catName = categories[cat]
        fileName = fileNames[catName]+'.csv'
        csv_file = open(fileName, 'w')
        csv_writer = csv.writer(csv_file)
        
        # Write column names into csv file
        csv_writer.writerow(['Description','Price per Unit','Unit','Price per Measure','Measure'])

        # Set page url params according to category
        # Set categoryID
        urlParams['categoryId'] = categoryIDs[catName]

        # Set top_category and parent_category_rn
        urlParams['top_category'] = parentCatIDs[catName]
        urlParams['parent_category_rn'] = parentCatIDs[catName]


        # Loop to scrape pages till end is reached
        # Check if end is reached, end = True if reached
        end  = False
        # Set beginIndex in urlParam, adjust based on pagesize
        i = 0
        pagelength = int(urlParams['pageSize'])
        urlParams['beginIndex'] = str(i*pagelength)

        while (end == False):
            # Get page html using BeautifulSoup
            page = requests.get(mainurl, params = urlParams)
            soup = BeautifulSoup(page.text, 'lxml')
            
            # Find product information
            for griditem in soup.find_all('li', class_='gridItem'):
            
            # Obtain name of item, remove non ASCII characters
                name = griditem.h3.a.text.strip().encode('ascii', 'ignore').decode()

                try:
                    # Obtain price details of item
                    price = griditem.find('div', class_='product')
                    
                    # Find price per unit, remove non ASCII characters
                    ppu = price.find('p', class_='pricePerUnit').text.strip().encode('ascii', 'ignore').decode()
                    
                    # Split into price and unit
                    ppusplit = ppu.split('/')
                    
                    # Find price per measure, remove non ASCII characters
                    ppm = price.find('p', class_='pricePerMeasure').text.strip().encode('ascii', 'ignore').decode()
                    
                    # Split into price and measure
                    ppmsplit = ppm.split('/')
                    
                    # Write to csv file name, ppu, unit, ppm, measure
                    csv_writer.writerow([name, ppusplit[0], ppusplit[1], ppmsplit[0], ppmsplit[1]])
                
                except:
                    pass
            
            # Check if end of items have been reached
            if (len(soup.find_all('li', class_='gridItem')) == pagelength):
                i += 1
                urlParams['beginIndex'] = str(i*pagelength)

            else:
                end = True

        # Close csv file
        csv_file.close()

        # Update user csv file has been updated
        print(fileName, 'has been updated successfully.')

updateEssentials(0)