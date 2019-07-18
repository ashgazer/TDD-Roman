import pytest
from noman import *

roman2 = roman()


@pytest.fixture
def smtp_connection():
    x = roman()
    return x


def test_call_roman():
    assert roman2


def test_call_roman_cal_with_I():
    expected = 1
    result = roman2.cal('I')

    assert result == expected


def test_call_roman_cal_with_V():
    expected = 5
    result = roman2.cal('V')

    assert result == expected


def test_call_roman_cal_with_X():
    expected = 10
    result = roman2.cal('X')

    assert result == expected, "expect 10 here"


def test_number_1_to_roman():
    expected = "I"
    result = roman2.num_2_rom(1)

    assert result == expected


def test_number_5_to_roman():
    expected = "V"
    result = roman2.num_2_rom(5)

    assert result == expected


def test_number_10_to_roman():
    expected = "X"
    result = roman2.num_2_rom(10)

    assert result == expected


def test_number_30_to_roman(smtp_connection):
    expected = "XXX"
    result = smtp_connection.num_2_rom(30)

    assert result == expected


@pytest.mark.parametrize('input, expected', [
    (30, "XXX"), (10, 'X'), (2, 'II')
    ,(15, 'XV'),(4,"IV"), (14, "XIV")
    ,(55,"LV"),(54,"LIV"), (70,"LXX")

])
def test_number_2_roman(input, expected):
    result = roman2.num_2_rom(input)

    assert result == expected


