#Project 3, program 2 infinite loop, Ciara Patch
print("Let's calculate how much money you spent this month by adding up all your receipts")
x=1
total=0
while True:
    price=float(input(f"Enter the price of reciept {x}: "))
    total=total+price
    ask=input("Is that the last reciept? (y/n) ").lower()
    if ask == "y":
        print(f"You spent {total} this month!")
        break
    elif ask == "n":
        x+=1
    else:
        print("Invalid input!")
        break

