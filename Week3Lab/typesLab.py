#Types Lab, Ciara Patch 9/2/2026
fl=2.0 #Match Section
integer=3
#You can still do math using a float and an integer. The outcome of the math will be a float- which is really helpful
#when you start adding in decimals and complex math equations or functions
math= fl - integer
print(type(math))
fl=input("Enter a number: ")
integer=input("Enter a number: ")
print(f"{fl}, {integer}")

grocery="eggs, chicken, syrup, bread, butter, noodles and strawberries" #String Section
space=", "
#A string is a special kind of variable that contains communications or objects using letters, words or numbers and uses quotes
allErrands="super glue, notebooks, pencils" + space + grocery
print(allErrands)
print(grocery[0])
substring=allErrands[4:8]
print(substring)

artSupplies=["paint brushes", "watercolor paint", "erasers", "pens"]#List Section
#A list can contain any kind of variable or data. A list is simply a list of a data
artSupplies.append("acrylic paint", "markers", "pencils", "canvases")
print(artSupplies)
artSupplies.remove("pens")
print(artSupplies)
print(len(artSupplies))

#Summary
#In this lab I recapped how to create, add onto and remove from lists, as well as combining strings and an overview of math.
#This will definetely make labs and projects that focus on combined data/related information that neewds to be stored together a lot easier. A
#good example of a lab I've done in the past where the use of lists combinations of strings was heavily used was one where you had to store the
#name of all of the employees for a company as well as their salary and job title. I'm sure there will be many projects in class and in jobs in
#the future that will need the similair use of lists and strings.