# Import required variables
from sainsvar import esscategories, essfileNames
from sainsvar import allcategories, allfileNames

# Import required functions
from checkvalidinput import invalidInt, validInput
from updatecsv import updateEssentials, updateAll, updateSuccessful

# Obtain users' preferred search domain, returns True if search all, False if search essentials
def searchDomain():
    searchall = True
    print("Please select your search domain:")
    print("0 :  All items")
    print("1 :  Essential items only")
    domain = input("\nYour selection (0-1): ")

    if (invalidInt(domain) == True):
        print("\nYou have not entered an integer.\nAll items will be searched.")

    elif (int(domain) == 0):
        print("\nYou have selected: All\nAll items will be searched.")

    elif (int(domain) == 1):
        print("\nYou have selected: Essentials\nOnly Essential items will be searched.")
        searchall = False

    else:
        print("\nYou have entered an invalid integer.\nAll items will be searched.")

    return searchall

# Obtain user's search category, returns 0 if invalid input, else returns user's selection
def searchCat(categories):
    print("\nPlease select a category to search item: ")
    print('0 : All')
    for i in categories:
        print(i, ":", categories[i])

    # Obtain category from user
    selection = input("\nYour selection (0-7): ")

    # Check for valid input (integer within range)
    return validInput(selection, categories)


# Check if user wants to update csv files, update only if user enters Y/y
def updatecsvfile(searchall, cat):
    update = input("Do you wish to update csv files? (Y/N): ")

    if (update.lower() == 'y'):
        if (cat == 0):
            print("All csv files are updating...")
        else:
            print("The csv file is updating...")

        # Update required csv files
        if (searchall == True):
            update = updateAll(cat)

        else:
            update = updateEssentials(cat)

        if (update == True) :
            # Update user that file update is successful
            updateSuccessful(searchall, cat)

        else:
            print("The csv file update was unsuccessful.")

    else:
        print("No csv files will be updated.")