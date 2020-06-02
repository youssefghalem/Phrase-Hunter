from phrasehunter.character import Character
import string
# we imported the string module to be able to use string.ascii_lowercase


class Game():
    def __init__(self, phrase):
        self.phrase = phrase
        self.attempts = 5

    def input(self):
        while self.attempts > 0 and not self.result() :


            a = input("Please type a character : ").lower()

            # we make sure not to count previous correct answers
            while self.phrase.string_guessed(a) == True or a not in string.ascii_lowercase :
                a = input("Please type a character : ")

            self.phrase.was_guessed(a)

            #if the player makes a mistake, attempts are decreased
            if not self.phrase.string_guessed(a) :
                self.attempts -= 1

            print(self.phrase)
            print(self.attempts)

    def result(self):
        return self.phrase.correct_answer() and self.attempts > 0


