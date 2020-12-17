# Import required variables
from sainsessvar import categories

def validInput(selection):
    broken = False
    try:
        cat = int(selection)
    except ValueError:
        broken = True

    if (broken == True):
        print("\nYou have input a non-integer.\nAll categories will be selected.\n")
        cat = 0

    elif (cat > len(categories) or cat < 0):
        print("\nYou have input an out of range integer.\nAll categories will be selected.\n")
        cat = 0

    else:
        if (cat == 0):
            print("\nYou have selected: All")
        else:
            print("\nYou have selected:", categories[cat])

    return cat