#Project 4, program 1, 10/28/2026, Ciara Patch
import random

def dice(tries):
    while tries > 0:
        num1 = random.randint(0, 6)
        num2 = random.randint(0, 6)
        print (f"{num1},  {num2} \n")
        with open("Week11/dice.txt","a") as file:
            file.write(f"{num1},  {num2}")
        if num1 == 1 and num2 == 1:
            print("You got snake eyes! Woah!")
        elif num1 == num2:
            print("You got doubles!")
            break
        else:
            tries -= 1
        if tries == 0:
            print("Wow... You didn't get a single one")


def play():
    print("Lets play a game! The aim is to get doubles")
    roll=float(input("How many rolls of the dice do you want to do? "))
    dice(roll)
    

print("Lets play a game! The aim is to get doubles")
rolls=float(input("How many rolls of the dice do you want to do? "))
dice(rolls)

playagain=input("Do you want to play again? (y/n) ").lower()
if playagain == "y":
    rolls=float(input("How many rolls of the dice do you want to do? "))
    play()
elif playagain == "n":
    with open("Week11/dice.txt","r") as file:
        contents=file.read()
        print(f"Here is the log of your plays: {contents}")
else:
    print("Invalid input!")

