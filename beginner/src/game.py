import random


class RockPaperScissors:
    def __init__(self, name):
        self.player_name = name
        self.choices = ["rock", "paper", "scissors"]

    def get_player_choice(self):
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in self.choices:
            print("Invalid choice. Please try again.")
            return self.get_player_choice()
        return user_choice.lower()

    def get_computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, computer_choice, user_choice):
        if computer_choice == user_choice:
            return "It's a tie!"
        elif computer_choice == "rock" and user_choice == "scissors":
            return "You lose!"
        elif computer_choice == "paper" and user_choice == "rock":
            return "You lose!"
        else:
            return "You win!"

    def play(self):
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(computer_choice , user_choice)
        print(self.decide_winner(computer_choice, user_choice))

if __name__ == "__main__":
    game = RockPaperScissors("Banafsheh")

    while True:
        game.play()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break