#!/usr/bin/python3

import click
import pandas as pd
import numpy as np
import sys


def parse_diamond_taxonomy_count(input_new_filename_tsv, taxon_level, output_file_name_tsv):
    """ Read in tsv in format "transcript","kingdom", "phylum","class","order","family" and gives stipulated counts"""
    df = pd.read_csv(input_new_filename_tsv, sep='\t')
    new_df = df.set_index(["transcript","kingdom", "phylum","class","order","family"]).count(level=taxon_level)
    new_df.to_csv(output_file_name_tsv, sep='\t')


if __name__ == '__main__':
    input_new_filename_tsv = sys.argv[1]
    taxon_level = sys.argv[2]
    output_file_name_tsv = sys.argv[3]
    parse_diamond_taxonomy_count(input_new_filename_tsv, taxon_level, output_file_name_tsv)
