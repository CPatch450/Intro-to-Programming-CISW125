x=5
y=6
z=x//y
subtraction=x-y
division=x/y
multiplication=x*y
square = x**x


print(f"The value of {x} + {y} is {x + y}")
print(f"The value of {x} - {y} is {z}")
print(f"Heres some basic math equations:")
print(f"{x} / {y} = {division} \n {x} x {y} = {multiplication} \n {x} // {y} = {z}")
print(f"The square of {x} is {square}")

groceryList="apples, bananas, oranges, bread, milk, chicken"
print(f"I'm getting groceries later. I'm buying {groceryList}")
snack=input("What snack do you want? ")
space=" and "
fullList= groceryList + space + snack
print(f"Okay I will buy {fullList}")

first=input("What is your first name? ")
last=input("What is your last name? ")
print(f"Your full name is {first + last}")

numberI=input("Enter a number 1-10: ")
number=float(numberI)
if number > 10:
    print("Invalid number")
elif number < 0:
    print("Invalid number")
else:
    print(f"The number you entered was {number}")