# Import required file function
from userinteraction import searchDomain, searchCat, updatecsvfile
from updatecsv import setcatandfile
from searchcsv import searchitem

# Import library
import time

# Welcome message
print("\n*** Welcome to Sainsbury's search function! ***\n")

# Obtain user's preferred search domain
# searchall = searchDomain()
# Set search domain to all items
searchall = True

# Set correct categories and filenames
categories, fileNames = setcatandfile(searchall)

# Obtain user's preferred search category
cat = searchCat(categories)

# Time duration to update file, Takes 659 seconds to update all files
# start_time = time.time()
# # Update csv file if required
# updatecsvfile(searchall, cat)
# print("---- %s seconds ----" % (time.time()-start_time))


# Obtain search content from user
query = input("\nPlease enter item to search for: ")
searchValues = query.lower().split()

# Search for item
result = searchitem(cat, categories, fileNames, searchValues)

# Prints result to user
if (len(result) == 0):
    print("No items were found")

else:
    if (cat == 0):
        print("Found ", len(result), "items in All")
    else:
        print("Found ", len(result), "items in", categories[cat])
    print(result)