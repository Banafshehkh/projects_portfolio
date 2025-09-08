from random import randint

choices = ["rock", "paper", "scissors"]
computer_choice = choices[randint(0, 2)]
attempt = 0
human_score = 0
computer_score = 0

def validate_choice(choice):
    if choice == 'q':
        exit()
    elif choice not in choices:
        print("Invalid choice. Please try again.")
        return False
    return True

while attempt < 5:
    human_choice = input("Enter a choice (rock, paper, scissors):"). lower()
    computer_choice = choices[randint(0, 2)]

    if validate_choice(human_choice):
        if human_choice == computer_choice:
            print("It's a tie!")
        elif human_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            human_score += 1
        elif human_choice == "paper" and computer_choice == "rock":
            print("You win!")
            human_score += 1
        elif human_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            human_score += 1
        else:
            print("You lose!")
            computer_score += 1
        attempt += 1
print("Game over!")
print(f"Your score is {human_score}")
print(f"Computer score is {computer_score}")

