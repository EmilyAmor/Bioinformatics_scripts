import click
import pandas as pd
import numpy as np

@click.command()
@click.argument('output_name_tsv')

def orthofinder_make_dataframe_OGs_and_protsequences(output_name_tsv):
    """ make a dataframe: OG0000  seq_1, seq_2
                          OG0001  seq_5, seq_10, seq_1000
                          OG0002  seq_9, seq_15
    to merge with annotation tables
    """
    # read in text file orthogroups.txt from OrthoFinder
    f = open('Orthogroups.txt', "r") # hardcoded the inputfile because it was written just for this file
