# Import your Game class
from phrasehunter.game import Game
from phrasehunter import phrase
from pathlib import Path
import random

data_folder = Path("phrasehunter/")
file_to_open = data_folder / "phrasebank.txt"

with open(file_to_open) as file_in:
    lines = []
    for line in file_in:
        lines.append(line.strip())


# constant_phrases = ("the cat is dead", "howdy", "my name is earl", "I am feeling go sick", "abracadabra")
# import phrases from file text ;)



if __name__ == "__main__" :

    play = "y"

    # Choosing a random phrase
    while play == "y":
        random_phrase = random.choice(lines)

        game = Game(phrase.Phrase(random_phrase))
        print(game.phrase)
        print(game.attempts)

        game.input()


        if game.result() :
            print("Bravo ! You guessed the right word")
        else :
            print(f"You lost ! the answer was {game.phrase.phrase}")

        play = "z"

        while play not in ["y","n"] :
            play = input("Do you want to play again? (Y/N)").lower()


