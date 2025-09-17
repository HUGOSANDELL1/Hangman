"""Swedish-themed Hangman with curse words.
"""
from __future__ import annotations

import random
from typing import Iterable, List, Set


HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
    / \  |
        ===
    """,
]

SVENSKA_SVORDOMMAR = [
    "fan",
    "helvete",
    "jävel",
    "skit",
    "skitstövel",
    "rövhål",
    "pucko",
    "idiot",
    "as",
    "slyna",
    "arsle",
]


def choose_word(words: Iterable[str]) -> str:
    """Choose a random word from an iterable."""
    words_list: List[str] = list(words)
    if not words_list:
        raise ValueError("Word list is empty")
    return random.choice(words_list)


def display_state(missed: int, guessed: Set[str], secret_word: str) -> None:
    """Print the current hangman state and the guessed word."""
    print(HANGMAN_PICS[missed])
    display_word = " ".join(letter if letter in guessed else "_" for letter in secret_word)
    print(f"Ord: {display_word}")
    print(f"Gissade bokstäver: {' '.join(sorted(guessed)) if guessed else '-'}")


def get_guess(already_guessed: Set[str]) -> str:
    """Prompt the user for a single letter guess."""
    while True:
        guess = input("Gissa en bokstav: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Skriv EN bokstav tack!")
            continue
        if guess in already_guessed:
            print("Den bokstaven har du redan testat.")
            continue
        return guess


def play_round(secret_word: str) -> bool:
    """Play a single round of Hangman and return True if the player wins."""
    guessed: Set[str] = set()
    missed = 0
    secret_letters = set(secret_word)

    while missed < len(HANGMAN_PICS) - 1:
        display_state(missed, guessed, secret_word)
        guess = get_guess(guessed)
        guessed.add(guess)

        if guess in secret_letters:
            print("Bra där!")
            if secret_letters.issubset(guessed):
                print(f"Du vann! Ordet var '{secret_word}'.")
                return True
        else:
            missed += 1
            print("Nope, fel bokstav.")

    display_state(missed, guessed, secret_word)
    print(f"Du förlorade! Ordet var '{secret_word}'.")
    return False


def play_game() -> None:
    """Start the Hangman game loop."""
    print("Välkommen till Svensk Svordoms-Hangman!")
    wins = 0
    losses = 0

    while True:
        secret_word = choose_word(SVENSKA_SVORDOMMAR)
        if play_round(secret_word):
            wins += 1
        else:
            losses += 1

        print(f"Statistik: {wins} vinster, {losses} förluster")
        again = input("Köra igen? (j/n): ").strip().lower()
        if again != "j":
            print("Tack för att du spelade! Hej då!")
            break


if __name__ == "__main__":
    play_game()
