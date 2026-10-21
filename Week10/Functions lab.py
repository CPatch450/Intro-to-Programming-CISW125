#Functions Lab, 10/21/2026, Ciara Patch
def greet_user(user): #Task 1, user greeting function
    print(f"Good morning {user}! Let's get started!")

def calc(a, b): #Task 2, calculator function
    choice=input("Would you like to do +, -, * or /? ")
    result=0
    if choice == "+":
        add=a+b
        result=add
    elif choice == "-":
        sub=a-b
        result=sub
    elif choice == "*":
        mult=a*b
        result=mult
    elif choice == "/":
        divide=a/b
        result=divide
    else:
        print("Invalid input!")
        calc(a, b) #If user enters none of the calc functions, they get asked again through a fake loop
    print(f"{a}{choice}{b}={result}")

def dig_counter(word): #Task 3, returns the length of an inputted word
    count=len(word)
    print(f"there are {count} digits in {word}")
    return count #returning the number of letters in the inputted word
    

def play(): #Task 4, the fake loop function
    word=input("Pick a plant: ")
    print("That's a cool plant!")
    ask=input("Would you like to play again? y/n ").lower()
    if ask == "y":
        play()

name=input("What is your name? ")#Task 1, gets the name so that it can input it into the parameters
greet_user(name)

num1=float(input("Pick a number above 0: ")) #Task 2, gets the 2 numbers so they can be put into the parameters
num2=float(input("Pick a number greater than the first one: "))
if num1 >= num2 or num1 <= 0: #Checking for valid numbers
    print("Invalid")
else:
    calc(num1, num2)

user_word=input("Enter a word: ")#Task 3, getting the parameter
dig_counter(user_word) #Calling the function
play()#Task 4, calling the fake loop function

#Reflection:
#I feel pretty comfortable working with functions. I took a C++ class last year, and the entire course ran on functions and the use of global variables.
#I do really like functions, they make life so much easier, especially when you start to get into programs that have complex math equations and long loops or if else statements.
#I don't have any questions, I am excited to use functions in the next project though!