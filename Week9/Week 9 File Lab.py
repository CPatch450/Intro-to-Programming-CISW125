#Week 9 notes, 10/14/26, Ciara Patch
#"r" for read
#"w" for write
#"a" for append

with open("Week9/file.txt","w") as file:
    file.write("Hello!\n I just did a lot of homework\n")

with open("Week9/file.txt","r") as file:
    contents=file.read()
    print(contents)


with open("Week9/file.txt","a") as file:
    file.write("It's definetely time to relax\n I like cheese pizza and TV\n")
    file.write("I think I'm going to watch a samurai show to help unwind")

with open("Week9/file.txt","r") as file:
    contents=file.read()
    print(contents)
