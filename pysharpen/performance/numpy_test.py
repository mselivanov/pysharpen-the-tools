"""
Module for demonstrating numpy based performance
optimization.
"""
from timeit import timeit
import numpy as np


VEC = list(range(1000000))


def vmul(v1, v2):
    return [el1*el2 for el1, el2 in zip(v1, v2)]


def vmul_numpy(v1, v2):
    return np.array(v1) * np.array(v2)


def test_numpy():
    print("python mul: ",
          timeit("vmul(VEC, VEC)",
                 "from __main__ import vmul, VEC",
                 number=10))
    print("numpy mul: ",
          timeit("numpy.array(list(range(1000000)))*"
                 "numpy.array(list(range(1000000)))",
                 "import numpy",
                 number=10))


def main():
    test_numpy()


if __name__ == "__main__":
    main()
