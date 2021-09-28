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

class Hangman:
    def __init__(self):
        self.word = random.choice(words)
        self.stage = 0
        self.guessed_letters = []
        self.progress = '-' * len(self.word)
        self.games_played = 0
        self.games_won = 0

    def display_hangman(self):
        print(Fore.CYAN + HANGMAN_PICS[self.stage])
        print('\n')
        print(self.progress + Style.RESET_ALL)
        print('\n')

    def play_hangman(self):
        """
        While user has lost less than 7 lives,
        requests a letter from user & validates input to ensure it is a letter
        checks if the letter is in the word and if it has been guessed already.
        Gives user appropraite feedback.
        Breaks loop when user has correctly guessed all letters
        """
        while self.stage < 6:
            self.display_hangman()
            guess = input(f'{Fore.YELLOW}Choose a letter: {Style.RESET_ALL}').lower().strip()
            print('\n')
            if guess.isalpha() and len(guess) == 1:
                if guess not in self.word:
                    if guess in self.guessed_letters:
                        print(f'You already guessed {guess}, try again')
                        print('\n')
                    else:
                        print(f'{Fore.RED}{guess} is not in the word, try again{Style.RESET_ALL}')
                        print('\n')
                        self.stage += 1
                        self.guessed_letters.append(guess)
                elif guess.isalpha() and guess in self.word:
                    print(f'{Fore.GREEN}{guess} is in the word!{Style.RESET_ALL}')
                    print('\n')
                    self.guessed_letters.append(guess)
                    # code for replacing underscores with letters adapted from
                    # https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
                    word_as_list = list(self.progress)
                    indices = [i for i, letter in enumerate(self.word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                        self.progress = "".join(word_as_list)
                    if "_" not in self.progress:
                        print(f'{Fore.GREEN}Congrats! You correctly guessed the answer: {self.word}{Style.RESET_ALL}')
                        print('\n')
                        self.games_won += 1
                        break

            elif guess.isalpha() and guess == self.word:
                print(f'{Fore.GREEN}Congrats! You correctly guessed the answer: {self.word}{Style.RESET_ALL}')
                print('\n')
                self.games_won += 1
                break

            elif guess.isalpha() and guess not in self.word and guess in self.guessed_words:
                print(f'You already guessed {guess}, try again')
                print('\n')

            elif guess.isalpha() and guess not in self.word and guess not in self.guessed_words:
                print(f'{Fore.RED}{guess} is not the word, try again{Style.RESET_ALL}')
                print('\n')
                self.stage += 1
                self.guessed_words.append(guess)
                print('\n')
            else:
                print('Invalid input \n')
        if self.stage >= 6:
            print(f'{Fore.RED}Game Over! The word was {self.word}{Style.RESET_ALL}')
            print('\n')
        self.play_again()

    def play_again(self):
        """
        Asks user if the want to play again by entering Y or N
        Calls display_hangman function while user wants to play again
        """
        play = input(f'{Fore.YELLOW}Would you like to play again? (Y/N)').strip().upper()
        print('\n')
        if play == 'Y':
            self.stage = 0
            self.guessed_letters = []
            self.guessed_words = []
            self.word = random.choice(words)
            self.progress = '_' * len(self.word)
            self.games_played += 1
            self.play()
        elif play == 'N':
            print('Thanks for playing! \n')
            print(f'You won {self.games_won} out of {self.games_played} games')
        else:
            print('Invalid choice \n')
            self.play_again()


def main():
    """
    Run hangman game functions
    """
    game = Hangman()
    game.play_hangman()

print(f"{Fore.YELLOW}Lets play Hangman!{Style.RESET_ALL}")
main()
