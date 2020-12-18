# Import required variables
from sainsvar import categoryIDs, parentCatIDs  # For both essential and all search
from sainsvar import esscategories, essfileNames, essmainurl, essurlParams  # For essential search
from sainsvar import allcategories, allfileNames, allmainurl, allurlParams    # For all search

# Import required libraries
from bs4 import BeautifulSoup
import requests
import csv

# Function to set category and filenames
def setcatandfile(searchall):
    if (searchall == True):
        categories = allcategories
        fileNames = allfileNames
    else:
        categories = esscategories
        fileNames = essfileNames
    return categories, fileNames

# Function to update essential csv for category of choice, update all by default
def updateEssentials(cat):

    # Update all categories
    if (cat == 0):
        for i in esscategories:
            updateEssentials(i)

    # Update specific category
    else:
        # Open csv file to write
        catName = esscategories[cat]
        fileName = essfileNames[catName]+'.csv'
        csv_file = open(fileName, 'w')
        csv_writer = csv.writer(csv_file)
        
        # Write column names into csv file
        csv_writer.writerow(['Description','Price/Unit','Unit','Price/Measure','Measure'])

        # Set page url params according to category
        # Set categoryID
        essurlParams['categoryId'] = categoryIDs[catName]

        # Set top_category and parent_category_rn
        essurlParams['top_category'] = parentCatIDs[catName]
        essurlParams['parent_category_rn'] = parentCatIDs[catName]


        # Loop to scrape pages till end is reached
        # Check if end is reached, end = True if reached
        end  = False
        # Set beginIndex in urlParam, adjust based on pagesize
        i = 0
        pagelength = int(essurlParams['pageSize'])
        essurlParams['beginIndex'] = str(i*pagelength)

        while (end == False):
            # Get page html using BeautifulSoup
            page = requests.get(essmainurl, params = essurlParams)
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
            if (len(soup.find_all('li', class_='gridItem')) == 0):
                end = True

            else:
                i += 1
                essurlParams['beginIndex'] = str(i*pagelength)

        # Close csv file
        csv_file.close()
    return True


# Function to update all csv for category of choice, update all by default
def updateAll(cat):
    # Update all categories
    if (cat == 0):
        for i in allcategories:
            updateAll(i)

    # Update specific category
    else:
        # Open csv file to write
        catName = allcategories[cat]
        fileName = allfileNames[catName]+'.csv'
        csv_file = open(fileName, 'w')
        csv_writer = csv.writer(csv_file)
        
        # Write column names into csv file
        csv_writer.writerow(['Description','Price/Unit','Unit','Price/Measure','Measure'])

        # Set page url params according to category
        # Set categoryId, top_category and categoryFacetId1
        allurlParams['categoryId'] = parentCatIDs[catName]
        allurlParams['top_category'] = parentCatIDs[catName]
        allurlParams['parent_category_rn'] = parentCatIDs[catName]


        # Loop to scrape pages till end is reached
        # Check if end is reached, end = True if reached
        end  = False
        # Set beginIndex in urlParam, adjust based on pagesize
        i = 0
        pagelength = int(allurlParams['pageSize'])
        allurlParams['beginIndex'] = str(i*pagelength)

        while (end == False):

            # Get page html using BeautifulSoup
            page = requests.get(allmainurl, params = allurlParams)
            soup = BeautifulSoup(page.text, 'lxml')
            
            # Find product information
            for griditem in soup.find_all('li', class_='gridItem'):
            
            # Obtain name of item, remove non ASCII characters
                name = griditem.h3.a.text.strip().encode('ascii', 'ignore').decode()

                try:
                    # Obtain price details of item
                    price = griditem.find('div', class_='pricing')
                    
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
            if (len(soup.find_all('li', class_='gridItem')) == 0):
                end = True

            else:
                i += 1
                allurlParams['beginIndex'] = str(i*pagelength)

        # Close csv file
        csv_file.close()
    return True

# Update user csv file has been updated
def updateSuccessful(searchall, cat):

    if (cat == 0):
        print("All csv files has been updated!")

    else:
        # Set correct categories and filenames
        categories, fileNames = setcatandfile(searchall)
        catName = categories[cat]
        fileName = fileNames[catName]+'.csv'
        print(fileName, 'has been updated successfully.')
