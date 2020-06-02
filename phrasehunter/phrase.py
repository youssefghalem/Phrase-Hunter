# Create your Phrase class logic here.
from phrasehunter.character import Character

class Phrase() :
    def __init__(self, phrase):
        self.phrase = phrase
        self.list_of_char = [Character(letter) for letter in phrase]

#prints the current state of sentence until it becomes plain
    def __str__(self):
        result = ""
        for char in self.list_of_char :
            result = result + char
        return result


    def correct_answer(self):
        return not False in [char.was_guessed == True for char in self.list_of_char]


    def __iter__(self):
        yield from self.list_of_char

    def was_guessed(self, character):
        for car in self.list_of_char :
            if car == character :
                car.character_guessed()

    def string_guessed(self, string):
        for car in self.list_of_char :
            if car == string :
                return car.was_guessed




