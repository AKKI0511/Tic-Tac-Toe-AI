# Tic Tac Toe AI Player

## Overview
This repository contains a Tic Tac Toe game implemented in Python, featuring an AI opponent using the minimax algorithm. The project provides both a command-line version (`tictactoe.py`) and a graphical version with a user interface created using Pygame (`runner.py`).

## Features

1. **Player Management:**
   - The game supports two players, X and O, with the computer acting as the AI opponent.

2. **Game Board Representation:**
   - The board is represented as a 3x3 grid, and each cell can be in one of three states: X, O, or empty.

3. **Gameplay Logic:**
   - Players take turns making moves.
   - The AI opponent uses the minimax algorithm to make strategic moves based on the current state of the board.

4. **Winning Conditions:**
   - The game identifies the winner by checking rows, columns, and diagonals for matching symbols.
   - If the board is filled without a winner, the game is declared a draw.

5. **Graphical User Interface (GUI):**
   - The Pygame-based GUI (`runner.py`) provides an interactive environment for playing the Tic Tac Toe game.

## `tictactoe.py` Technical Details

### Functions

1. **`initial_state()`**
   - Returns the starting state of the Tic Tac Toe board.

2. **`player(board)`**
   - Determines the player (X or O) with the next turn.

3. **`actions(board)`**
   - Returns a set of all possible actions (i, j) available on the board.

4. **`result(board, action)`**
   - Generates the resulting board after a player makes a valid move.

5. **`winner(board)`**
   - Determines the winner of the game or returns None if there is no winner.

6. **`terminal(board)`**
   - Returns True if the game is over (either a player wins or the board is filled), otherwise False.

7. **`utility(board)`**
   - Returns the utility value for the current state of the board (-1, 0, 1).

8. **`minimax(board)`**
   - Implements the minimax algorithm to find the optimal move for the current player.

### How to Run
To experience the Tic Tac Toe game (`tictactoe.py`), follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the Python script: `python tictactoe.py`.

### Future Enhancements
Consider exploring the following enhancements for future development:
- Implement a graphical user interface (GUI) for a more interactive gaming experience.
- Add difficulty levels to adjust the AI's strategy for different skill levels.

## `runner.py` Technical Details

### How to Run
To play the Tic Tac Toe game with the graphical interface (`runner.py`), follow these steps:
1. Ensure you have Python and Pygame installed on your machine.
2. Clone the repository to your local machine.
3. Open a terminal and navigate to the project directory.
4. Run the Pygame script: `python runner.py`.

### Gameplay
- **Player Selection:**
  - At the start, the game prompts the user to choose between playing as "X" or "O."
  - Click the respective buttons on the GUI to make your selection.

- **Game Board:**
  - The Tic Tac Toe board is displayed on the GUI.
  - Users can make moves by clicking on an empty cell.
  - The AI opponent uses the minimax algorithm to make strategic moves.

- **Game Over:**
  - When the game is over (either a player wins or the board is filled), the result is displayed.
  - Users can choose to play again by clicking the "Play Again" button.

### Dependencies
- **Pygame Library:**
  - The Pygame library is utilized for creating the graphical interface and handling user input.

### Future Enhancements
Consider exploring the following enhancements for future development:
- Implement additional GUI improvements, such as animations and smoother transitions.
- Allow users to choose difficulty levels for the AI opponent.
- Incorporate sound effects or visual cues to enhance the gaming experience.

Feel free to contribute, report issues, or provide feedback to enhance the Tic Tac Toe AI game with a graphical interface!
