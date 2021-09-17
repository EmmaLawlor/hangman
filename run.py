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
    progress = '_' * len(word)
    print("Let's play Hangman!\n")
    print(HANGMAN_PICS[stage])
    print('\n')
    print(progress)
    print('\n')
    while stage < 7:
        guess = input('Choose a letter: \n')
        if guess.lower().strip().isalpha():
            if guess not in word:
                print(f'{guess} is not in the word, try again')
                stage += 1
                print(HANGMAN_PICS[stage])
                print('\n')
                print(progress)
                guessed_letters.append(guess)
            elif guess in guessed_letters:
                print(f'You already guessed {guess}, try again')
            else: 
                print(f'{guess} is in the word!')
                guessed_letters.append(guess)
                word_as_list = list(progress)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    progress = "".join(word_as_list)
                    print(HANGMAN_PICS[stage])
                    print('\n')
                    print(progress)
                if "_" not in progress:
                    print(f'Congrats! You correctly guessed the answer: {word}')
                    break
        else: print('Invalid input')


word = get_random_word(words)
display_hangman(word)

