"""
Example of implementing binary search in python
"""
import unittest

def binary_search_recurs(data, search_value):
    return _binary_search(data, search_value, 0, len(data))

def _binary_search(data, search_value, start, end):
    if start + 1 == end:
        return start if data[start] == search_value else None
    else:
        middle = start + (end-start)//2
        guess = data[middle]
        if guess == search_value:
            return middle
        elif guess < search_value:
            return _binary_search(data, search_value, middle + 1, end)
        else:
            return _binary_search(data, search_value, start, middle) 


def binary_search_iter(data, search_value):
    end = len(data)
    start = 0
    while start < end:
        middle = start + (end - start)//2
        guess = data[middle]
        if guess == search_value:
            return middle
        elif guess < search_value:
            start = middle + 1
        else:
            end = middle
    return None

def main():
    data = [1, 2, 3] 
    print(binary_search_iter(data, 1))
    print(binary_search_iter(data, 3))
    print(binary_search_iter(data, 2))
    print(binary_search_iter(data, 4))
    print(binary_search_recurs(data, 1))
    print(binary_search_recurs(data, 3))
    print(binary_search_recurs(data, 2))
    print(binary_search_recurs(data, 4))

if __name__ == '__main__':
    main()
