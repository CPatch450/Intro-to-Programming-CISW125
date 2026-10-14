#Week 9 Lab Challenge, 10/14/26, Ciara Patch
print("Me and my roommate don't have a lot of things in common, can you help me prepare to introduce myself?")
name1=input("What is my name? ")
name2=input("What is my roommates name? ")

with open("Week9/challenge.txt","r") as file:
    contents=file.read()
    print(contents)

with open("Week9/challenge.txt","w") as file: #Saves the earlier inputted info from the user to the file
    file.write(f"My name is {name1} and my roommates name is {name2}!\n")

food=input(f"What is {name2}'s favorite food? ").lower()
if food != "pizza":
    print("They definete;y have different taste than me")
else:
    print("Woah, we do have things in common!")

drink=input(f"What is {name2}'s favorite drink? ").lower()
if drink != "rootbeer":
    print("That's different")
else:
    print("Woah, we do have things in common!")

activity=input(f"What is {name2}'s favorite hobby? ").lower()
if drink != "watching tv":
    print("That's different than me")
else:
    print("Woah, we do have things in common!")

rmLikes=activity, food," and", drink

with open("Week9/challenge.txt","a") as file: #Prints the list of roommates likes to the file
    file.write(f" {name2} likes {rmLikes} then\n")
    file.write("Hopefully we get along well")

with open("Week9/challenge.txt","r") as file: #Reads the final results of the file
    contents=file.read()
    print(contents)

with open("Week9/challenge.txt","w") as file:
    file.write("Hello! I like cheese pizza, rootbeer and TV") #Returns the original writing in the file just in case there are issues with it while attempting to run the program multiple times