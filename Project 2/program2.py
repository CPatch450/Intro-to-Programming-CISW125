#Project 2, program 2. Ciara Patch

print("Let's see how many airline rewards you have after your summer vacation")
total = float(input("How many miles did you fly in total? "))
premium = False
premiumAsk = input("Are you a premium member? (Y or N) ")
if premiumAsk.upper() == "Y":
    premium = True
if total < 0:
    print("You qualify for nothing")
elif total < 150:
    print("You have 20 free miles")
    if premium == True:
        print("and a free meal with your premium membership")
elif total < 300:
    print("You have 50 free miles and a free 3 hour rental car")
    if premium == True:
        print("and 2 free meals with your premium membership")
elif total < 500:
    print("You have 75 free miles and a free 6 hour rental car")
    if premium == True:
        print("and 1 free night at an associated hotel with your premium membership")
else:
    print("You have 100 free miles, a free meal and a free 6 hour rental car")
    if premium == True:
            print("and 2 free nights at an associated hotel with your premium membership")