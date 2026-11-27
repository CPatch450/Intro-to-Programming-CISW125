#Final Project, Freedom of Choice. Intro to Programming, Ciara Patch
    #Bologna, italy, kimi antonelli born here - not capital
    #Barcelona, spain, capital
    #Brussels, belgium, capital
    #Vienna, austria, capital and federal state
    #Oslo, norway, capital
#Here is where I got the info for the import time and sleep functions: https://realpython.com/python-sleep/

import random
import time #For the sleep (pauses) to space out dialogue
#nested dictionary on fleshed out facts: official languages, tourist attractions, culture, food

locations={ #quick base facts that need nested
    "Bologna, Italy": {
        "quick facts":"Although Bologna is not the capital, it's become a huge tourist attraction thanks to its hidden canals and the University of Bologna- which is"
        "the oldest university in operation to this day and was built in 1088. Students, travelers and food connessuiers come from all over the world "
        "to come partake in the rich experiences and unique local atmosphere here.",
        "culture":"It's no secret that Italians love their pasta- and it's actually believed that the creation of tagliatelle, lasagna and tortellini are tied to the city here."
        "The cultue in and around the city here has been greatly influenced by the University and focusses on fun, community, experiences and education."
        "Toursists often come to Bologna looking for a quick get away with good food but often leave with fond memories and describe feeling a real connection"
        "and community that gets lost easily in the rush of fast paced life",
        "landmarks/celebrities":"The undeniably beautiful red terracotta roofs of the buildings here stand proud and host homes to many great attractions and people."
        "Such as the youngest ever Formula 1 World Champion, Kimi Antionelli, who was born and raised among the beautiful cobbled streets here or even the UNESCO Porticoes\n"
        "and medieval Asinelli and Garisenda towers. There are never things to run out of to see in Italy, and especially so in Bologna."
    },
    "Barcelona, Spain": {

    },
    "Brussels, Belgium": {

    },
    "Vienna, Austria": {

    },
    "Oslo, Norway": {

    }
           }

def travelChoice():#Fake loop for running through dictionary
    print("The travel agent recommended some places that fit your timeline for your time off and sent you a digital pamphlet")
    print(f"It looks like your options are:\n    {places}")
    valid = False
    factValid = False
    while valid == False:
        pamAsk=input("Which locations pamphlet would you like to read? (1) Bologna, (2) Barcelona, (3) Brussels, (4) Vienna, (5) Oslo, (6) all: ")
        if pamAsk == "1": #Bologna
            while factValid == False:
                factAsk=input("Would you like to see the sections on (1) quick facts, (2) culture, (3) landmarks/celebrities or (4) all of the above? ")
                if factAsk=="1":
                    print(locations["Bologna, Italy"]["quick facts"])
                    factValid = True
                elif factAsk =="2":
                    print(locations["Bologna, Italy"]["culture"])
                    factValid = True
                elif factAsk =="3":
                    print(locations["Bologna, Italy"]["landmarks/celebrities"])
                    factValid = True
                elif factAsk =="4":
                    print(locations["Bologna, Italy"])
                    factValid = True
                else:
                    print("Invalid input!")
        elif pamAsk =="2": #Barcelona
            factAsk=input("Would you like to see the sections on (1) quick facts, (2) culture, (3) landmarks/celebrities or (4) all of the above? ")
        elif pamAsk =="3": #Brussels
            factAsk=input("Would you like to see the sections on (1) quick facts, (2) culture, (3) landmarks/celebrities or (4) all of the above? ")
        elif pamAsk =="4": #Vienna
            factAsk=input("Would you like to see the sections on (1) quick facts, (2) culture, (3) landmarks/celebrities or (4) all of the above? ")
        elif pamAsk =="5": #Oslo
            factAsk=input("Would you like to see the sections on (1) quick facts, (2) culture, (3) landmarks/celebrities or (4) all of the above? ")
        elif pamAsk =="6": #All locations
            factAsk=input("Would you like to see the sections on (1) quick facts, (2) culture, (3) landmarks/celebrities or (4) all of the above? ")        
        else:
            print("Invalid input!")


bonus=random.randint(50,150) #Randomly generating numbers for story telling purposes
lottery=random.randint(1800,2500)
totalUSD=bonus+lottery
places=["Bologna, Italy", "Barcelona, Spain", "Brussels, Belgium", "Vienna, Austria", "Oslo, Norway"]

print("It's been a long week at work... All of these weird IT outages and Microsoft problems have been taking a toll on you")
print("At least you finally have a week off to help you unwind and relax- and your boss has given you a small bonus to make up for all the stress!")
print("...")
time.sleep(2.) #Pause for 2 seconds
print(f"Nice!\nIt looks like she gave you ${bonus}!")
print("And after your coworker suddenly quit without notice (which definetely helped with the stress) he slipped you a lottery ticket")
validScratch = False #Loop to ensure valid user input
while validScratch == False:
    scratch=input("Would you like to scratch the ticket (1) or keep it as a momento? (2) ")
    if scratch == "2": #Ends program early
        print("You decide to pin the lottery ticket on your bulletin board of memories and think back on the good times you shared")
        print("You then spend your nice bonus on some books, puzzles and video games to help unwind for the rest of your time off")
        break
    elif scratch == "1": #Continues program
        #pause...
        print("Oh. Oh my...")
        time.sleep(1.25)
        print(f"You Won! You won ${lottery}! And there's some travel agents info attached")
        print("It's definetely time for a vacation!")
        travelChoice()
        validScratch = True
    else: #Easier to check for inputted invalid string input by keeping the input as a string and labelling 1 and 2 as strings
        print("Invalid input!")



#text walking simulator, 1 or 2 user input kind of situation based on selected location like in civil war example
#remember equations for purchased items to subtract from total and conversions for local currency
#3 max purchases - subtract random amount from USD total for flights