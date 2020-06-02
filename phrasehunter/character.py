# Create your Character class logic in here.
class Character():
    def __init__(self, original):
        self.original = original

        if self.original == " ":
            self.was_guessed = True
        else :
            self.was_guessed = False


    def character_guessed(self):
        self.was_guessed = True

    def __str__(self):
        if self.was_guessed:
            return self.original
        elif self.original == " " :
            return " "
        else:
            return "_"

    def __repr__(self):
        return self.original


    def __eq__(self, other):
        if isinstance(other, Character) :
            return self.original == other.original
        elif isinstance(other, str) :
            return self.original == other

    def __add__(self, other):
        if isinstance(other, Character) :
            return str(self) + str(other)
        elif isinstance(other, str) :
            return str(self) + other

    def __radd__(self, other):
        if isinstance(other, Character) :
            return other.original + str(self)
        elif isinstance(other, str) :
            return other + str(self)



