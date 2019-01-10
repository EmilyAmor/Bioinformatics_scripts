#!/usr/bin/python3

import click
import pandas as pd
import numpy as np
import sys


def parse_diamond_taxonomy_count(input_new_filename_tsv, output_file_name_tsv):
    """ Read in tsv in format "transcript","kingdom", "phylum","class","order","family, genus, specie" and gives stipulated counts"""
    df = pd.read_csv(input_new_filename_tsv, sep='\t')
    taxonomy = ["kingdom", "phylum", "class", "order", "family", "g", "specie"]
    appended_data = []
    df_all = pd.DataFrame()
    for i in taxonomy:
        data = df[i].value_counts().reset_index()
        appended_data.append(data)
    appended_data = pd.concat(appended_data, axis=1)
    appended_data.to_csv(output_file_name_tsv, sep="\t")


if __name__ == '__main__':
    input_new_filename_tsv = sys.argv[1]
    output_file_name_tsv = sys.argv[2]
    parse_diamond_taxonomy_count(input_new_filename_tsv, output_file_name_tsv)
