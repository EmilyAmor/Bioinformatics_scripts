import click
import numpy as np
import pandas as pd
from scipy import stats

@click.command()
@click.argument('input_file')
@click.argument('sample_column_name')
@click.argument('first_test_column_name')
@click.argument('second_test_column_name')

def orthofinder_make_dataframe_OGs_and_protsequences(input_file, sample_column_name, first_test_column_name, second_test_column_name):
    """ make a dataframe: OG0000  seq_1, seq_2
                          OG0001  seq_5, seq_10, seq_1000
                          OG0002  seq_9, seq_15
    to merge with annotation tables
    """
    
