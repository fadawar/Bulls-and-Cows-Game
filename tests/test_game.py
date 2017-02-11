import pytest
from bulls_and_cows.bullsandcows import Game, BullsCowsCount, WrongInputException


def test_game_has_secret_number():
    g = Game(lambda: 0)
    assert g._secret_number is not None
    assert type(g._secret_number) is str


def test_secret_number_has_4_digits():
    g = Game(lambda: 0)
    assert len(g._secret_number) == 4


def test_secret_numbers_digits_are_different():
    g = Game(lambda: 0)
    s = set(g._secret_number)
    assert len(s) == 4


def test_ask_until_correct_answer():
    input_generator = (i for i in ['2016', '2017'])
    g = Game(lambda: next(input_generator))
    g._secret_number = '2017'
    g.get_and_check_answers()
    assert g._guesses == 2


def test_count_of_bulls():
    assert BullsCowsCount('1234', '1234').bulls() == '4 bulls'
    assert BullsCowsCount('1234', '1289').bulls() == '2 bulls'
    assert BullsCowsCount('1234', '1987').bulls() == '1 bull'


def test_count_of_cows():
    assert BullsCowsCount('1234', '1234').cows() == '0 cows'
    assert BullsCowsCount('1234', '1487').cows() == '1 cow'
    assert BullsCowsCount('1234', '4321').cows() == '4 cows'
    assert BullsCowsCount('1234', '3419').cows() == '3 cows'


def test_ask_for_number_returns_input():
    g = Game(lambda: '1234')
    assert g.ask_for_number() == '1234'


def test_ask_for_number_checks_input():
    g1 = Game(lambda: '12')                                     # too short
    with pytest.raises(WrongInputException) as exc_info:
        g1.ask_for_number()
        assert str(exc_info.value) == 'Wrong input. Input must be 4 different digits.'

    g2 = Game(lambda: '123456')                                 # too long
    with pytest.raises(WrongInputException) as exc_info:
        g2.ask_for_number()
        assert str(exc_info.value) == 'Wrong input. Input must be 4 different digits.'

    g3 = Game(lambda: '12ab')                                   # not a number
    with pytest.raises(WrongInputException) as exc_info:
        g3.ask_for_number()
        assert str(exc_info.value) == 'Wrong input. Input must be 4 different digits.'

    g4 = Game(lambda: '1223')                                   # same digits
    with pytest.raises(WrongInputException) as exc_info:
        g4.ask_for_number()
        assert str(exc_info.value) == 'Wrong input. Input must be 4 different digits.'
