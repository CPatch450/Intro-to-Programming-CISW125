#Project 4, program 1, 10/28/2026, Ciara Patch
import random

def play(): #Fake loop that asks the user to play again
    playagain=input("Do you want to play again? (y/n) ").lower()
    if playagain == "y":
        ask()
    elif playagain == "n": #If user does not want to play again, it prints out the dice rolls from the text file
        with open("Week11/dice.txt","r") as file:
            contents=file.read()
            print(f"Here is the log of your plays:\n{contents}")
    else:
        print("Invalid input!")

def dice(tries): #Tries is the number of dice rolls
    while tries > 0:
        num1 = random.randint(0, 6) #Generating the random number on the dice
        num2 = random.randint(0, 6)
        print (f"{num1},  {num2} \n")
        with open("Week11/dice.txt","a") as file: #Saving the number to the text file
            file.write(f"{num1},  {num2}\n")
        if num1 == 1 and num2 == 1: #Ends the program if the user gets doubles
            print("You got snake eyes! Woah!")
            break
        elif num1 == num2:
            print("You got doubles!")
            break
        else:
            tries -= 1
        if tries == 0: #If user doesnt get doubles it goes back to the fake loop
            print("Wow... You didn't get a single one")
            play()

def ask(): #Gets user input to ask for the number of dice rolls
    roll=float(input("How many rolls of the dice do you want to do? "))
    dice(roll)
    
print("Lets play a game! The aim is to get doubles")
ask()



