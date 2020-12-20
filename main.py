# Import required file function
from userinteraction import searchDomain, searchCat, updatefile, oldcsv, printResult
from updatecsv import setVar
from searchcsv import searchItem, sortItems

def main():
    print("\n*** Welcome to Sainsbury's search function! ***\n")    # Welcome message

    searchall = False                                                # Sets search domain to all items (True), essential items (False)
    # searchall = searchDomain()                                    # Use to obtain user's preferred search domain
    categories, fileNames, mainurl, urlParams = setVar(searchall)   # Set correct variables
    cat = searchCat(categories)                                     # Obtain user's preferred search category

    # Checks if csv file is older than ## days, prompt update if required
    days = 0                                                        # To be set by user, "days = 0" to trigger update prompt
    if (oldcsv(categories, fileNames, cat, days) == True): 
        updatefile(searchall, cat)
    else:
        pass

    searchValues = input("\nPlease enter item to search for: ").lower().split()     # Obtain search content from user
    searchResult = searchItem(cat, categories, fileNames, searchValues)             # Search for item
    result = sortItems(searchResult)                                                # Sort result
    length = 150                                                                    # Set cut off length for results table
    printResult(result, cat, categories, length)                                    # Prints result to user

if __name__ == "__main__":
    main()