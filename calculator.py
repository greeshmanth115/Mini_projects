#-----------------Basic Calculator-------------------
print("Welcome to Calculator 🤝")

# Function to get a valid number
def get_number(message):
    while True:
        num = input(message)
        if num == "":
            print("Please enter a value!")
            continue
        try:
            return int(num)
        except ValueError:
            print("Invalid input! Please enter a number.")

# Function to get a valid operator
def get_operator():
    while True:
        op = input("Enter the operator (+, -, *, /): ")
        if op == "":
            print("Please enter a symbol!")
        elif op in "+-*/":
            return op
        else:
            print("Invalid operator!")

a = get_number("Enter the first number: ")
b = get_number("Enter the second number: ")
c = get_operator()

if c == "+":
    print("Result:", a + b)
elif c == "-":
    print("Result:", a - b)
elif c == "*":
    print("Result:", a * b)
else:
    try:
        print("Result:", a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero!")