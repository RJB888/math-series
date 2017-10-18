"""Test file to test fibonacci function, lucas function, and sum_series
   function  in series.py file.
"""
import pytest

FIB_TABLE = [
    (1, 0),
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
    (1, 2),
    (2, 1),
    (3, 3),
    (4, 4),
    (5, 7),
    (6, 11),
    (7, 18),
    (8, 29),
    (9, 47),
    (10, 76)
    ]

SERIES_TABLE = [
    (0, 0, 0, 0),
    (1, 4, 4, 15),
    (4, 262, 42, 110),
    (10, 490, 12, 7),
    (10, 144, 2, 3)
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


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_sum_series_for_fibonnaci(n, result):
    """Test sum_series function works when passed only 1 parameter"""
    from series import sum_series
    assert sum_series(n) == result


@pytest.mark.parametrize('n, result, pos1, pos2', SERIES_TABLE)
def test_series(n, result, pos1, pos2):
    """Check number sent into lucas function equals correct results"""
    from series import sum_series
    assert sum_series(n, pos1, pos2) == result
