import bz2
from collections import namedtuple
from csv import DictReader
from datetime import datetime as dt
from helpers.helpers import print_header
import os
import pandas as pd

def parse_timestamp(ts_str):
    return dt.strptime(ts_str, '%Y-%m-%d %H:%M:%S') 


Column = namedtuple('Column', ['src', 'dst', 'conv'])
columns = [
    Column('VendorID', 'vendor_id', int),
    Column('tpep_pickup_datetime', 'tpep_pickup_datetime', parse_timestamp),
    Column('tpep_dropoff_datetime', 'tpep_dropoff_datetime', parse_timestamp),
    Column('passenger_count', 'passenger_count', int),
    Column('trip_distance', 'trip_distance', float),
    Column('RatecodeID', 'ratecode_id', int),
    Column('store_and_fwd_flag', 'store_and_fwd_flag', str),
    Column('PULocationID', 'pu_location_id', int),
    Column('DOLocationID', 'do_location_id', int),
    Column('payment_type', 'payment_type', int),
    Column('fare_amount', 'fare_amount', float),
    Column('extra', 'extra', float),
    Column('mta_tax', 'mta_tax', float),
    Column('tip_amount', 'tip_amount', float),
    Column('tolls_amount', 'tolls_amount', float),
    Column('improvement_surcharge', 'improvement_surcharge', float),
    Column('total_amount', 'total_amount', float)
]


def iter_records(filepath):
    with bz2.open(filepath, 'rt') as f:
        reader = DictReader(f)
        for row in reader:
            dst_row = {}
            for col in columns:
                conv_function = col.conv
                dst_row[col.dst] = conv_function(row[col.src])
            yield dst_row


def csv_module_example():
    print_header('CSV example')
    from pprint import pprint
    src_file = f'{os.getcwd()}{os.sep}pysharpen{os.sep}dataengineering{os.sep}ingestion{os.sep}taxi.csv.bz2' 
    for idx, row in enumerate(iter_records(src_file)):
        if idx > 10:
            break
        pprint(row)

def pandas_example():
    print_header('Pandas example')
    from pprint import pprint
    src_file = f'{os.getcwd()}{os.sep}pysharpen{os.sep}dataengineering{os.sep}ingestion{os.sep}taxi.csv.bz2' 
    with bz2.open(src_file, 'rt') as f:
        df = pd.read_csv(f, parse_dates=['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
        for idx, row in df.iterrows():
            if idx > 10:
                break
            pprint(row)


def main():
    csv_module_example()
    pandas_example()



if __name__ == '__main__':
    main()