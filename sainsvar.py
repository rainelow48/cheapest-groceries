# This file contains variables relevant to Sainsburys
# Prefix of:
# "ess" : essentials items only
# "all" : all items

# Dictionary of categories
esscategories = {
    1 : 'Fruits and Vegetables',
    2 : 'Meat and Fish',
    3 : 'Dairy, Eggs and Chilled',
    4 : 'Bakery',
    5 : 'Frozen',
    6 : 'Food Cupboard',
    7 : 'Household'
}

allcategories = {
    1 : 'Fruits and Vegetables',
    2 : 'Meat and Fish',
    3 : 'Dairy, Eggs and Chilled',
    4 : 'Bakery',
    5 : 'Frozen',
    6 : 'Food Cupboard',
    7 : 'Household',
    8 : 'Drinks',
    9 : 'Beauty and Cosmetics',
    10 : 'Toiletries',
    11 : 'Home',
    12 : 'Baby and Toddler',
    13 : 'Pet',
    14 : 'Price Lock'
}

# Dictionary of filenames
essfileNames = {
    'Fruits and Vegetables': 'fruitandveg',
    'Meat and Fish': 'meatandfish',
    'Dairy, Eggs and Chilled': 'dairyeggsandchilled',
    'Bakery': 'bakery',
    'Frozen': 'frozen',
    'Food Cupboard': 'foodcupboard',
    'Household': 'household',
    'Drinks': 'drinks'
}

allfileNames = {
    'Fruits and Vegetables': 'allfruitandveg',
    'Meat and Fish': 'allmeatandfish',
    'Dairy, Eggs and Chilled': 'alldairyeggsandchilled',
    'Bakery': 'allbakery',
    'Frozen': 'allfrozen',
    'Food Cupboard': 'allfoodcupboard',
    'Household': 'allhousehold',
    'Drinks': 'alldrinks',
    'Beauty and Cosmetics' : 'allbeautyandcosmetics',
    'Toiletries' : 'alltoiletries',
    'Home' : 'allhome',
    'Baby and Toddler' : 'allbabyandtoddler',
    'Pet' : 'allpet',
    'Price Lock' : 'allpricelock'
}

# URL for essentials
essmainurl = 'https://www.sainsburys.co.uk/shop/CategoryDisplay'

# URL for all items
allmainurl = 'https://www.sainsburys.co.uk/shop/CategorySeeAllView'

# URL parameters
essurlParams = {
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

allurlParams = {
    'pageSize': '120',
    'orderBy': 'FAVOURITES_FIRST',
    'storeId': '10151',
    'categoryFacetId1': '',    # To input from parentCatIDs
    'promotionId': '',
    'listId': '',
    'catalogId': '10241',
    'searchTerm': '',
    'beginIndex': '',   # To adjust to get next page of items
    'top_category': '', # To input from parentCatIDs
    'langId': '44',
    'categoryId': '',   # To input from parentCatIDs
    'parent_category_rn': ''
}

# Category IDs (only used in updateEssentials)
categoryIDs = {
    'Fruits and Vegetables': '474593',
    'Meat and Fish': '474595',
    'Dairy, Eggs and Chilled': '474592',
    'Bakery': '474594',
    'Frozen': '474596',
    'Food Cupboard': '442361',
    'Household': '478352',
}

# Parent Category IDs (used in both updateEssentials, updateAll)
parentCatIDs = {
    'Fruits and Vegetables': '12518',
    'Meat and Fish': '13343',
    'Dairy, Eggs and Chilled': '428866',
    'Bakery': '12320',
    'Frozen': '218831',
    'Food Cupboard': '12422',
    'Household': '12564',
    'Drinks': '12192',
    'Beauty and Cosmetics' : '448352',
    'Toiletries' : '12448',
    'Home' : '281806',
    'Baby and Toddler' : '11651',
    'Pet' : '12298',
    'Price Lock' : '488855'
}