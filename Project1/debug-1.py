# Intro to Programming
# Debug Exercise 2

# This program should add three numbers together.
#Ciara Patch, 9/9/2026
total = 0
num1 = input("What's the first number? >")
total = float(num1) #Made sure to convert string input to float for all variables labelled total
num2 = input("What's the second number? >")
total = float(num2) + total #added num2 to total instead of overwriting it
num3 = input("What's the third number? >")
total = float(num3) + total #added num3 to total instead of overwriting it
print(f"Total of {num1}, {num2} and {num3} is {total}")