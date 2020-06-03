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

            if a not in string.ascii_lowercase :
                print("please type one alphabetic character")
                continue

            elif  self.phrase.string_guessed(a) == True :
                print("this character has been guessed, try a new one")
                continue

            self.phrase.was_guessed(a)

            #if the player makes a mistake, attempts are decreased
            if not self.phrase.string_guessed(a) :
                self.attempts -= 1
                print(f"you still have {self.attempts} lives out of 5" )

            print(self.phrase)


    def result(self):
        return self.phrase.correct_answer() and self.attempts > 0


