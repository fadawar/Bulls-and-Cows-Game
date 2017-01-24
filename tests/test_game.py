from bulls_and_cows.bullsandcows import Game, Bulls, Cows


def test_game_has_secret_number():
    g = Game(lambda x: 0)
    assert g._secret_number is not None


def test_secret_number_has_4_digits():
    g = Game(lambda x: 0)
    assert len(str(g._secret_number)) == 4


def test_secret_numbers_digits_are_different():
    g = Game(lambda x: 0)
    s = set(str(g._secret_number))
    assert len(s) == 4


def test_ask_until_correct_answer():
    input_generator = (i for i in ['2016', '2017'])
    g = Game(lambda: next(input_generator))
    g._secret_number = 2017
    guesses = g.get_and_check_answers()
    assert guesses == 2


def test_count_of_bulls():
    assert int(Bulls(1234, 1234)) == 4
    assert int(Bulls(1234, 1200)) == 2


def test_count_of_cows():
    assert int(Cows(1234, 1234)) == 0
    assert int(Cows(1234, 1020)) == 1
    assert int(Cows(1234, 4321)) == 4
    assert int(Cows(1234, 1111)) == 3
