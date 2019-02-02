#!/usr/bin/python3

import click
import pandas as pd

@click.command()
@click.argument('table_1')
@click.argument('table_2')
@click.argument('new_file_name')
@click.argument('merge_on')


def merge_annotation_tables(table_1, table_2, new_file_name, merge_on):
    """
    USAGE: Merges two transcriptome annotation tables (on 'transcripts' column)
    (NB: ALL TABLES MUST BE .TSV)

    OUTPUT: merged .tsv annotation table

    latest: Also removes duplicated annotations (drops dublicates) and only uses the first entry
    """

    t1 = pd.read_table(table_1,sep='\t', engine='python')
    df1 = t1.drop_duplicates(subset='transcript', keep='first')
    t2 = pd.read_table(table_2,sep='\t', engine='python')
    df2 = t2.drop_duplicates(subset='transcript', keep='first')
    merge = pd.merge(df1, df2, how="left", on=merge_on)
    merge.to_csv(new_file_name, sep='\t', index=False)


if __name__ == '__main__':
      merge_annotation_tables()
