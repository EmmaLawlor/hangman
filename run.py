import random
from words import words

def get_random_word(words):
    word = random.choice(words)
    print(word)

get_random_word(words)
