#Week 12 Lab, 11/4/2026, Ciara Patch
#Lists also have the functions: .append("item"), .instert([place], "item"), .sort(), .reverse() and .count("item")
#Dictionaries can have just their keys/values printed with .keys() and .values() or .items() for both, dictionaries can be nested with other dictionaries or lists

shoppingCart=["apples", "bananas", "bread", "milk", "eggs"] #Lists
print(len(shoppingCart))
print(shoppingCart[2])
shoppingCart.append("oranges")
shoppingCart.insert(3, "chocolate")

print(shoppingCart) #List methods
print(shoppingCart.count("butter")) 
shoppingCart.remove("bananas")
print(shoppingCart)
shoppingCart.sort() #Outcome is the list getting sorted alphabetically in descending order
print(shoppingCart)
shoppingCart.reverse() #Outcome is reversing the sort so the list is aplhabetized in ascending order
print(shoppingCart)

inventory={ #Dictionaries
    "apples":15,
    "oranges":30,
    "bread loafs":20,
    "eggs":10,
    "potatoes":5
}
print(inventory["apples"])
inventory["grapes"]=25
inventory["apples"]+=5
print(inventory)

for keys in inventory.keys(): #Iterating over dictionaries
    print(keys)
for values in inventory.values():
    print(values)
for keys, values in inventory.items():
    print(f"{keys} : {values}")

customers={ #Nested dictionaries
    "01":{
        "Name":"John",
        "Items Bought":["apples", "bread", "grapes"],
        "Total": 25.60
    },
    "02":{
        "Name":"Jennifer",
        "Items Bought":["eggs", "potatoes"],
        "Total": 8.12
    }
}
print(customers["02"]["Items Bought"])

#I've used dictionaries and lists before in previous classes, but I didn't know about the sort features for the lists. Suprisingly I don't think I've nested dictionaries
#within each other either, just lists within dictionaries, or if I did then I forgot. Nesting dictionaries is actually really useful and I think I'll plan my final project
#around a nested dictionary function similair to the civil war example you shared. I'm not sure what topic I would want my dictionary to cover yet though, I'm sure I'll
#come up with some ideas when I use dictionaries and lists in project 5
