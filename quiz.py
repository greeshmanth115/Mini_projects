#---------------Quiz game-----------------
count = 0 #count how many times you played

def new_game():

    guesses = [] #empty guesses list
    correct_guesses = 0
    question_num = 1
    for key in questions: #prints question
        print("---------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)

        guess = input("Enter (A, B, C or D): ") .upper()
        guesses.append(guess)#store in guesses list
        question_num += 1
        correct_guesses += check_answer(questions.get(key),guess) #questios.get(key)=answer
    display_score(correct_guesses,guesses)

def check_answer(answer,guess):
    if answer == guess :
        print("CORRECT!")
        return 1 #score +1
    else:
        print("WRONG!")
        return 0 #score +0
    
def display_score(correct_guesses,guesses):
    print("---------------------------------")
    print("RESULTS!")
    print("---------------------------------")
    #correct ans
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    #guess ans
    print("guesses:", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    #score
    score = int((correct_guesses / len(questions))*100)
    print("Your score: ", str(score), "%")

def play_again():
    response = input ("Do you want to play again (Yes/No): ") .lower()
    if response == "yes":
        return True
    else :
        return False

questions = {"Who created Python?: ": "A",
             "What year was Python created?: ": "B",
             "Python is tributed to which comedy group?: ": "C",
             "Is the Earth round?": "A"}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's"]]

new_game()

while play_again():
    new_game()
    count += 1
    print("You played",count+1,"times")
    
print("Thanks for playing!")