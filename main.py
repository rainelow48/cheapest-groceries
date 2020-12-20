# Import required file function
from userinteraction import searchDomain, searchCat, updatefile, oldcsv
from updatecsv import setVar
from searchcsv import searchItem, sortItems

# Import library
import time

# Welcome message
print("\n*** Welcome to Sainsbury's search function! ***\n")

# Obtain user's preferred search domain
# searchall = searchDomain()
searchall = True # Sets search domain to all items

# Set correct categories and filenames
categories, fileNames, mainurl, urlParams = setVar(searchall)

# Obtain user's preferred search category
cat = searchCat(categories)

# Checks if csv file is older than ## days, update if required
if (oldcsv(categories, fileNames, cat, 1) == True): # 0 days: last updated today 
    
    # Time duration to update file, Takes 659 seconds to update all files
    start_time = time.time()
    updatefile(searchall, cat)
    print("---- %.2f seconds ----" % (time.time()-start_time))
else:
    pass

# Obtain search content from user
query = input("\nPlease enter item to search for: ")
searchValues = query.lower().split()

# Search for item
searchResult = searchItem(cat, categories, fileNames, searchValues)

# Sort result
result = sortItems(searchResult)

# Prints result to user
if (len(result) == 0):
    print("No items were found")

else:
    if (cat == 0):
        print("Found ", len(result), "items in All")
    else:
        print("Found ", len(result), "items in", categories[cat])
    
    # If result is <100 items, print all to user, else, print shortened table
    if (len(result) > 100):
        print(result)
    else:
        print(result.to_string())