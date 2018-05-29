"""
Module for loading csv file demo and calculating average of 1 column
File format:
    csv
    first row is a header row
    Row structure (left to right):
    - date - in dd.mm.yyyy format
    - date_block - integer
    - shop_id - integer
    - item_id - integer
    - item_price - float
    - item_cnt_day - items sold, integer
"""
import sys
import cProfile
import csv


def calc_avg_python(path_to_file):
    """Calculate sales average using only python"""
    total = 0
    idx = 0
    with open(path_to_file, "rt") as data:
        data_row = data.readline()
        while data_row != '':
            if idx > 0:
                total += float(data_row.split(",")[4])
            idx += 1
            data_row = data.readline()
    return total / idx if idx > 0 else 0


def calc_avg_csvreader(path_to_file):
    with open(path_to_file, "rt", newline = '') as data:
        reader = csv.DictReader(data)
        idx = 1
        total = 0
        for row in reader:
            total += float(row["item_price"])
            idx += 1
    return total / idx

def test_calc_avg(file_path):
    """
    Test method
    """
    pr = cProfile.Profile()
    pr.enable()
    calc_avg_python(file_path)
    pr.disable()
    pr.print_stats(sort="time")
    pr = cProfile.Profile()
    pr.enable()
    calc_avg_csvreader(file_path)
    pr.disable()
    pr.print_stats(sort="time")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage python calcaverage.py <path to sales files>")
    else:
        file_path = sys.argv[1]
        test_calc_avg(file_path)
