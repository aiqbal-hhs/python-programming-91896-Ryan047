thelist = ["Add", "add", "Multiply", "multiply", "Divide", "divide","Subtract", "subtract"]

def Multiply(x,y):
    z = x * y
    print(z)

def Divide(x,y):
    x = float(x)
    y = float(y)
    z = x / y
    print(z)

def Add(x,y):
    z = x + y
    print(z)

def Subtract(x,y):
    z = x - y
    print(z)

while True:
    operation = input("What would you like to do? Multiply/Divide/Add/Subtract ")
    if operation in thelist:
        break
    else:
        print("That was not an option..")

if operation == "Multiply" or operation == "multiply":
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    while True:
        try:
            y = int(input("Second number: "))
            break
        except ValueError:
            print("Make sure to enter a number...")
    Multiply(x,y)
elif operation == "subtract" or operation == "Subtract":
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    while True:
        try:
            y = int(input("Second number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    Subtract(x,y)
elif operation == "Add" or operation == "add":
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number..")
    while True:
        try:
            y = int(input("Second number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    Add(x,y)
elif operation == "Divide" or operation == "divide":
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    while True:
        try:
            y = int(input("Second number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    Divide(x,y)
else:
    passs
