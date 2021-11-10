
import random

hang = ["""
H A N G M A N - Olympics
   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N - Olympics

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N - Olympics

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N - Olympics

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N - Olympics

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N - Olympics

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N - Olympics

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]
def getRandomWord():
    words = ['judo', 'badminton', 'karate', 'boxing', 'rowing', 'luge', 'basketball', 'soccer',
             'gymnastics', 'fencing', 'weightlifting', 'volleyball', 'handball', 'taekwondo', 'diving', 'curling', 'bobsleigh']

    word = random.choice(words)
    return word


def displayBoard(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)