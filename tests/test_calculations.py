import pytest
from my_repo.calculations import addition


def test_check_adding_two_numbers():
    assert addition(1, 2) == 3


def test_check_error_adding_two_numbers():
    assert not addition(1, 1) == 1
