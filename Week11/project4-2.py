#Project 4, program 2, 10/29/2026, Ciara Patch
def pantry(item1, item2, item3): 
    haveThings = False
    thingsHad = 0
    snackBin=["chips", "pretzels"]
    candyBin=["skittles", "chocolate", "licorice"]
    sodaBin=["fanta", "water", "rootbeer"]
    if item1 in snackBin: #Checking to see if we have what the user wants
        print(f"Perfect! we have {item1}!")
        thingsHad +=1
        if item2 in candyBin:
            print(f"We have {item2} too!")
            thingsHad +=1
            if item3 in sodaBin:
                thingsHad +=1
                print("Yay! We have everything you want!")
                haveThings=True
    if haveThings == False: #If we don't have what the user wants, it lists what we do have
        print("Sorry, it looks like we don't have everything you want, but we do have: ")
        for i in snackBin:
            print(i)
        for i in candyBin:
            print(i)
        for i in sodaBin:
            print(i)
    return thingsHad #Returns the number of things we have that the user wanted

def ask(): #Getting user input
    snack=input("What kind of snack do you want? ").lower()
    candy=input("What kind of candy do you want? ").lower()
    soda=input("What kind of drink do you want? ").lower()
    totalItems = pantry (snack, candy, soda)
    if totalItems < 3: #Fake loop
        print(f"Sorry it looks like we only had {totalItems} things")
        print("I don't feel like buying anything so you'll have to pick from something we already have")
        ask()
    

print("Let's have a movie night!")
ask()
