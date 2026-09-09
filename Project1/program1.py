#Project 1, porgram 1 (Inputs), Ciara Patch

print("Let's play wheel of facts and do some ice breakers!") #Initializing
name=input("What is your name? ")
age=input("How old are you? ")

num=input("What's your favorite prime number? ") #Questions for the wheel
food=input("What's your favorite tropical fruit? ")
breakfast=input("What's your least favorite breakfast food? ")
job=input("Would you rather work day shift outside or night shifts inside for a job? ")
vacation=input("Would you rather canoe down a river in a rain forest or sand ski down a sand dune in a desert? ")
wheel=float(input("Pick a number between 1 and 5 and I'll spin the fact wheel! "))
print(f"Your name is {name}! You are {age} years old")
if wheel > 5 or wheel < 1:
    print("and you don't know how to read instructions the first time.") #I'm joking


if wheel ==1:
    print(f"and your favorite prime number is {num}")
elif wheel == 2:
    print(f"and your favorite tropical fruit is {food}")
elif wheel == 3:
    print(f"and your least favorite breakfast food is {breakfast}")
elif wheel == 4:
    print(f"if given the choice between working day shifts outside or night shifts inside, you chose {job}")
elif wheel == 5:
    print(f"when asked if you would rather canoe down a river in a rain forest or sand ski down a sand dune in a desert, you chose {vacation}")