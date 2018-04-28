"""
Different tricks for optimizing performance
"""
import timeit
from memory_profiler import memory_usage
# import dis

# Name caching

numbers = []
p1 = None
p2 = None


class config:
    factor = 7.3
    threshold = 12


def normalize(numbers):
    norm = []
    for num in numbers:
        if num > config.threshold:
            num /= config.factor
        norm.append(num)
    return norm


def normalize_cached(numbers):
    norm = []
    factor = config.factor
    threshold = config.threshold
    append = norm.append
    for num in numbers:
        if num > threshold:
            num /= factor
        append(num)
    return norm


# Function calls
# Additional function for returning
# absolute value of a negative even number
def abs_even(num):
    if num % 2 == 0 and num < 0:
        return abs(num)
    return num


def fix_num(numbers):
    return [abs_even(n) for n in numbers]


# abs_even converter to inline expression
def fix_num_inline(numbers):
    return [-n if n % 2 == 0 and n < 0 else n for n in numbers]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PPoint:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


class SPoint:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


def allocate_points(cls, num):
    return [cls(1, 1) for _ in range(num)]


# Functions to test code performance and
# output results
def test_normalize():
    import random
    # Use constant - always generate the same sequence
    random.seed(666)
    global numbers
    numbers = [random.randint(5, 50) for _ in range(1000)]
    print("normalize time: {0}".format(
        timeit.timeit("normalize(numbers)",
                      "from __main__ import numbers, normalize",
                      number=1000)))
    print("normalize_cached time: {0}".format(
        timeit.timeit("normalize_cached(numbers)",
                      "from __main__ import numbers, normalize_cached",
                      number=1000)))


def test_fix_num():
    import random
    # Use constant - always generate the same sequence
    random.seed(666)
    global numbers
    numbers = [random.randint(-20, 20) for _ in range(1000)]
    print("fix_num time: {0}".format(
        timeit.timeit("fix_num(numbers)",
                      "from __main__ import numbers, fix_num",
                      number=1000)))
    print("fix_num_inline time: {0}".format(
        timeit.timeit("fix_num_inline(numbers)",
                      "from __main__ import numbers, fix_num_inline",
                      number=1000)))


def test_property_access():
    global p1
    global p2
    p1 = Point(1, 2)
    p2 = PPoint(1, 2)
    print("Direct attr access time: {0}".format(
        timeit.timeit("p1.x",
                      "from __main__ import p1",
                      number=100000)))
    print("Property attr access time: {0}".format(
        timeit.timeit("p2.x",
                      "from __main__ import p2",
                      number=100000)))


def test_slots():
    musage_point = memory_usage((allocate_points, (Point, 1000000)))
    musage_spoint = memory_usage((allocate_points, (SPoint, 1000000)))
    print("Mem usage Point. Initial: {0}. Surplus: {1}".
          format(musage_point[0],
                 musage_point[-1] - musage_point[0]))
    print("Mem usage SPoint. Initial: {0}. Surplus: {1}".
          format(musage_spoint[0],
                 musage_spoint[-1] - musage_spoint[0]))


if __name__ == "__main__":
    test_normalize()
    test_fix_num()
    test_property_access()
    test_slots()
    # print(dis.dis(normalize))
    # print(dis.dis(normalize_cached))
