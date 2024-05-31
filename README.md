# Game Introduction:
__Wordle__ is a popular daily word game where players guess a secret five-letter word. This Python implementation of

Wordle allows you to play the game locally on your computer. The game color-codes each letter in the guess,

indicating whether it is in the correct position (green), in the word but not in the correct position (yellow), or

not in the word at all (red)

## Rules
- The game uses a secret five-letter word that changes daily.
- Players can guess the word by entering a five-letter word.
- Players has 6 tries to guess the word.
- At the end of the 6 attempts, if the player fails to guess the right word, the word is revealed.
- Player can enter __q__ to quit the game.

## TODO
- The player enters a random 5-letter word.
- If the random word is the word to be guessed, the game is over. The player receives a congratulations message.
- Based on this, the player has 6 tries to guess the word.
- At the end of the 6 attempts, if the player fails to guess the right word, the word is revealed.

## How to Run

- Clone the repository and `cd` into it.
- Install the requirements by running `pip install -r requirements.txt`.
- In your terminal, run `export PYTHONPATH=$PYTHONPATH:$(pwd)` to add the current directory to your `PYTHONPATH`.
- Run `python src/run.py` in your Terminal to start the game.