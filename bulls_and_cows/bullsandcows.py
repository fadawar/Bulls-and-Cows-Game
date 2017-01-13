from random import randint


class Game:
    """Bulls and Cows game"""

    def __init__(self, input_func):
        self.input_func = input_func
        self._secret_number = randint(1000, 9999)

    def start(self):
        print("Hi there!\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.\nEnter a "
              "number")
        guesses = self._get_and_check_answers()
        print("Correct, you've guessed the right number in {} guesses!\nThat's amazing, average, not so good, ...".format(guesses))

    def _get_and_check_answers(self):
        guesses = 0
        while True:
            guesses += 1
            guess = int(self.input_func())
            if guess == self._secret_number:
                break
            else:
                print("{} bulls, {} cows".format(self._bulls_in(guess), self._cows_in(guess)))
        return guesses

    def _bulls_in(self, number):
        bulls = 0
        for l, r in zip(str(self._secret_number), str(number)):
            if l == r:
                bulls += 1
        return bulls

    def _cows_in(self, number):
        cows = 0
        for l, r in zip(str(self._secret_number), str(number)):
            if l != r and r in str(self._secret_number):
                cows += 1
        return cows


if __name__ == '__main__':
    Game(input).start()
