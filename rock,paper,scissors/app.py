import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, or scissors: ")
    computer_input = random.choice(options)
    
    if user_input == "exit":
        print("\nThanks for playing!")
        exit = True
        
    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is tie")
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("You lose this round.")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("Congratulations! You win the game!!")
            user_points += 1
            
    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("Congratulations! You win the game!!")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It is a tie.")
        elif computer_input == "scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("You lose this round")
            computer_points += 1
    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("You lose this round!")
            computer_points += 1
        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("Congratulations! You win the game!!")
            user_points += 1
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("It is a tie")
            