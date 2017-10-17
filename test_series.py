"""Test file to test fibonacci function, lucas function in series.py file is return the
   correct values
"""
import pytest

FIB_TABLE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (8, 13),
    (9, 21),
    (10, 34)
    ]


LUCAS_TABLE = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 7),
    (6, 11),
    (7, 18),
    (8, 29),
    (9, 47),
    (10, 76)
    ]


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci(n, result):
    """Check number sent into fibonacci function equals correct results"""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    """Check number sent into lucas function equals correct results"""
    from series import lucas
    assert lucas(n) == result
