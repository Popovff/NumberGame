import pytest
from game import check_guess

def test_check_guess():
    secret = 50
    assert check_guess(secret, 30) == "Слишком мало"
    assert check_guess(secret, 70) == "Слишком много"
    assert check_guess(secret, 50) == "Поздравляю! Вы угадали!"