import random
#for count how many times you played
yes_count = 0
#to play again
while True:

    choice = ("rock", "paper", "scissor")
    computer = random.choice(choice) #computer choice

    #to enter correct value
    player = None
    while player not in choice:
        player = input("Enter your choice: ") .lower()
    #actual game
    if computer == player :
        print ("Computer",computer)
        print("Player",player)
        print("It's tie!🤝")

    elif player == "rock" and computer == "scissor" or player == "paper" and computer == "rock" or player == "scissor" and computer == "paper":
        print ("You win!🥇")

    else :
        print ("You lost🫢")
    #want to play again or not
    again = input("Do you want to continue (yes/no):") .lower()

    if again == "yes":
        yes_count += 1 #for count
    else:
        print ("You played", yes_count + 1, "times")
        break

print("Thanks for playing!🥰")