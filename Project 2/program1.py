#Project 2, program 1. Ciara Patch

print("Lets play hide and seek! Help me find Bob, Jill and Jannett") #Explaining the game
print("Here are the spot numbers: 1 = under the bed, 2 = behind the cough, 3 = the attic, 4 = the laundry room, 5 = the backyard")
spot=float(input("Where should we look first? ")) #User input
hiding = 0
valid = True
if spot < 1 or spot > 5: #Checking for valid input
    print("Invalid!")
    valid = False
elif spot == 1: #Checks for each spot
    print("We found bob!")
    hideAsk = input("When you hide, would you want to hide here? (Y or N) ") #I got bored and wanted some extra nesting so this is to find another spot
    if hideAsk.upper() == "Y": #Sets the hiding spot for the next full set of if statements
        hiding = "spot1" #If user says they want to hide here, then it sets the spot
elif spot == 2:
    print("We didn't find anyone...")
    hideAsk = input("When you hide, would you want to hide here? (Y or N) ")
    if hideAsk.upper() == "Y":
        hiding = "spot2"
elif spot == 3:
    print("We found Jannett!")
    hideAsk = input("When you hide, would you want to hide here? (Y or N) ")
    if hideAsk.upper() == "Y":
        hiding = "spot3"
elif spot == 4:
    print("We found Jill!")
    hideAsk = input("When you hide, would you want to hide here? (Y or N) ")
    if hideAsk.upper() == "Y":
        hiding = "spot4"
else: #Last place to hide which is 5
    print("We didn't find anyone...")
    hideAsk = input("When you hide, would you want to hide here? (Y or N) ")
    if hideAsk.upper() == "Y":
        hiding = "spot5"

if valid == True: #You only get to hide if you played the game correctly the first round with a valid answer
    print("Now it's our turn to hide!")
    if hiding == "spot1": #If statements for the spots that you chose while seeking
        print("Bob found you!") #If you chose to hide in a spot someone else was hiding in, they find you
    elif hiding == "spot2":
        print("Nobody found you! You won!")
    elif hiding == "spot3":
        print("Jannett found you!")
    elif hiding == "spot4":
        print("Jill found you!")
    elif hiding == "spot5": 
        print("Nobody found you! You won!")
    else:
        print("You seriously didn'y pick a valid spot while you were seeking?... It's too late Bob already saw you")

if valid == False:#You only get to hide if you played the game correctly the first round with a valid answer
    print("You're no fun to play with")