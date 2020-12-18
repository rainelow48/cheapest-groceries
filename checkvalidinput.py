# Function checks if userInput is invalid(not an integer), returns True if invalid
def invalidInt(userInput):
    broken = False
    try:
        int(userInput)
    except ValueError:
        broken = True
    
    return broken

# Function returns category number (0 if invalid input)
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