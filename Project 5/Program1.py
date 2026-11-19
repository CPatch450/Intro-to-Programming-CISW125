#Project 5, program 1 (Lists), Ciara Patch
#aquarium program that shows a list of different kinds of fish? like the jeelyfish?
def fishDisplay(area):
    saltFish=["yellow fin tuna", "striper fish", "dolphin fish mahi", "sailfish"]
    freshFish=["coho salmon", "large mouth bass", "white perch", "atlantic salmon", "shad"]
    sharks=["cookie cutter shark", "thresher shark", "hammer head shark", "tiger shark", "whale shark"]
    jellyfish=["moon jelly", "fried egg jellyfish", "lions mane jellyfish", "pink meani jelly", "pacific sea nettle"]
    if area == 1:
        print(f"The types of fish living here are: \n{saltFish}")
    elif area == 2:
        print(f"The types of fish living here are: \n{freshFish}")
    elif area == 3:
        print(f"The types of fish living here are: \n{sharks}")
    else:
        print(f"The types of fish living here are: \n{jellyfish}")
    print(f"Oh no! A shark got out and began eating the other fish!")
    print(f"It looks like the aquarium only has a few kinds left and is getting rid of most sharks!")
    allFish=[saltFish+freshFish+jellyfish]
    allFish.remove("coho salmon")
    allFish.remove("yellow fin tuna")
    allFish.append(sharks[4])
    print(allFish)
    print(f"All that's left is: \n {allFish.sort()}")

    
def areaChoice():
    valid = False
    areas=["1. Salt water fish", "2. Fresh water fish", "3. Sharks", "4. Jellyfish"]
    print(f"There are many kinds of fish to see. Here are the main attractions: \n{areas}" )
    while valid == False:
        choice=float(input("What area would you like to see first? "))
        if choice < 1 or choice > 4:
            print("Invalid!")
        else:
            fishDisplay(choice)

print("Welcome to the Tokyo aquarium!")
areaChoice()


