# Import required variables
from sainsvar import categoryIDs, parentCatIDs  # For both essential and all search
from sainsvar import esscategories, essfileNames, essmainurl, essurlParams  # For essential search
from sainsvar import allcategories, allfileNames, allmainurl, allurlParams    # For all search

# Import required libraries
from bs4 import BeautifulSoup
import requests
import csv
import os
from datetime import date, timedelta

# Set variables (category, filenames, mainurl, urlParams)
def setVar(searchall):
    if (searchall == True):
        categories = allcategories
        fileNames = allfileNames
        mainurl = allmainurl
        urlParams = allurlParams
    else:
        categories = esscategories
        fileNames = essfileNames
        mainurl = essmainurl
        urlParams = essurlParams
    return categories, fileNames, mainurl, urlParams

# Return file's last modified date
def lastMod(categories, fileNames, cat):
    if (cat == 0):
        modDate = date.today()
        for i in categories:
            tempDate = lastMod(categories, fileNames, i)
            if (tempDate < modDate):
                modDate = tempDate
            else:
                pass

    else:
        catName = categories[cat]
        filename = os.getcwd() + '\\csv files\\' + fileNames[catName] + '.csv'
        try:
            modDate = date.fromtimestamp(os.path.getmtime(filename))
        except:
            modDate = date.today()
    return modDate

# Check if folder does not exists, else makes folder
def folderExist(directory, folder):
    if not os.path.exists(directory + folder):
        os.makedirs(directory + folder)
    else:
        pass

# Update user csv file has been updated
def updateSuccessful(searchall, cat):
    if (cat == 0):
        print("All csv files has been updated!")

    else:
        # Set correct categories and filenames
        categories, fileNames, mainurl, urlParams = setVar(searchall)
        catName = categories[cat]
        fileName = fileNames[catName]+'.csv'
        print(fileName, 'has been updated successfully.')

# Format text (get rids of empty space, non-ascii character and comma)
def formatText(text):
    newText = text.strip().encode('ascii', 'ignore').decode().replace(',', '')
    return newText

# Update essential csv for category of choice, update all by default
def updatecsvFiles(searchall, cat):

    # Set variables
    categories, fileNames, mainurl, urlParams = setVar(searchall)
    
    # Update all categories
    if (cat == 0):
        for i in categories:
            updatecsvFiles(searchall, i)

    # Update specific category
    else:
        # Open csv file to write
        catName = categories[cat]
        folderExist(os.getcwd(), '\\csv files\\')
        fileName = os.getcwd()+ '\\csv files\\' + fileNames[catName]+'.csv'
        csv_file = open(fileName, 'w')
        csv_writer = csv.writer(csv_file)
        
        # Write column names into csv file
        csv_writer.writerow(['Description','Price/Unit','Unit','Price/Measure','Measure'])

        # Set page url params according to category
        if searchall == True:
            # Set categoryId, top_category and categoryFacetId1 (all items)
            allurlParams['categoryId'] = parentCatIDs[catName]
            allurlParams['top_category'] = parentCatIDs[catName]
            allurlParams['parent_category_rn'] = parentCatIDs[catName]
        else:
            # Set categoryID, top_category and parent_category_rn (essential items)
            essurlParams['categoryId'] = categoryIDs[catName]
            essurlParams['top_category'] = parentCatIDs[catName]
            essurlParams['parent_category_rn'] = parentCatIDs[catName]

        # Loop to scrape pages till end is reached
        end  = False    # Check if end is reached, end = True if reached
        i = 0           # Set beginIndex in urlParam, adjust based on pagesize
        pagelength = int(urlParams['pageSize'])
        urlParams['beginIndex'] = str(i*pagelength)

        while (end == False):
            # Get page html using BeautifulSoup
            page = requests.get(mainurl, params = urlParams)
            soup = BeautifulSoup(page.text, 'lxml')
            
            # Find product information
            for griditem in soup.find_all('li', class_='gridItem'):

                try:
                    # Obtain name of item, remove non ASCII characters
                    name = formatText(griditem.h3.a.text)

                    # Obtain price details of item
                    price = griditem.find('div', class_='pricing')
                    
                    # Find price per unit, remove non ASCII characters
                    ppu = formatText(price.find('p', class_='pricePerUnit').text)
                    
                    # Split into price and unit
                    ppusplit = ppu.split('/')
                    
                    # Find price per measure, remove non ASCII characters
                    ppm = formatText(price.find('p', class_='pricePerMeasure').text)

                    # Split into price and measure
                    ppmsplit = ppm.split('/')
                    
                    # Write to csv file name, ppu, unit, ppm, measure
                    csv_writer.writerow([name, ppusplit[0], ppusplit[1], ppmsplit[0], ppmsplit[1]])
                
                except:
                    pass
            
            # Check if end of items have been reached
            if (len(soup.find_all('li', class_='gridItem')) == 0):
                end = True

            else:   # Continue scraping next page
                i += 1
                urlParams['beginIndex'] = str(i*pagelength)

        # Close csv file
        csv_file.close()
    return True
