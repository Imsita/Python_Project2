class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # Starting player

    def start_game(self):
        self.board = [' ' for _ in range(9)]  # Reset the board
        self.current_player = 'X'  # Reset to starting player
        print("Game started! Player X goes first.")

    def make_move(self, position):
        if self.is_valid_move(position):
            self.board[position] = self.current_player
            if self.check_winner():
                print(f"Player {self.current_player} wins!")
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'  # Switch player
            return False
        else:
            print("Invalid move. Try again.")
            return False

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]               # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def is_valid_move(self, position):
        return self.board[position] == ' ' and 0 <= position < 9

    def reset_game(self):
        self.start_game()