#!/usr/bin/python3

import click
import pandas as pd
import numpy as np
import sys


def parse_kraken_count(input_new_filename_tsv):
    
    df = pd.read_csv(input_new_filename_tsv, sep='\t', index_col= 0 )
    df['kraken_classification'].value_counts()

if __name__ == '__main__':
    input_new_filename_tsv = sys.argv[1]
    parse_kraken_count(input_new_filename_tsv)
