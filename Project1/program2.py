#Project 1, porgram 2 (Math), Ciara Patch

print("I recently heard that you took a trip to Brazil! That's so cool!")
print("That's gotta be a long flight though, and you'll definetely have had some lay overs")
print("Let's calculate how many miles you travelled the whole trip!")
car1=float(input("How far is the airport from your house? "))
flight1=float(input("How many miles was your first flight? "))
flight2=float(input("How many miles was your second flight? "))
car2=float(input("How many miles was tha taxi ride between gates? I heard that second airport was massive. "))
flight3=float(input("How many miles was your final flight to Brazil? " ))
car3=float(input("How far was your hotel from the airport? "))
car4=float(input("I heard you also went on that crazy city tour of Rio that was half by car and half by foot. How long was that? "))
flightBrazilTotal= flight1 + flight2 + flight3
flightTotal= flightBrazilTotal * 2
carBrazilTotal= car1 + car2 + car3 + car4
carTotal= carBrazilTotal * 2 - car4

print("Wow you did a lot of travelling!")
print(f"You travelled {flightBrazilTotal} miles by plane on the way to Brazil and {flightTotal} total!")
print(f"You travelled {carBrazilTotal} miles by car the first half of your trip and you travelled {carTotal} miles by car total!")

print("Speaking of of numbers and Brazil, I bet that hotel was expensive")
cost=float(input("How expensive was the hotel? "))
stay=float(input("and how many nights did you stay in Brazil again? "))
nightlyCost = cost / stay
print(f"Wow! so they were charging {nightlyCost} per night!")