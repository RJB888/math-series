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
    series = [0, 1]
    if n < 2:
        return series[n - 1]
    # num = 0
    for i in range(2, n):
        series.append(series[i - 1] + series[i - 2])
    return series[-1]


def lucas(n):
    """Return the nth number in Lucas Numbes."""
    series = [2, 1]
    if n < 2:
        return series[n - 1]
    # num = 0
    for i in range(2, n):
        series.append(series[i - 1] + series[i - 2])
    return series[-1]


def sum_series(n, start1=0, start2=1):
    """Run series function based on optional parameters given."""
    series = [start1, start2]
    if n < 2:
        return series[n - 1]
    for i in range(2, n):
        series.append(series[i - 1] + series[i - 2])
    return series[-1]


if __name__ == "__main__":
    print("This module defines functions that implement mathematical series.")
    print("\nfibonacci(n): Returns the nth value in the fibonacci series.")
    print("fibonacci(5): ", fibonacci(5))
    print("\nlucas(n): Returns the nth value in the Lucas Numbers.")
    print('lucas(5): ', lucas(5))
    print("\nsum_series(n): Returns the nth value in a random series based on\
the fibonacci calculations, and can take params for the initial 2 numbers.")
    print("sum_series(5,10,2): ", sum_series(5, 10, 2))
