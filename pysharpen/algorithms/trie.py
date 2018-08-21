"""
https://en.wikipedia.org/wiki/Trie
"""

import random
from time import perf_counter
from collections import defaultdict

import sys

class Node2:
    def __init__(self, num_bits):
        self._zero_node = None
        self._one_node = None
        self._num_bits = num_bits
        self._zero_indices = defaultdict(list)
        self._one_indices = defaultdict(list)

    def is_range_in_index(self, index, start, end):
        for idx in range(start, end + 1):
            if idx in index:
                return True
        return False

    def insert_zero(self, parent_node, num, index):
        if not parent_node._zero_node:
            parent_node._zero_node = Node(self._num_bits)
        if index not in parent_node._zero_node._zero_indices:
            parent_node._zero_node._zero_indices[index] = num
        return parent_node._zero_node

    def insert_one(self, parent_node, num):
        if not parent_node._one_node:
            parent_node._one_node = Node(self._num_bits)
        if index not in parent_node._one_node._one_indices:
            parent_node._one_node._one_indices[index] = num
        return parent_node._one_node

    def is_msb_set(self, num):
        return num & self._msb_mask != 0

    def shift(self, num):
        return (num << 1) & self._value_mask

    def insert(self, num, index):
        current_num = num
        current_node = self
        for _ in range(self._num_bits):
            if self.is_msb_set(current_num):
                current_node = self.insert_one(current_node, num, index)
            else:
                current_node = self.insert_zero(current_node, num, index)
            current_num = self.shift(current_num)

    def max_xor(self, num, start, end, bits_left):
        if self.is_msb_set(num):
            if self.is_range_in_index(self._zero_indices, start, end):
                return self._zero_node.max_xor(
                    self.shift(num), start, end, bits_left - 1)
            else:
                pass
        else:
            pass


class Node:
    def __init__(self, num_bits):
        self._zero_node = None
        self._one_node = None
        self._num_bits = num_bits
        self._values_on_path = {}
        self._value_mask = 2**num_bits - 1
        self._msb_mask = 2**(num_bits - 1)
        self._values_size = 0

    def __str__(self):
        s = ""
        s += f"Zero node exists: {self._zero_node != None}{chr(10)}"
        s += f"One node exists: {self._one_node != None}{chr(10)}"
        s += f"Values: {self._values_on_path}{chr(10)}"
        s += f"Values size: {self._values_size}{chr(10)}"
        return s

    def insert_zero(self, parent_node, num):
        if not parent_node._zero_node:
            parent_node._zero_node = Node(self._num_bits)
        if num not in parent_node._zero_node._values_on_path:
            parent_node._zero_node._values_on_path[num] = True
            parent_node._zero_node._values_size += 1
        return parent_node._zero_node

    def insert_one(self, parent_node, num):
        if not parent_node._one_node:
            parent_node._one_node = Node(self._num_bits)
        if num not in parent_node._one_node._values_on_path:
            parent_node._one_node._values_on_path[num] = True
            parent_node._one_node._values_size += 1
        return parent_node._one_node

    def is_msb_set(self, num):
        return num & self._msb_mask != 0

    def shift(self, num):
        return (num << 1) & self._value_mask

    def insert(self, num):
        current_num = num
        current_node = self
        for _ in range(self._num_bits):
            if self.is_msb_set(current_num):
                current_node = self.insert_one(current_node, num)
            else:
                current_node = self.insert_zero(current_node, num)
            current_num = self.shift(current_num)

    def max_xor(self, num):
        current_num = num
        current_node = self
        for _ in range(self._num_bits):
            if self.is_msb_set(current_num):
                if current_node._zero_node:
                    current_node = current_node._zero_node
                elif current_node._one_node:
                    current_node = current_node._one_node
                else:
                    return current_node._values_on_path[0]

            else:
                if current_node._one_node:
                    current_node = current_node._one_node
                elif current_node._zero_node:
                    current_node = current_node._zero_node
                else:
                    return current_node._values_on_path[0]
            current_num = self.shift(current_num)

        if current_node and current_node._values_size == 1:
            return list(current_node._values_on_path)[0]
        else:
            raise ValueError("Trie is in inconsistent state")


def max_xor_trie(x, queries):
    result = []
    for query in queries:
        node = Node(16)
        a, l, r = query
        for x_val in x[l - 1:r]:
            node.insert(x_val)
        result.append(node.max_xor(a))
    return result


def max_xor(x, queries):
    result = []
    for query in queries:
        a, l, r = query
        result.append(max(a ^ xj for xj in x[l - 1:r]))
    return result


def generate_x(num, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(num_x)]


def generate_queries(num_x, num_queries, a_min_value, a_max_value):
    starts = [random.randint(1, num_x - 1) for _ in range(num_queries)]
    return [[
        random.randint(a_min_value, a_max_value), s,
        random.randint(s + 1, num_x)
    ] for s in starts]


if __name__ == "__main__":
    num_x = 10
    num_queries = 5
    x = generate_x(num_x, 1, 32768)
    q = generate_queries(num_x, num_queries, 1, 32768)
    print(x)
    print(q)
    start_time = perf_counter()
    res = max_xor(x, q)
    duration = perf_counter() - start_time
    print("Duration (list): {0}".format(duration))
    print(res)
    start_time = perf_counter()
    res = max_xor_trie(x, q)
    duration = perf_counter() - start_time
    print("Duration (trie): {0}".format(duration))
    print(res)
