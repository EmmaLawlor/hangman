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
    guessed_letters = []
    print("Let's play Hangman!\n")
    print(HANGMAN_PICS[stage])
    print('\n')
    print('    ','_' * len(word))
    print('\n')
    while stage < 7:
        guess = input('Choose a letter: \n')
        if guess.lower().strip().isalpha():
            if guess not in word:
                print(f'{guess} is not in the word, try again')
                stage += 1
                guessed_letters.append(guess)
            elif guess in guessed_letters:
                print(f'You already guessed {guess}, try again')
            else: print(f'{guess} is in the word!')
        else: print('Invalid input')


word = get_random_word(words)
display_hangman(word)

