import sys
from multiprocessing import Pool
from collections import abc
import gzip

def worker(args):
    worker_idx, source, word, chunk_size = args
    try:
        index = source[worker_idx*chunk_size: (worker_idx + 1)*chunk_size].index(word)
        return index + worker_idx*chunk_size
    except ValueError:
        return None


def find_word_index(words, word, process_number):
    chunk_size = int(len(words) / process_number + 1)
    pool = Pool(process_number)
    results = pool.map(worker, [(idx, words, word, chunk_size) for idx in range(process_number)], chunksize=1)
    return [result for result in results if result]


def load_text(file_path):
    return [line.strip() for line in gzip.open(file_path, mode="rt")]


def main(file_path, word, process_number):
    words = load_text(file_path)
    return find_word_index(words, word, process_number)


if __name__ == "__main__":
    print(main(sys.argv[1], sys.argv[2], int(sys.argv[3])))
