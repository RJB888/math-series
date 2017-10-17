"""Test file to test fibonacci function in series.py file is return the
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


@pytest.mark.parametrize('n, result', FIB_TABLE)
def test_fibonacci(n, result):
    """Check number sent into fibonacci function equals correct results"""
    from series import fibonacci
    assert fibonacci(n) == result

