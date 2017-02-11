import random
import string


class Game:
    """Bulls and Cows game"""

    def __init__(self, input_func, number_size):
        self._input_func = input_func
        self._number_size = number_size
        self._secret_number = ''.join(random.sample(string.digits, number_size))
        self._guesses = 0

    def play(self):
        print("Hi there!")
        print("I've generated a random {} digit number for you.".format(self._number_size))
        print("Let's play a bulls and cows game.")
        self.ask_and_evaluate_answers()
        self.print_results()

    def ask_and_evaluate_answers(self):
        while True:
            try:
                self._guesses += 1
                number = self.get_guess()
                if number == self._secret_number:
                    break       # correct guess, stop asking
                else:
                    count = BullsCowsCount(self._secret_number, number)
                    print("{}, {}".format(count.bulls(), count.cows()))
            except WrongInputException as e:
                print(e)
                continue        # go and ask again

    def get_guess(self):
        print('Enter a number')
        input_ = self._input_func().strip()
        if not input_.isdecimal() or len(set(input_)) != self._number_size:
            raise WrongInputException('Wrong input. Input must be {} different digits.'.format(self._number_size))
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
        for i in range(len(secret)):
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
    Game(input, 4).play()
