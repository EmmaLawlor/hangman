import random
from words import words

HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
         |
        ===''', '''
     +---+
     O   |
    /|\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\  |
    / \  |
        ===''']

def get_random_word(words):
    """
    Selects random word from word list and returns the word in loswercase
    """
    word = random.choice(words)
    return word

def display_hangman(word):
    """
    Initialises game by displaying welcome message to user,
    Displays first stage of hangman image and an
    underscore for each missing letter of the random word chosen from list
    """
    stage = 0
    print("Let's play Hangman!\n")
    print(HANGMAN_PICS[stage])
    print('\n')
    print('    ','_' * len(word))


word = get_random_word(words)
display_hangman(word)

