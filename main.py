from updatecsv_essentials import updateEssentials

# Dictionary of categories
categories = {
    0 : 'All',
    1 : 'Fruits and Vegetables',
    2 : 'Meat and Fish',
    3 : 'Dairy, eggs and Chilled',
    4 : 'Bakery',
    5 : 'Frozen',
    6 : 'Food Cupboard',
    7 : 'Household'
    # 8 : 'Drinks'
}
print("Welcome to Sainsbury's cheapest groceries!\n")
print("You can choose from the following categories:")
for i in categories:
    print(i, ":", categories[i])

selection = input("\nPlease select a category (0-7) to update csv: ")
broken = False
try:
    cat = int(selection)
except ValueError:
    broken = True

if (broken == True):
    print("You have input a non-integer. All csv files will be updated.")
    cat = 0
elif (int(selection) >= len(categories) or int(selection) < 0):
    print("You have input an out of range integer. All csv files will be updated.")
    cat = 0
else:
    print("You have selected:", categories[cat], "\nThe file(s) will be updated.")
    cat = int(selection)

# updateEssentials(cat)
