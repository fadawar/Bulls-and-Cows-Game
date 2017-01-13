from random import randint


class Game:
    """Bulls and Cows game"""

    def __init__(self, input_func):
        self._input_func = input_func
        self._secret_number = randint(1000, 9999)

    def start(self):
        print("Hi there!\n"
              "I've generated a random 4 digit number for you.\n"
              "Let's play a bulls and cows game.\n"
              "Enter a number")
        guesses = self.get_and_check_answers()
        print("Correct, you've guessed the right number in {} guesses!\nThat's amazing...".format(guesses))

    def get_and_check_answers(self):
        attempts = 0
        while True:
            attempts += 1
            guess = int(self._input_func())
            if guess == self._secret_number:
                break
            else:
                print("{}, {}".format(Bulls(self._secret_number, guess), Cows(self._secret_number, guess)))
        return attempts


class Bulls:
    def __init__(self, secret, guess):
        self.secret = secret
        self.guess = guess

    def __int__(self):
        bulls = 0
        for sec_digit, guess_digit in zip(str(self.secret), str(self.guess)):
            if sec_digit == guess_digit:
                bulls += 1
        return bulls

    def __str__(self):
        value = int(self)
        if value == 1:
            return "{} bull".format(value)
        return "{} bulls".format(value)


class Cows:
    def __init__(self, secret, guess):
        self.secret = secret
        self.guess = guess

    def __int__(self):
        cows = 0
        for sec_digit, guess_digit in zip(str(self.secret), str(self.guess)):
            if sec_digit != guess_digit and guess_digit in str(self.secret):
                cows += 1
        return cows

    def __str__(self):
        value = int(self)
        if value == 1:
            return "{} cow".format(value)
        return "{} cows".format(value)


if __name__ == '__main__':
    Game(input).start()
