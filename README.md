# Tic Tac Toe Game

This is a simple implementation of the classic Tic Tac Toe game in Python. The game allows two players to take turns marking spaces on a 3x3 grid, with the goal of getting three of their marks in a row (horizontally, vertically, or diagonally).

## Project Structure

```
tic_tac_toe
├── src
│   ├── main.py       # Entry point of the game
│   ├── game.py       # Contains the Game class and game logic
│   └── utils.py      # Utility functions for the game
├── requirements.txt   # List of dependencies
└── README.md          # Project documentation
```

## How to Run the Game

1. Clone the repository or download the project files.
2. Navigate to the project directory in your terminal.
3. (Optional) Create a virtual environment and activate it.
4. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
5. Run the game by executing:
   ```
   python src/main.py
   ```

## Game Rules

- The game is played on a 3x3 grid.
- Players take turns placing their mark (X or O) in an empty cell.
- The first player to get three of their marks in a row wins the game.
- If all cells are filled and no player has three in a row, the game ends in a draw.

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or features you would like to add!