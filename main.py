# Import required variables
from sainsessvar import categories

# Import required file function
from updatecsv_essentials import updateEssentials
from checkvalidinput import validInput



print("Welcome to Sainsbury's cheapest groceries!\n")
print("You can choose from the following categories:")
print('0 : All')
for i in categories:
    print(i, ":", categories[i])

selection = input("\nPlease select a category (0-7) to update csv: ")

# Check for valid input (integer within range)
cat = validInput(selection)

# Update required csv files
updateEssentials(cat)
