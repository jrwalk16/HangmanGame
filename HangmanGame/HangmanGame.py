
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

    for i in range(len(secretWord)):  # puts letters in place of blanks
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # shows word with spaces betweeen letters
        print(letter, end=' ')
    print("\n")


def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

        def playAgain():
    return input("\nDo you want to play again? ").lower().startswith('y')


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord()
gameIsDone = False

while True:
    displayBoard(hang, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The secret word is "' +
                  secretWord + '"! You have won!')
            gameIsDone = True