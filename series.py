"""Implements Fibonacci sequence and Lucas Numbers."""

"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""

# Fib
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# Lucas
# 2, 1, 3, 4, 7, 11, 18, 29, ...


def fibonacci(n):
    """Calculate the fiboacci sequence given the nth place to calculate to."""
    if n == 0 or n == 1:
        return n
    # num = 0
    series = [0, 1]
    for i in range(2, n):
        series.append(series[i - 1] + series[i - 2])
    return series[-1]


def lucas(n):
    """Return the nth number in Lucas Numbes."""
    if n == 2 or n == 1:
        return n
    # num = 0
    series = [2, 1]
    for i in range(2, n):
        series.append(series[i - 1] + series[i - 2])
    return series[-1]


def sum_series(n, start1=0, start2=1):
    """Run series function based on optional parameters given."""
    if start1 == 0:
        fibonacci(n)
    elif start1 == 2:
        lucas(n)


# sum_series with one required parameter and two optional parameters.
# The required parameter will determine which element in the series to print.
# The two optional parameters will have default values of 0 and 1 and will
# determine the first two values for the series to be produced.
