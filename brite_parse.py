#!/usr/bin/python3

import click
import pandas as pd
import numpy as np
import sys


def brite_parse(brite_file, letter, output_tsv):
    dict_count = {}

    C_name = "nothiny_yet"
    count_C = 0

    with open(brite_file) as f:
        for line in f:
            if line.startswith(letter):
                dict_count[C_name] = count_C
                C_name = ((line.strip(" ")[1:]).strip("\n")).lstrip()
                count_C = 0
            if line.startswith("E"):
                count_C += 1

    df = pd.DataFrame.from_dict(dict_count, orient='index')
    df.to_csv(output_tsv, sep='\t')

if __name__ == '__main__':
    brite_file = sys.argv[1]
    letter = sys.argv[2]
    output_tsv =sys.argv[3]
    brite_parse(brite_file, letter, output_tsv)
