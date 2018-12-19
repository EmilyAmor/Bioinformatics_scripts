import click
import pandas as pd
import numpy as np

@click.command()
@click.argument('OG_list_csv')
@click.argument('plant_number')
@click.argument('unique_rooibos/aspalathin_orthofinder')
@click.argument('input_new_filename_tsv')

def extract_og_contigs_orthofinder(OG_list_csv, orthogroups_csv, plant_number, unique_rooibos/aspalathin_orthofinder, input_new_filename_tsv):
    """ extract OGs of interest from Orthogroups.csv (output from OrthoFinder)"""

    # read in the OGs (from Orthofinder) that you want to extract
    with open(OG_list_csv, "r") as f:
    test=[i for line in f for i in line.split(',')]
    stripped_line = [s.rstrip() for s in test]
    OGs = list(filter(None, stripped_line))

    # read in the complete orthogroups.csv file from orthofinder software
    orthologs = pd.read_csv(orthogroups_csv, sep='\t', header=0,index_col=0, engine='python')

    # select contigs
    protein_IDs_list = []
    for i in OGs:
        a = orthologs.loc[i][plant_number]
        protein_IDs_list.append(a)
    # edit contigs contigs names
    joined_list = '\n'.join(protein_IDs_list)
    protein_names = joined_list.replace("\n", ",").replace(" ","").split(",")

    # Write protein names to a dataframe then save dataframe to csv file
    df = pd.DataFrame({'transcript':protein_names})
    df[unique_rooibos/aspalathin_orthofinder] = 'yes'
    new_df = df.set_index('transcript')
    new_df.to_csv(input_new_filename_tsv, sep='\t')

if __name__ == '__main__':
      extract_og_contigs_orthofinder()
