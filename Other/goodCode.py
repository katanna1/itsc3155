# Calculator Function - Good

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: division by zero."
    return a / b

def calculator():
    print("Select operation (1/2/3/4): ")
    print("1: Addition ")
    print("2: Subtraction ")
    print("3: Multiplication ")
    print("4: Divide ")

    choice = input("Enter choice (1/2/3/4): ")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print(f"{a}+{b} = {add(a, b)}")
    elif choice == "2":
        print(f"{a}-{b} = {subtract(a, b)}")
    elif choice == "3":
        print(f"{a}*{b} = {multiply(a, b)}")
    elif choice == "4":
        print(f"{a}/{b} = {divide(a, b)}")
    else:
        print("Invalid choice")

calculator()