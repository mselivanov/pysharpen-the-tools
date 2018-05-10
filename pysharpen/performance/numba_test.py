"""
Module for demonstrating numba performance
optimizations.
"""
import numba
from timeit import timeit


coefs = [4, 8, 15, 16, 23, 42]


def poly(coefs, n):
    total = 0
    for i, c in enumerate(coefs):
        total += c * n**i
    return total


@numba.jit
def poly_jit(coefs, n):
    total = 0
    for i, c in enumerate(coefs):
        total += c * n**i
    return total


def test_jit():
    print("No jit",
          timeit("poly(coefs, 7)",
                 "from __main__ import poly, coefs",
                 number=1000000))
    print("Jit",
          timeit("poly_jit(coefs, 7)",
                 "from __main__ import poly_jit, coefs",
                 number=1000000))


def main():
    test_jit()


if __name__ == "__main__":
    main()
