#! /Users/nguyen/anaconda3/bin/python

import pandas as pd
import sys

def preview_csv(file, delimiter=','):
    data = pd.read_csv(sys.argv[1], delimiter=delimiter)

    print('-------------')
    print('DESCRIBE')
    print('-------------')
    print(data.describe())
    print('-------------')
    print('INFO')
    print('-------------')
    print(data.info())
    print('-------------')
    print('COLUMNS')
    print('-------------')
    print(data.columns)
    print('-------------')
    print('HEAD')
    print('-------------')
    print(data.head())
    print('-------------')
    print('TAIL')
    print('-------------')
    print(data.tail())

if __name__ == '__main__':
    if len(sys.argv) > 2:
        preview_csv(sys.argv[1], sys.argv[2])
    else:
        preview_csv(sys.argv[1], ',')
