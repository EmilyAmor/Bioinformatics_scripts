#!/usr/bin/python3

import click
import pandas as pd

@click.command()
@click.argument('table_1')
@click.argument('table_1_separator')
@click.argument('table_2')
@click.argument('table_2_separator')
@click.argument('new_file_name')

def merge_annotation_tables(table_1, table_1_separator, table_2, table_2_separator, new_file_name):
    """Merges two transcriptome annotation tables (on 'transcripts' column), given the tables and their separators as input. Ouputs table in tsv format"""
    t1 = pd.read_table(table_1,sep=table_1_separator, engine='python')
    t2 = pd.read_table(table_2,sep=table_2_separator, engine='python')
    merge = pd.merge(t1, t2, how="left", on="transcript")
    merge.to_csv(new_file_name, sep='\t')


if __name__ == '__main__':
      merge_annotation_tables()
