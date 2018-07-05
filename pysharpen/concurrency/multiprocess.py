"Module demonstrates basics of multiprocessing"
import itertools
import multiprocessing as mpc
import os


def processor(*args):
    "Calculates maximum of xor"
    x_numbers, queries = args[0]
    result = []
    for query in queries:
        a, l, r = query
        result.append(max(a ^ x_j for x_j in x_numbers[l+1:r]))
    return result


def main():
    x_numbers = [2, 5, 6, 18]
    data = [(x_numbers, [[10, 1, 3]]), (x_numbers, [[10, 1, 3]]), (x_numbers, [[10, 1, 3]])]
    with mpc.Pool(os.cpu_count()) as p:
        result = p.map(processor, data)
        result = [element for partial_result in data for element in partial_result]
    print(result)

if __name__ == "__main__":
    main()
