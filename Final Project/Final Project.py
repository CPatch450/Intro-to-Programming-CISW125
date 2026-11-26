#Final Project, Freedom of Choice. Intro to Programming, Ciara Patch
    #Bologna, italy, kimi antonelli born here - not capital
    #Barcelona, spain, capital
    #Brussels, belgium, capital
    #Vienna, austria, capital and federal state
    #Oslo, norway, capital

#def for running through dictionary/fake loop/ask user if they want to see more facts
import random
#import pause to space out all the dialogue at the beginning for better story telling

bonus=random.randint(50,150) #Randomly generating numbers for story telling purposes
lottery=random.randint(1800,2500)
totalUSD=bonus+lottery
print("It's been a long week at work... All of these weird IT outages and Microsoft problems have been taking a toll on you")
print("At least you finally have a week off to help you unwind and relax- and your boss has given you a small bonus to make up for all the stress!")
#pause
print(f"It looks like she gave you ${bonus}!\n Nice!")
print("And after your coworker suddenly quit without notice (which definetely helped with the stress) he slipped you a lottery ticket")
validScratch = False #Loop to ensure valid user input
while validScratch == False:
    scratch=float(input("Would you like to scratch the ticket (1) or keep it as a momento? (2) "))
    if scratch == 2: #Ends program early
        print("You decide to pin the lottery ticket on your bulletin board of memories and think back on the good times you shared")
        print("You then spend your nice bonus on some books, puzzles and video games to help unwind for the rest of your time off")
        break
    elif scratch == 1: #Continues program
        #pause...
        print("Oh. Oh my...")
        print(f"You Won! You won ${lottery}! And there's some travel agents info attached")
        print("It's definetely time for a vacation!")
        validScratch = True
    else:
        print("Invalid input!")

#nested dictionary on fleshed out facts: official languages, tourist attractions, culture, food
locations={ #quick base facts that need nested
    "Bologna, Italy": "Kimi Antonelli formula 1 20 year old WDC born here - not capital. Oldest still running university (1088 University of Bologna). UNESCO Porticoes. Discovery of tortellini tied to city. Hidden canals",
    "Barcelona, Spain": "Capital of Spain, 9 UNESCO World Heritage Sites. La Diada de Sant Jordi holiday celebrated on April 23. Catalan and Spanish",
    "Brussels, Belgium": "Capital of Belgium, NATO headquarters. French and Dutch. Census says very international feel with 180+ nationalities and 100+ languages. Airport biggest chocolate sales",
    "Vienna, Austria": "Capital of Austria, population 2 mil and on Danube river. Acts as city and 1 of Austria's 9 federal states. Once the capital of Austro-Hungarian Empire. Oldest zoo (1752) and oldest ferris wheel (1897). Home of Mozart, Beethoven and Schubert",
    "Oslo, Norway": "Capital of Norway, founded around 1048 by King Harald Hardrada but had name changes in 1624 and 1925. Nicknamed Tigerstaden (Tiger City) after poem, 1 of highest electric car rates in world. 6 hours sunlight in winter, 19 hours summer"
           }

#text walking simulator, 1 or 2 user input kind of situation based on selected location like in civil war example
#remember equations for purchased items to subtract from total and conversions for local currency
#3 max purchases - subtract random amount from USD total for flights