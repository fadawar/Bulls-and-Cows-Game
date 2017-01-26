from random import shuffle


class Game:
    """Bulls and Cows game"""
    def __init__(self, input_func):
        self._input_func = input_func
        self._secret_number = self.generate_secret_number()

    def generate_secret_number(self):
        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        shuffle(digits)
        num = ''.join(digits[:4])
        return int(num)

    def start(self):
        print("Hi there!\n"
              "I've generated a random 4 digit number for you.\n"
              "Let's play a bulls and cows game.\n")
        guesses = self.get_and_check_answers()
        print("Correct, you've guessed the right number in {} guesses!\nThat's amazing...".format(guesses))

    def get_and_check_answers(self):
        attempts = 0
        while True:
            print("Enter a number")
            attempts += 1
            guess = int(self._input_func())
            if not self.number_is_correct(guess):
                continue
            if guess == self._secret_number:
                break
            else:
                print("{}, {}".format(Bulls(self._secret_number, guess), Cows(self._secret_number, guess)))
        return attempts

    def number_is_correct(self, number):
        s = set(str(number))
        if len(s) == 4:
            return True
        return False


class Bulls:
    """Count bulls between two numbers"""
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
    """Count cows between two numbers"""
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
