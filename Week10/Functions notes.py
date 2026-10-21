def say_hello():
    print("Hello!")

def counting(x):
    y=0
    for i in range (0, x):
        print(y)
        y+=1

def math():
    a=float(input("Pick a number above 0: "))
    b=float(input("Pick a number greater than the first one: "))
    if a >= b or a <= 0:
        print("Invalid")
        math()
    else:
        multiply=a*b
        divide=a/b
        return (f"{a} multiplied by {b} is {multiply}\n{a} divided by {b} is {divide}")

say_hello()
counting(3)
print (math())