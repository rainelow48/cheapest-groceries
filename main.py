# Import required variables
from sainsessvar import categories

# Import required file function
from checkvalidinput import validInput
from updatecsv_essentials import updateEssentials, updateSuccessful
from searchcsv_essentials import searchEssentials


# Instructions
print("\n*** Welcome to Sainsbury's! ***\n")
print("Please select a category to search item: ")
print('0 : All')
for i in categories:
    print(i, ":", categories[i])

# Obtain category from user
selection = input("\nYour selection (0-7): ")

# Check for valid input (integer within range)
cat = validInput(selection)

# Check if user wants to update csv files, update only if user enters Y/y
update = input("Do you wish to update csv files? (Y/N): ")

if (update.lower() == 'y'):
    if (cat == 0):
        print("All csv files are updating...")
    else:
        print("The csv file is updating...")

    # Update required csv files
    update = updateEssentials(cat)
    if (update == True) :

        # Update user that file update is successful
        updateSuccessful(cat)
    else:
        print("The csv file update was unsuccessful.")

else:
    print("No csv files will be updated.")

# Obtain search content from user
query = input("Please enter item to search for: ")
searchValues = query.lower().split()

# Search for item
searchEssentials(cat, searchValues)
