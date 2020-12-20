# Import required variables
from sainsvar import esscategories, essfileNames
from sainsvar import allcategories, allfileNames

# Import required functions
from updatecsv import updatecsvFiles, updateSuccessful, lastMod

# Import required libraries
from datetime import date, timedelta
import time

# Checks if userInput is invalid(not an integer), returns True if invalid
def invalidInt(userInput):
    broken = False
    try:
        int(userInput)
    except ValueError:
        broken = True
    
    return broken

# Returns category number (0 if invalid input)
def validInput(userInput, categories):

    if (invalidInt(userInput) == True):
        print("\nYou have input a non-integer.\nAll categories will be selected.\n")
        cat = 0

    else:
        cat = int(userInput)
        if (cat > len(categories) or cat < 0):
            print("\nYou have input an out of range integer.\nAll categories will be selected.\n")
            cat = 0

        elif (cat == 0):
            print("\nYou have selected: All")

        else:
            print("\nYou have selected:", categories[int(userInput)])

    return cat

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
    prompt = '\nYour selection (0-' + str(len(categories)) + '): '
    selection = input(prompt)

    # Check for valid input (integer within range)
    return validInput(selection, categories)

# Check if user wants to update csv files, update only if user enters Y/y
def updatefile(searchall, cat):
    update = input("Do you wish to update csv files? (Y/N): ")
    
    if (update.lower() == 'y'):
        # Update required csv files
        if (searchall == True and cat == 0):    # Checks if all searchall csv files need to be updated
            # Get user confirmation again
            confirm = input("This might take a long while (10-15min). Do you wish to proceed? (Y/N): ")

            if (confirm.lower() == 'y'):
                print("All csv files are updating...")
                start_time = time.time()    # Time duration to update file, Takes 600-900 seconds to update all files
                update = updatecsvFiles(searchall, cat)

            else:
                pass

        else:   # Update either all/one essential csv files or one searchall csv file
            print("Updating file(s)...")
            start_time = time.time()
            update = updatecsvFiles(searchall, cat)

        # Update user status of csv file update
        if (update == True) :
            updateSuccessful(searchall, cat)
        else:
            print("The csv file update was unsuccessful.")

        print("---- %.2f seconds ----" % (time.time()-start_time))
    else:
        print("No csv files will be updated.")

# Check if csv files are older than n days (default 2 days), prompt user to update if true
def oldcsv(categories, fileNames, cat, days = 2):
    today = date.today()
    lastModDate = lastMod(categories, fileNames, cat)
    dateDiff = today - lastModDate
    return (dateDiff >= timedelta(days))

# Print result to user
def printResult(result, cat, categories, length = 150):
    if (len(result) == 0):
        print("No items were found")

    else:
        if (cat == 0):
            print("Found ", len(result), "items in All")
        else:
            print("Found ", len(result), "items in", categories[cat])
        
        # If result is length items, print all to user, else print shortened table
        if (len(result) > length):
            print(result)
        else:
            print(result.to_string())