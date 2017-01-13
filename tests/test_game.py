from bulls_and_cows.bullsandcows import Game


def test_game_has_secret_number():
    g = Game(lambda x: 0)
    assert g._secret_number is not None


def test_secret_number_has_4_digits():
    g = Game(lambda x: 0)
    assert len(str(g._secret_number)) == 4


def test_ask_until_correct_answer():
    input_generator = (i for i in ['2016', '2017'])
    g = Game(lambda: next(input_generator))
    g._secret_number = 2017
    guesses = g._get_and_check_answers()
    assert guesses == 2


def test_number_of_bulls():
    g = Game(lambda: 0)
    g._secret_number = 1234
    assert g._bulls_in(1234) == 4
    assert g._bulls_in(1200) == 2

def test_number_of_cows():
    g = Game(lambda: 0)
    g._secret_number = 1234
    assert g._cows_in(1234) == 0
    assert g._cows_in(1020) == 1
    assert g._cows_in(4321) == 4
    assert g._cows_in(1111) == 3


if __name__ == '__main__':
    import pytest
    pytest.main()
