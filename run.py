import random
from words import words
from colorama import Fore, Back, Style

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
    print(f"{Fore.YELLOW}Lets play Hangman!{Style.RESET_ALL}")
    print(HANGMAN_PICS[stage])
    print('\n')
    print(progress)
    print('\n')

    """
    While user has lost less than 7 lives,
    requests a letter from user & validates input to ensure it is a letter
    checks if the letter is in the word and if it has been guessed already.
    Gives user appropraite feedback.
    Breaks loop when user has correctly guessed all letters
    """
    while stage < 6:
        guess = input('Choose a letter: \n')
        if guess.lower().strip().isalpha() and len(guess) == 1:
            if guess not in word:
                if guess in guessed_letters:
                    print(f'You already guessed {guess}, try again')
                    print('\n')
                else:
                    print(f'{guess} is not in the word, try again')
                    print('\n')
                    stage += 1
                    print(HANGMAN_PICS[stage])
                    print('\n')
                    print(progress)
                    guessed_letters.append(guess)
            elif guess in word and guess in guessed_letters:
                print(f'You already guessed {guess}, try again')
                print('\n')
            elif guess in word:
                print(f'{guess} is in the word!')
                print('\n')
                guessed_letters.append(guess)
                # code for replacing underscores with letters adapted from
                # https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
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
                    print('\n')
                    break
        else:
            print('Invalid input \n')


def play_again():
    """
    Asks user if the want to play again by entering Y or N
    Calls display_hangman function while user wants to play again
    """
    play = input('Would you like to play again? (Y/N) \n')
    if play.upper() == 'Y':
        word = get_random_word(words)
        display_hangman(word)
    elif play.upper() == 'N':
        print('Thanks for playing! \n')
    else:
        print('Invalid choice \n')
        input('Would you like to play again? (Y/N) \n')


word = get_random_word(words)
display_hangman(word)
play_again()
