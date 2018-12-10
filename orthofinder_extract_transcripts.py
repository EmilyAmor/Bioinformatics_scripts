#!/usr/bin/python

import sys
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
"""
@click.command()
@click.argument('orthogroups_csv')
@click.argument('transcriptome_proteins')
@click.argument('OG_ID')
"""
def orthofinder_extract_transcripts(orthogroups_csv, transcriptome_proteins, OG_ID, plant_ID):

    # read in the complete orthogroups.csv file from orthofinder software
    orthologs = pd.read_csv(orthogroups_csv, sep='\t', header=0,index_col=0, engine='python')

    # select a specific ortho group of interest in a specific specie
    single_plant = orthologs.loc[OG_ID][plant_ID]

    # make a list of just the transcript IDs from the specie of interest OGs
    single_plant_list = single_plant.split(',')
    new_list = []
    for i in single_plant_list:
        new_list.append(i.split()[0])

    # get protein sequence that matches the transcript IDs
    record_dict = SeqIO.to_dict(SeqIO.parse(transcriptome_proteins, "fasta"))

    # write the transcript IDs and protein sequences to new fasta file
    fasta = ''
    for i in new_list:
        fasta += record_dict[i].format("fasta")

    output_file = open(plant_ID + "_" + OG_ID + ".fasta", 'w')
    output_file.write(fasta)
    output_file.close()
    return

if __name__ == '__main__':
    orthogroups_csv = sys.argv[1]
    transcriptome_proteins = sys.argv[2]
    OG_ID = sys.argv[3]
    plant_ID = sys.argv[4]

    orthofinder_extract_transcripts(orthogroups_csv, transcriptome_proteins, OG_ID, plant_ID)
