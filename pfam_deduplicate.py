#!/usr/bin/python3

import click
import pandas as pd
import numpy as np

@click.command()
@click.argument('pfam_csv')
@click.argument('edit_new_dedupl_file_name_tsv')

def pfam_deduplicate(pfam_csv,edit_new_dedupl_file_name_tsv):
    """ Input Pfam.csv with duplicate (more than one entry per protein) pfam accession and pfam ids
    are inserted into a single row and separated by "," """

    df = pd.read_csv(pfam_csv, sep=',', index_col=0)
    deduplicate =  df.groupby('transcript').agg({'Pfam_accession': ', '.join,
                             'pfam_domain':', '.join }).reset_index()
    deduplicate.to_csv(edit_new_dedupl_file_name_tsv, sep='\t')

if __name__ == '__main__':
      pfam_deduplicate()
