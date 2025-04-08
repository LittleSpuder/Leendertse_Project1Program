#Get's the users input and checks whether it is the type defined.
#Main method for user input validation
#Returntype is defualted string so if you don't input a returnType, it'll automatically be chosen to be a str
def getUserInput(instructions, returnType = str, Yes_No = False):
    valid = False
    while not valid:
        result = input(instructions).strip()
        if Yes_No == True:
            if result.lower() == 'y' or result.lower() == 'n':
                try:
                    result = str(result)
                except:
                    #returns return type as __name__ rather than <class '_returntype'>
                    print(f"Invalid Input! Please enter a string.\n")
                else:
                    valid = True
            else:
                print("Please input a valid Y or N.")
        else:
                try:
                    result = returnType(result)
                except:
                    #returns return type as __name__ rather than <class '_returntype'>
                    print(f"Invalid Input! Please enter a {returnType.__name__}.\n")
                else:
                    valid = True
    return(result)

def user_customization():
    valid = False
    while not valid:
        instructions = getUserInput("Would you like the instructions? (Y/N) ", str, True).strip()
        if instructions.lower() == 'y':
            print("When using this system, please pay note that the following numbers signify the following settings. \n• 1 - Language\n• 2 - Username\n• 3 - Custom Colours\n• 4 - Custom Music and Sound Effects.\nIf you'd like to exit, press 0!")
        customization = getUserInput("What would you like to change? ", int)
        cus_valid = False
        while not cus_valid:
            if customization == 0:
                cus_valid = True
                valid = True
                wrong = False
            elif customization == 1:
                cus_valid = True
                wrong = False
            elif customization == 2:
                cus_valid = True
                wrong = False
            elif customization == 3:
                cus_valid = True
                wrong = False
            elif customization == 4:
                cus_valid = True
                wrong = False
            else:
                print("That is an invalid number! Please try again. \n")
                cus_valid = True
                wrong = True
        if valid == False and wrong == False:
            exit = getUserInput("Would you like to go back to the main home screen? ", str, True)
            if exit.lower() == 'y':
                valid = True

user_customization()
print("Out of User Customisation <3")