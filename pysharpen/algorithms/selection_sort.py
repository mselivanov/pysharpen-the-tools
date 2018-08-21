"""
Module demonstrates selection sort
"""
from random import randint


def selection_sort_recurs(data):
    "Recursive selection sort implementation"
    if len(data) <= 1:
        return list(data)
    minimum_value = data[0]
    minimum_index = 0
    for idx, value in enumerate(data):
        if value < minimum_value:
            minimum_value = value
            minimum_index = idx
    return [minimum_value] + selection_sort_recurs(data[0:minimum_index] +
                                                   data[minimum_index + 1:])


def selection_sort_iter(data):
    "Iterative selection sort implementation"
    result = []
    _data = list(data)
    while _data:
        _idx = 0
        _value = _data[0]
        for idx, value in enumerate(_data):
            if value < _value:
                _idx = idx
                _value = value
        result.append(_value)
        del _data[_idx]
    return result


def main():
    "Main function calls sort functions"
    data = [randint(1, 10000) for _ in range(10)]
    print(f"Initial data: {data}")
    sorted_data = selection_sort_recurs(data)
    print(f"Sorted data (recursive): {sorted_data}")
    sorted_data = selection_sort_iter(data)
    print(f"Sorted data (iterative): {sorted_data}")


if __name__ == '__main__':
    main()
