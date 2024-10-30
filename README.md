Word Guessing Game

A simple command-line word guessing game where the player tries to guess a randomly chosen word within a limited number of attempts. Each incorrect guess reduces the player's attempts, while correct guesses reveal the letters in the hidden word. This project demonstrates basic Python concepts such as loops, conditionals, functions, and string manipulation.


How It Works

The program randomly selects a word from a predefined list.
The chosen word is then hidden behind dashes (-) equal to the word's length.
The player is prompted to guess one letter at a time.
If the guessed letter is in the word, it appears in the correct position(s).
If the guessed letter is not in the word, the player's remaining attempts (guesses_left) are reduced by one.
The game continues until the player either:
Reveals the entire word (win), or
Runs out of attempts (lose).


Files

main.py – The main game file that contains all the game logic.


How to Run

Clone this repository to your local machine.
Open a terminal and navigate to the project directory.
Run the code using Python
