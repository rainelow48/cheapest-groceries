# Import required variables
from sainsessvar import categories

def validInput(selection):
    broken = False
    try:
        cat = int(selection)
    except ValueError:
        broken = True

    if (broken == True):
        print("You have input a non-integer.\nAll csv files will be updated.\n")
        cat = 0

    elif (cat > len(categories) or cat < 0):
        print("You have input an out of range integer.\nAll csv files will be updated.\n")
        cat = 0

    else:
        if (cat == 0):
            print("You have selected: All\nThe file(s) will be updated.")
        else:
            print("You have selected:", categories[cat], "\nThe file will be updated.\n")

    return cat