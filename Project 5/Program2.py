#Project 5, program 2 (Dictionaries), Ciara Patch
def tickets(price, money, travel):
    print(f"Tickets for {travel} cost {price}")
    tickets=round(money/price)
    if tickets >= 1:
        print(f"It looks like you can afford {tickets} tickets!")
    else:
        print("It looks like you can't afford these tickets right now sorry!")

def travelAsk():
    validCity = False
    while validCity == False:
        money=float(input("How much USD do you have? "))
        if money < 0:
            print("Invalid!")
        else:
            travel=input("What concert would you like to go to? ").lower()
            if travel == "seattle" or travel == "new york":
                print("Perfect! There is no conversion needed for these tickets")
                tickets(165, money, travel)
                validCity = True
            elif travel == "tokyo":
                money=money/0.0063
                print(f"With the conversion rate, you have {money} Yen")
                tickets(10038, money, travel)
                validCity = True
            elif travel == "seoul":
                money=money/0.00075
                print(f"With the conversion rate, you have {money} Won")
                tickets(20043, money, travel)
                validCity = True
            elif travel == "vancouver":
                money=money/0.7
                print(f"With the conversion rate, you have {money} Canadian Dollars!")
                tickets(220, money, travel)
                validCity = True
            elif travel == "stockholm":
                money=money/0.098
                print(f"With the conversion rate, you have {money} Krona")
                tickets(1400, money, travel)
                validCity = True
            else:
                print("Invalid input!")

def rateAsk():
    overallAsk=input("Would you like to see the conversion rates between the other countries while we're at it? y/n ").lower()
    loop = True
    while loop == True:
        if overallAsk == "y":
            convChoice=input("What currency would you like to see the rates of? (japenese yen, korean won, canadian dollars, euro, swedish krona)").lower()
            for currencies, values in overall[convChoice].items():
                print(f"{currencies} : {values}")
            usdAsk=input("Would you like to see the USD rates? y/n ").lower()
            if usdAsk == "y":
                for currencies, values in usd.items():
                    print(f"{currencies} : {values}")
            again=input("Would you like to check more rates? ").lower()
            if again == False:
                loop = False
        else:
            loop = False

usd={
    "japenese yen":0.0063,
     "korean won": 0.00075,
     "euro": 1.10,
     "canadian dollar":0.7,
     "swedish krona":0.098}

overall={
    "japenese yen":{
        "korean won": 8.37,
        "euro": 0.0057,
        "canadian dollar": 0.009,
        "swedish krona": 0.064
    },
     "korean won":{
        "japanese yen": 0.12,
        "euro": 0.00068,
        "canadian dollar": 0.0011,
        "swedish krona": 0.0076
    },
     "euro":{
        "japanese yen": 174.9,
        "korean won": 1462.23,
        "canadian dollar": 1.57,
        "swedish krona": 11.16
     },
     "canadian dollar":{
        "japanese yen": 111.25,
        "korean won": 0.0057,
        "euro": 0.009,
        "swedish krona": 0.064
     },
     "swedish krona":{
        "japanese yen": 8.37,
        "korean won": 0.0057,
        "canadian dollar": 0.009,
        "euro": 0.009,
     } 
}

cities=["Tokyo", "Seoul", "Berlin", "Vancouver", "Seattle", "New York", "Stockholm"]
print("Your favorite msuic artist is going on a world tour and you just got a bonus at work!")
print(f"The cities being visited are:\n {cities}")
showRates=input("Would you like to see the conversion rates for the local currencies of the tickets to USD? y/n ").lower()
if showRates == "y":
    for currencies, values in usd.items():
        print(f"{currencies} : {values}")
        
print("=========================")
travelAsk()
print("=========================")
rateAsk()










