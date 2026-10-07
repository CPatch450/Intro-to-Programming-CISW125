#Project 3, program 1 finite loop, Ciara Patch
num=float(input("Enter a number: "))
ask=(input("Do you want to double (d) or half (h) your number? ")).lower()
repeats=int(input("How many times? "))
x=0
for x in range (0, repeats):
    if ask =="h":
        num=num/2
    elif ask =="d":
        num=num*2
    else:
        print("Invalid input!")
        break
    x+=1
    print(f"num {x} is: {num}")
