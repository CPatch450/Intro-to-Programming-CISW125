#Project 5, program 1 (Lists), Ciara Patch
import random

def fishDisplay(area):
    if area == 1:
        print(f"The types of fish living here are: \n{saltFish}") #Listing all the fish
    elif area == 2:
        print(f"The types of fish living here are: \n{freshFish}")
    elif area == 3:
        print(f"The types of fish living here are: \n{sharks}")
    else:
        print(f"The types of fish living here are: \n{jellyfish}")
    print(f"Oh no! A shark got out and began eating the other fish!")
    print(f"It looks like the aquarium only has a few kinds left and is getting rid of most sharks!")
    i = 0
    while i < 14: #Removes 14 fish from the list of all fish
        sharkBait = random.randint(0, len(allFish) - 1) #Generates a random index number to determine the fish thats eaten but
        allFish.remove(allFish[sharkBait]) #makes sure the number is less than the number of fish left
        i += 1
    allFish.sort()#Alaphebetical sort
    print(f"All that's left is: \n {allFish}")
    
def areaChoice():
    valid = False
    areas=["1. Salt water fish", "2. Fresh water fish", "3. Sharks", "4. Jellyfish"]
    print(f"There are many kinds of fish to see. Here are the main attractions: \n{areas}" )
    while valid == False: #Makes sure user input is valid
        choice=float(input("What area would you like to see first? "))
        if choice < 1 or choice > 4:
            print("Invalid!")
        else:
            fishDisplay(choice)
            break

saltFish=["yellow fin tuna", "striper fish", "dolphin fish mahi", "sailfish"] #List of all the different kinds of fish
freshFish=["coho salmon", "large mouth bass", "white perch", "atlantic salmon", "shad"]
sharks=["cookie cutter shark", "thresher shark", "hammer head shark", "tiger shark", "whale shark"]
jellyfish=["moon jelly", "fried egg jellyfish", "lions mane jellyfish", "pink meani jelly", "pacific sea nettle"]
allFish=saltFish+freshFish+jellyfish+sharks

print("Welcome to the Tokyo aquarium!")
areaChoice()


