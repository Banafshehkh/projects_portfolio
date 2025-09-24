import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 10  # We use 1-9 for convenience, 0 is ignored
        self.player_turn = self.get_random_first_player()

    def get_random_first_player(self):
        return 'X' if random.randint(0, 1) == 0 else 'O'

    def fix_spot(self, cell, player):
        self.board[cell] = player

    def has_player_won(self, player):
        #check all combinations
        win_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                            (1, 4, 7), (2, 5, 8), (3, 6, 9),
                            (1, 5, 9), (3, 5, 7)]
        for combination in win_combinations:
            if all(self.board[cell] == player for cell in combination):
                return True
        return False

    def is_board_filled(self):
        #check all cells are not empty
        return all(cell != ' ' for cell in self.board[1:])

    def swap_player_turn(self):
        self.player_turn = 'O' if self.player_turn == 'X' else 'X'
        return self.player_turn

    def show_board(self):
        print("\n")
        rows = [[self.board[i+j] for i in range(1, 4)] for j in range(0, 7, 3)]
        for row in rows:
            print(row)
        print("\n")

    def start(self):
        while True:
            self.show_board()
            try:
                cell = int(input(f"Player {self.player_turn}, Enter the cell number: "))

                # Check if cell is in the allowed range and is empty
                if cell in range(1, 10) and self.board[cell] == ' ':
                    self.fix_spot(cell, self.player_turn)

                    if self.has_player_won(self.player_turn):
                        print(f"Player {self.player_turn} wins!")
                        break

                    if self.is_board_filled():
                        print("It's a Draw!")
                        break

                    self.swap_player_turn()

                else:
                    print("Invalid input, please try again.")
            except ValueError:
                print("Invalid input, please enter a number between 1 and 9.")


if __name__ == "__main__":
    # Create a game and start it
    game = TicTacToe()
    game.start()