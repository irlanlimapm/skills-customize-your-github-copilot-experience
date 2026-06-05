"""Starter code for the Hangman game assignment.

This file follows the project's starter-code pattern: small, well-named
functions that students can implement or extend. A minimal, runnable
version is provided so educators can choose whether to give a skeleton
or a working example.
"""

import random
from typing import List, Set, Tuple

# Public configuration
WORDS: List[str] = ["python", "hangman", "challenge", "programming", "computer"]
MAX_INCORRECT = 6


def select_word(words: List[str]) -> str:
	"""Return a randomly selected word from `words`."""
	return random.choice(words)


def initialize_game(secret_word: str, max_incorrect: int = MAX_INCORRECT) -> Tuple[Set[str], Set[str], int]:
	"""Initialize and return (guessed_letters, incorrect_guesses, max_incorrect).

	- `guessed_letters`: letters correctly guessed so far
	- `incorrect_guesses`: letters guessed that are not in the word
	- `max_incorrect`: allowed incorrect guesses
	"""
	guessed_letters: Set[str] = set()
	incorrect_guesses: Set[str] = set()
	return guessed_letters, incorrect_guesses, max_incorrect


def display_progress(secret_word: str, guessed_letters: Set[str]) -> str:
	"""Return the current progress string for the secret word.

	Example: for secret "python" and guessed {'p','h'}, returns "p _ _ h _ _".
	"""
	return " ".join([c if c in guessed_letters else "_" for c in secret_word])


def is_word_guessed(secret_word: str, guessed_letters: Set[str]) -> bool:
	"""Return True if all letters in the secret word have been guessed."""
	return set(secret_word).issubset(guessed_letters)


def update_state(guess: str, secret_word: str, guessed_letters: Set[str], incorrect_guesses: Set[str]) -> bool:
	"""Update game state with `guess` and return True if guess was correct.

	- Ignores invalid input (non-alpha or multi-char) and repeated guesses.
	- Adds the guess to `guessed_letters` if correct, otherwise to `incorrect_guesses`.
	"""
	guess = guess.lower()
	if len(guess) != 1 or not guess.isalpha():
		return False
	if guess in guessed_letters or guess in incorrect_guesses:
		return False
	if guess in secret_word:
		guessed_letters.add(guess)
		return True
	else:
		incorrect_guesses.add(guess)
		return False


def play_game(words: List[str] = WORDS, max_incorrect: int = MAX_INCORRECT) -> None:
	"""Run a simple command-line Hangman game.

	Students can use this function as a reference implementation or
	replace its internals with their own versions as part of the task.
	"""
	secret_word = select_word(words)
	guessed_letters, incorrect_guesses, max_incorrect = initialize_game(secret_word, max_incorrect)

	while not is_word_guessed(secret_word, guessed_letters) and len(incorrect_guesses) < max_incorrect:
		print("\nWord:", display_progress(secret_word, guessed_letters))
		print(f"Incorrect guesses: {', '.join(sorted(incorrect_guesses))} ({len(incorrect_guesses)}/{max_incorrect})")
		guess = input("Enter a single letter: ").strip().lower()
		if not guess:
			print("Please enter a letter.")
			continue
		update_state(guess, secret_word, guessed_letters, incorrect_guesses)

	print()
	if is_word_guessed(secret_word, guessed_letters):
		print("Congratulations — you guessed the word:", secret_word)
	else:
		print("Out of attempts. The word was:", secret_word)


if __name__ == "__main__":
	play_game()

