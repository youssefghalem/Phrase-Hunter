# Import your Game class
from phrasehunter.game import Game
from phrasehunter import phrase

import random

constant_phrases = ("the cat is dead", "howdy", "my name is earl")

if __name__ == "__main__" :
    # Choosing a random phrase
    random_phrase = random.choice(constant_phrases)

    game = Game(phrase.Phrase(random_phrase))
    print(game.phrase)
    print(game.attempts)
    game.input()
    print(game.result())