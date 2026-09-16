#Branching Lab, Ciara Patch
name=input("Enter your name: ")
print("Lets check what grade you have in your math class")
print("Grades are defined as: F = 0 - 59, D = 60 - 69, C = 70 - 79, B = 80 - 89, A = 90 - 100")
grade=float(input("Enter your grade in your math class: "))
if grade < 0 or grade > 100:
    print("Invalid!")
elif grade < 60:
    print("It looks like you have an F. You might want to study harder")
elif grade < 70:
    print("It looks like you have a D")
elif grade < 80:
    print("It looks like you have a C")
elif grade < 90:
    print("It looks like you have a B")
else:
    print("You have an A! Well done!")

print("\nNow let's classify your age group")
age=float(input("How old are you? "))
if age < 0 or age > 200:
    print("I don't think so...")
elif age < 5:
    print("You are a toddler")
elif age < 13:
    print("You are a kid")
elif age < 18:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")

print("\nLet's calculate if you qualify for a discount")
bought=float(input("How much did your purchase cost? "))
if bought < 0 or bought > 250:
    print("Invalid")
elif bought < 30:
    print("You do not qualify for a discount! Sorry!")
elif bought < 50:
    print("You qualify for a 5 percent discount")
elif bought < 100:
    print("You qualify for a 10 percent discount")
else:
    print("You qualify for a 15 percent discount")
