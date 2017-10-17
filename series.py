"""Implements Fibonacci sequence and Lucas Numbers."""

"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""

# Fib
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# Lucas
# 2, 1, 3, 4, 7, 11, 18, 29, ...


def fib_series(n):
    """Calculate the fiboacci sequence given the nth place to calculate to."""
    if n == 0 or n == 1:
        return n
    # num = 0
    series = [0, 1]
    for i in range(2, n):
        series.append(series[i - 1] + series[i - 2])
    return series[-1]
