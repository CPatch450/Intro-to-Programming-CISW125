#Project 0, program 2. Ciara Patch 9/2/2026
print("Ugh! I'm so tired after a long day of classes!\nI'm starving!")
print("I have no idea what to make for dinner though...")
dinner=input("What should I make for dinner? ")
print(f"Hmmm... {dinner} does sound good")
pantry="eggs, chicken, syrup, bread, butter, noodles and strawberries"
print(f"It looks like I only have {pantry}")
print(f"Do I have what I need to make the {dinner} you suggested?")
ask=input("Y or N? ").upper()
if ask == 'N':
    print("Hmm... I'm too tired to go get groceries. I'll just makes noodles instead")
elif ask == 'Y':
    print(f"Okay perfect! I'll make {dinner} for dinner then! Thank you!")
else:
    print("Invalid input!")