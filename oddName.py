"""
Chloe Jane Coleman
"""
name = input("Please enter your name")
while name == "":
    name = input("Your name must have at least one character \nPlease enter your name")
print(name[::2])
