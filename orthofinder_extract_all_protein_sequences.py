#!/usr/bin/python

import sys
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def orthofinder_extract_all_proteins(orthogroups_csv, transcriptome_proteins, OG_IDs, name_output_fasta, plant_ID):
    """ Extract OrthoGrous (OGs) of interest corresponding protein sequences from a protein.fasta file """

    # read in the files:

    #1) complete orthogroups.csv file from orthofinder software output
    orthologs = pd.read_csv(orthogroups_csv, sep='\t', header=0,index_col=0, engine='python')

    #2) protein sequences from a specified transcriptome
    record_dict = SeqIO.to_dict(SeqIO.parse(transcriptome_proteins, "fasta"))

    #3) List of OG IDs of interest that want to be extracted
    with open(OG_IDs, "r") as f:
        test=[i for line in f for i in line.split(',')]
        stripped_line = [s.rstrip() for s in test]
    OGs = list(filter(None, stripped_line))

    # Find the corresponding transcript_IDs of a specified specie to the OG IDs of interest
    transcript_IDs = []
    for i in OGs:
        a = orthologs.loc[i, plant_ID]
        transcript_IDs.append(a.strip())
    ids =[i for line in transcript_IDs for i in line.split(',')]
    ids = [x.strip(' ') for x in ids]

    # compile a fasta file containing the proteins of interest
    fasta = ''
    for i in ids:
        fasta += record_dict[i].format("fasta")

    # write out fasta file
    output_file = open(name_output_fasta, 'w')
    output_file.write(fasta)
    output_file.close()

if __name__ == '__main__':
    orthogroups_csv = sys.argv[1]
    transcriptome_proteins = sys.argv[2]
    OG_IDs = sys.argv[3]
    name_output_fasta = sys.argv[4]
    plant_ID = sys.argv[5]

    orthofinder_extract_all_proteins(orthogroups_csv, transcriptome_proteins, OG_IDs, name_output_fasta, plant_ID)
