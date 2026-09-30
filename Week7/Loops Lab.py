#Loops Lab, 9/30/2026, Ciara Patch
for i in range (0, 6): #Part 1
    print(i)
    i+=1

nameLen=float(input("How many letter are in your name? ")) #Part 2
while nameLen<0 or nameLen>100:
    print("Invalid. Try again")
    nameLen=float(input("How many letter are in your name? "))

groceries=["apples", "butter", "bread", "bacon"] #Part 3
for i in groceries:
    print(i)

for i in range (2, 8): #Part 4
    print(f"number is {i}")
    square=i*i
    print(f"square is {square}")
    i+=1

name="Ciara" #Part 5
for i in name:
    print(i)

for i in range (1, 11): #Part 6
    print(i)
    i+=1
    if i == 8:
        break

for a in range (1, 10): #Part 7
    for b in range (5, 15):
        print(f"a = {a}")
        print(f"b = {b}")
#The loop starts by repeating the first loop once, then the second, then restarting. When it hits the second loop though it increments it by 1 while the first loop stays the same
#Then once the variable in the second loop hits the end variable (15) in the range, the first loops variable is incremented by 1 and the process restarts
