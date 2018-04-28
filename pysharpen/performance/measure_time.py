from time import perf_counter
from timeit import timeit
from random import shuffle

seq = []


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n*factorial_recursive(n-1)


def factorial_iter(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial_test():
    n = 996
    message = "Factorial method: {0}. Duration: {1}"
    start_time = perf_counter()
    factorial_recursive(n)
    duration = perf_counter() - start_time
    print(message.format("recursive", duration))

    start_time = perf_counter()
    factorial_iter(n)
    duration = perf_counter() - start_time
    print(message.format("iterative", duration))


def max_python(seq):
    max_val = seq[0]
    for val in seq:
        if val > max_val:
            max_val = val
    return max_val


def max_builtin(seq):
    return max(seq)


def max_test():
    global seq
    seq = [x for x in range(1000000)]
    shuffle(seq)
    print("max_builtin took ",
          timeit("max_builtin(seq)",
                 "from __main__ import seq, max_builtin",
                 number=100))
    print("max_python took ",
          timeit("max_python(seq)",
                 "from __main__ import seq, max_python",
                 number=100))


def cprofile_test():
    import cProfile
    cProfile.run("factorial_recursive(900)",
                 filename="factorial_recursive.out")


def main():
    factorial_test()
    # max_test()
    cprofile_test()


if __name__ == "__main__":
    main()
