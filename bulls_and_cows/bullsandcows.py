import random
import string


class Game:
    """Bulls and Cows game"""

    def __init__(self, input_func):
        self._input_func = input_func
        self._secret_number = ''.join(random.sample(string.digits, 4))
        self._guesses = 0

    def play(self):
        print("Hi there!")
        print("I've generated a random 4 digit number for you.")
        print("Let's play a bulls and cows game.")
        self.get_and_check_answers()
        self.print_results()

    def get_and_check_answers(self):
        while True:
            try:
                self._guesses += 1
                number = self.ask_for_number()
                if number == self._secret_number:
                    break       # correct guess, stop asking
                else:
                    count = BullsCowsCount(self._secret_number, number)
                    print("{}, {}".format(count.bulls(), count.cows()))
            except WrongInputException as e:
                print(e)
                continue        # go and ask again

    def ask_for_number(self):
        print('Enter a number')
        input_ = self._input_func().strip()
        if not input_.isdecimal() or len(set(input_)) != 4:
            raise WrongInputException('Wrong input. Input must be 4 different digits.')
        return input_

    def print_results(self):
        print("Correct, you've guessed the right number in {} guesses!".format(self._guesses))
        if self._guesses <= 5:
            print("That's amazing!")
        elif self._guesses <= 10:
            print("That's average.")
        else:
            print("That's not so good.")


class BullsCowsCount:
    """Count bulls and cows between two numbers"""

    def __init__(self, secret, guess):
        self._bulls = self._cows = 0
        self._count(secret, guess)

    def _count(self, secret, guess):
        for i in range(4):
            if secret[i] == guess[i]:
                self._bulls += 1
            elif guess[i] in secret:
                self._cows += 1

    def bulls(self):
        if self._bulls == 1:
            return "{} bull".format(self._bulls)
        return "{} bulls".format(self._bulls)

    def cows(self):
        if self._cows == 1:
            return "{} cow".format(self._cows)
        return "{} cows".format(self._cows)


class WrongInputException(Exception):
    pass


if __name__ == '__main__':
    Game(input).play()
