import time
print("Welcome to our food ordering system...!😋")
count = 0
while True: #for counting orders

    menu = ["Pizza(1)", "Burger(2)", "Chicken Roll(3)", "Sushi(4)", "Fries(5)"]
    order = ["1", "2", "3", "4", "5"]
    print("Please select for the below menu")
    print("⬇︎".center(8, " "))
#Displaying the menu with a delay
    for i in menu:
        time.sleep(0.8)
        print(i)
#forcing the user to enter a valid item number
    a = ""
    while len(a) == 0:
        time.sleep(0.5)
        a = input("Enter the item number you want to order: ")
#ordering process based on the item number selected
#pizza
    if a in order[0]:
        print("Size: small(1), medium(2), large(3): ")
        p = input("Please enter number for size: ")
        if p == "1":
            print("You have selected small pizza")
        elif p == "2":
            print("You have selected medium pizza")
        elif p == "3":
            print("You have selected large pizza")
        else:
            print("Invalid size selection")
        print("Please wait for the order")
        print("Thank you! Have a great meal, Visit again...😄")
#burger
    elif a in order[1]:
        print("Size: small(1), medium(2), large(3): ")
        p = input("Please enter number for size: ")
        if p == "1":
            print("You have selected small burger")
        elif p == "2":
            print("You have selected medium burger")
        elif p == "3":
            print("You have selected large burger")
        else:
            print("Invalid size selection")
        print("Please wait for the order")
        print("Thank you! Have a great meal, Visit again...😄")
#chicken roll
    elif a in order[2]:     
        print("Size: small(1), medium(2), large(3): ")
        p = input("Please enter number for size: ")
        if p == "1":
            print("You have selected small chicken roll")
        elif p == "2":
            print("You have selected medium chicken roll")
        elif p == "3":
            print("You have selected large chicken roll")
        else:
            print("Invalid size selection") 
        print("Please wait for the order")
        print("Thank you! Have a great meal, Visit again...😄")       
#sushi
    elif a in order[3]:
        print("Size: small(1), medium(2), large(3): ")
        p = input("Please enter number for size: ")
        if p == "1":
            print("You have selected small sushi")
        elif p == "2":
           print("You have selected medium sushi")
        elif p == "3":
            print("You have selected large sushi")
        else:
            print("Invalid size selection")
        print("Please wait for the order")
        print("Thank you! Have a great meal, Visit again...😄") 
#fries
    elif a in order[4]:
        print("Size: small(1), medium(2), large(3): ")
        p = input("Please enter number for size: ")
        if p == "1":
            print("You have selected small chips")
        elif p == "2":
            print("You have selected medium chips")
        elif p == "3":
            print("You have selected large chips")
        else:
            print("Invalid size selection")

        print("Please wait for the order")
        print("Thank you! Have a great meal, Visit again...😄")
#invalid item number

    else: 
        print("Sorry, We don't have that item on the menu.")
        print("Thank you! Visit again...😄")
    #for counting orders
    another = input("Do you want any other item (Yes/No)") .lower()
    
    if another == "yes":
        count += 1
    else :
        print("You ordered", count+1, "items!")
        break
print("Please wait for the order")
print("Thank you! Have a great meal, Visit again...😄")