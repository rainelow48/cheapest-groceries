from bs4 import BeautifulSoup
import requests
import csv


# URL to be scraped (essentials)

mainurl = 'https://www.sainsburys.co.uk/shop/CategoryDisplay'

urlparams = {
    'listId': '',
    'catalogID': '10241',
    'searchTerm': '',
    'beginIndex': '240',
    'pageSize': '120',
    'orderBy': 'TOP_SELLERS|SEQUENCING',
    'top_category': '13343',
    'langId': '44',
    'storeId': '10151',
    'categoryId': '474595',
    'promotionId': '',
    'parent_category_rn': '13343'
}

urlparams['beginIndex'] = str(120)

# Essentials
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

# print(urlparams)

page = requests.get(mainurl, params = urlparams)
soup = BeautifulSoup(page.text, "lxml")

csv_file = open('meatandfish.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Description','Price per Unit','Unit','Price per Measure','Measure'])

print(len(soup.find_all('li', class_='gridItem')))
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

csv_file.close()