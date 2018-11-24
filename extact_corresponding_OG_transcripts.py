#!/usr/bin/python3

import click
import pandas as pd
import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

@click.command()
@click.argument('annotation_table')
@click.argument('OGs_of_interest_csv')
@click.argument('Orthogroups_csv')
@click.argument('plant_number')
@click.argument('transcript_OG_new_file_name')
@click.argument('new_merged_annotation_table_name')

def extact_corresponding_OG_transcripts(annotation_table, OGs_of_interest_csv, Orthogroups_csv, plant_number, transcript_OG_new_file_name, new_merged_annotation_table_name):
    """  extract transcripts according to OG from OrthoFinder Orthogroups.csv file"""

    # Read in annotation table:
    annotation_table = pd.read_csv(annotation_table, sep='\t', header=0,index_col=0, engine='python')

    # Read on OGs that want to extract:
    with open(OGs_of_interest_csv, "r") as f:
        test=[i for line in f for i in line.split(',')]
        stripped_line = [s.rstrip() for s in test]
    OGs = list(filter(None, stripped_line))

    # Read in Orthogroups.csv from OrthoFinder:
    orthologs = pd.read_csv(Orthogroups_csv, sep='\t', header=0,index_col=0, engine='python')

    # Select transcripts:
    protein_IDs_list = []
    for i in OGs:
        a = orthologs.loc[i][plant_number]
        protein_IDs_list.append(a)
    joined_list = '\n'.join(protein_IDs_list)
    protein_names = joined_list.replace("\n", ",").replace(" ","").split(",")
    contigs = [] # save only contig names
    for i in protein_names:
        contigs.append(re.sub(r'\|m.*', '', i))

    # write gene names to dataframe and csv output:
    df = pd.DataFrame({'t':contigs})
    df['aspalathin'] = 'aspalathin_negative' # change according to new column names of interest
    new_dataframe = df.set_index('t')
    new_dataframe.to_csv("transcript_OG_new_file_name", sep='\t')

    # merge tables to extend annotation tables and write to new csv
    merge = pd.merge(annotation_table, new_dataframe, how="left", right_index=True, left_index=True)
    merge.to_csv(new_merged_annotation_table_name, sep='\t')

if __name__ == '__main__':
      extact_corresponding_OG_transcripts()
