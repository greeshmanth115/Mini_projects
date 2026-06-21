#------------Basic calculater---------------
print("Welcom to calculator🤝")

while True: 

    a = input("Enter a first number: ")

    if a =="":
        print("Please enter a value!")
    
    try:
        a = int(a)

        break
    except ValueError:
        print("Invalid Input in numbers!")

while True:
    b = input("Enter a second number: ")

    if b =="":
        print("Please enter a value!")
    try:
        b = int(b)
        break
    except ValueError:
        print("Invalid Input in numbers!")

while True:

    c = input("Enter the symbol you want to calculate(+,-,*,/): ")

    if c =="":
        print("Please enter a symbol!")
    
    try:

        if c not in ("+","-","*","/"):
            print("Invalid Input in symbols!")
        break
    except ValueError:
        print("Invalid Input in numbers!")

if c == "+":
    add = a+b
    print("Addition of your two number is:",str(add))

elif c == "-":
    sub = a-b
    print("Subtraction of your two number is:",str(sub))

elif c == "*":
    mul = a*b
    print("Multiplication of your two number is:",str(mul))
elif c == "/":
    try:
        div = a/b
        print("Division of your two number is:",str(div))

    except ZeroDivisionError:
        print("Number cannot divided by zero you idiot!")