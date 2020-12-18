# This file contains variables relevant to Sainsburys
# ess: essentials items only
# all: all items

# Dictionary of categories
esscategories = {
    1 : 'Fruits and Vegetables',
    2 : 'Meat and Fish',
    3 : 'Dairy, eggs and Chilled',
    4 : 'Bakery',
    5 : 'Frozen',
    6 : 'Food Cupboard',
    7 : 'Household'
}

allcategories = {
    1 : 'Fruits and Vegetables',
    2 : 'Meat and Fish',
    3 : 'Dairy, eggs and Chilled',
    4 : 'Bakery',
    5 : 'Frozen',
    6 : 'Food Cupboard',
    7 : 'Household',
    8 : 'Drinks'
}

# Dictionary of filenames
essfileNames = {
    'Fruits and Vegetables': 'fruitandveg',
    'Meat and Fish': 'meatandfish',
    'Dairy, eggs and Chilled': 'dairyeggsandchilled',
    'Bakery': 'bakery',
    'Frozen': 'frozen',
    'Food Cupboard': 'foodcupboard',
    'Household': 'household',
    'Drinks': 'drinks'
}

allfileNames = {
    'Fruits and Vegetables': 'allfruitandveg',
    'Meat and Fish': 'allmeatandfish',
    'Dairy, eggs and Chilled': 'alldairyeggsandchilled',
    'Bakery': 'allbakery',
    'Frozen': 'allfrozen',
    'Food Cupboard': 'allfoodcupboard',
    'Household': 'allhousehold',
    'Drinks': 'alldrinks'
}

# URL to be scrapped
essmainurl = 'https://www.sainsburys.co.uk/shop/CategoryDisplay'

# URL for all items = allmainurl1 + allurlcat[category] + allmainurl2
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
    'top_category': '',
    'langId': '44',
    'categoryId': '',   # To input from parentCatIDs
    'parent_category_rn': ''

    # 'fromMegaNav': '1',
    # 'langID': '44',
    # 'storeId': '10151',
    # 'catalogId': '10241',
    # 'categoryId': '',  
    # 'parent_category_rn': '',
    # 'top_category': '',      # To input from parentCatIDs
    # 'pageSize': '120',
    # 'orderBy': 'FAVOURITES_FIRST',
    # 'searchTerm': '',
    # 'catSeeAll': 'true',
    # 'beginIndex': '',  # To adjust to get next page of items
    # 'categoryFacetId1': '',      # To input from parentCatIDs
    # 'categoryFacetId2': ''
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