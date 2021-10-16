import random

print("Let the game begin! First one to score 5 points wins! All the best!")
actions = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0

while(True):
    user = int(input("Enter 1 for rock, 2 for paper, 3 for scissor: "))
    computer = random.choice(actions)

    if user == 1 and computer == "rock":
        print("Computer did rock")
        print("It's a tie")
        print("Your current score is: ", user_score)
        print("Computer's current score is: ", computer_score)
        if user_score > computer_score and user_score >= 5:
            print("Game over, you won. Congrats!")
            exit()
        elif computer_score > user_score and computer_score >= 5:
            print("Game over, you lost. Better luck next time")
            exit()

    elif user == 1 and computer == "paper":
        print("Computer did paper")
        print("Computer won")
        computer_score += 1
        if user_score > computer_score and user_score >= 5:
            print("Game over, you won. Congrats!")
            exit()
        elif computer_score > user_score and computer_score >= 5:
            print("Game over, you lost. Better luck next time")
            exit()
        print("Your current score is: ", user_score)
        print("Computer's current score is: ", computer_score)

    elif user == 1 and computer == "scissor":
        print("Computer did scissor")
        print("You won")
        user_score += 1
        if user_score > computer_score and user_score >= 5:
            print("Game over, you won. Congrats!")
            exit()
        elif computer_score > user_score and computer_score >= 5:
            print("Game over, you lost. Better luck next time")
            exit()
        print("Your current score is: ", user_score)
        print("Computer's current score is: ", computer_score)

    elif user == 2 and computer == "rock":
        print("Computer did rock")
        print("You won")
        user_score += 1
        if user_score > computer_score and user_score >= 5:
            print("Game over, you won. Congrats!")
            exit()
        elif computer_score > user_score and computer_score >= 5:
            print("Game over, you lost. Better luck next time")
            exit()
        print("Your current score is: ", user_score)
        print("Computer's current score is: ", computer_score)

    elif user == 2 and computer == "paper":
        print("Computer did paper")
        print("It's a tie")
        print("Your current score is: ", user_score)
        print("Computer's current score is: ", computer_score)
        if user_score > computer_score and user_score >= 5:
            print("Game over, you won. Congrats!")
            exit()
        elif computer_score > user_score and computer_score >= 5:
            print("Game over, you lost. Better luck next time")
            exit()

    elif user == 2 and computer == "scissor":
        print("Computer did paper")
        print("Computer won")
        computer_score += 1
        if user_score > computer_score and user_score >= 5:
            print("Game over, you won. Congrats!")
            exit()
        elif computer_score > user_score and computer_score >= 5:
            print("Game over, you lost. Better luck next time")
            exit()
        print("Your current score is: ", user_score)
        print("Computer's current score is: ", computer_score)

    elif user == 3 and computer == "rock":
        print("Computer did paper")
        print("Computer won")
        computer_score += 1
        if user_score > computer_score and user_score >= 5:
            print("Game over, you won. Congrats!")
            exit()
        elif computer_score > user_score and computer_score >= 5:
            print("Game over, you lost. Better luck next time")
            exit()
        print("Your current score is: ", user_score)
        print("Computer's current score is: ", computer_score)

    elif user == 3 and computer == "paper":
        print("Computer did rock")
        print("You won")
        user_score += 1
        if user_score > computer_score and user_score >= 5:
            print("Game over, you won. Congrats!")
            exit()
        elif computer_score > user_score and computer_score >= 5:
            print("Game over, you lost. Better luck next time")
            exit()
        print("Your current score is: ", user_score)
        print("Computer's current score is: ", computer_score)

    elif user == 3 and computer == "scissor":
        print("Computer did rock")
        print("It's a tie")
        print("Your current score is: ", user_score)
        print("Computer's current score is: ", computer_score)
        if user_score > computer_score and user_score >= 5:
            print("Game over, you won. Congrats!")
            exit()
        elif computer_score > user_score and computer_score >= 5:
            print("Game over, you lost. Better luck next time")
            exit()

    else:
        print("Invalid")

