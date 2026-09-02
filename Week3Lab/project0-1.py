#Project 0, program 1. Ciara Patch 9/2/2026
print("Wow! It's a beautiful day!\nYou should get some fresh air!")
print("Do you live in the Boise area or the Twin Falls area?")
validArea = False
while validArea == False:
    areaAsk=input("Enter 1 for Boise or 2 for Twin Falls: ")
    area=float(areaAsk)
    if area > 2:
        print("Invalid entry! Try again!")
        validArea = False
    elif area < 1:
        print("Invalid entry! Try again!")
        validArea = False
    else:
        validArea = True

print("Perfect! I know some great places in the area!")
if area == 1:
    print("The Boise greenbelt is a really nice place to enjoy a slow walk!")
    print("Or you can hike up the Old Penitentiary Trailhead if you want a higher energy activity")
if area ==2:
    print("If you're looking for a calm walk, the fitness trail on the CSI Campus or the City Park are great spots!")
    print("If you would prefer to go on a hike, the Auger Falls Trailhead is a beautiful hike")
