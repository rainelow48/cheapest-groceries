# Import required variables
from sainsvar import esscategories, essfileNames
from sainsvar import allcategories, allfileNames

# Import required file function
from userinteraction import searchDomain, searchCat, updatecsvfile
from updatecsv import updateEssentials, updateSuccessful, setcatandfile
from searchcsv import searchitem


# Welcome message
print("\n*** Welcome to Sainsbury's! ***\n")

# Obtain user's preferred search domain
searchall = searchDomain()

# Set correct categories and filenames
categories, fileNames = setcatandfile(searchall)

# Obtain user'r preferred search category
cat = searchCat(categories)

# Update csv file if required
updatecsvfile(searchall, cat)

# Obtain search content from user
query = input("\nPlease enter item to search for: ")
searchValues = query.lower().split()

# Search for item
searchitem(cat, categories, fileNames, searchValues)
