import random
yes_count = 0
while True:

    choice = ("rock", "paper", "scissor")
    computer = random.choice(choice)
    
    player = None
    while player not in choice:
        player = input("Enter your choice: ") .lower()

    if computer == player :
        print ("Computer",computer)
        print("Player",player)
        print("It's tie!🤝")

    elif player == "rock":
        if computer == "paper":
            print ("Computer",computer)
            print("Player",player)
            print("You dont know ho to play!🤪")
        elif computer == "scissor":
            print ("Computer",computer)
            print("Player",player)
            print("You win!🥳")
    elif player == "paper":
        if computer == "rock":
            print ("Computer",computer)
            print("Player",player)
            print("You win!🥳")
        elif computer == "scissor":
            print ("Computer",computer)
            print("Player",player)
            print("You dont know ho to play!🤪")
    elif player == "scissor":
        if computer == "paper":
            print ("Computer",computer)
            print("Player",player)
            print("You win!🥳")
        elif computer == "rock":
            print ("Computer",computer)
            print("Player",player)
            print("You dont know ho to play!🤪")
    
    again = input("Do you want to continue (yes/no):") .lower()

    if again == "yes":
        yes_count += 1
    else:
        print ("You played", yes_count, "times")
        break

print("Thanks for playing!")