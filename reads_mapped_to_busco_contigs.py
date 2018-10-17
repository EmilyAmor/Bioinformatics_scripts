#!/usr/bin/env python3

import click
import pandas as pd
from Bio import SeqIO
@click.command()
@click.argument('contigs_hit_busco')
@click.argument('bowtie_stats')

def mapped_reads_to_busco_contigs(contigs_hit_busco, bowtie_stats ):

    # read in list of contigs that have a hit to a busco
    file = open(contigs_hit_busco, 'r')
    busco_transcripts = []
    for line in file:
        busco_transcripts.append(line.strip())

    # read in mapped_reads_to_contig.tsv file from bowtie2 .sam output
    reads_that_map = pd.read_csv(bowtie_stats, sep='\t', header=0)
    mapped_reads_dict = dict(zip(reads_that_map['contigs'], reads_that_map['mapped_reads']))

    new_dict = {}
    for transcript in busco_transcripts:
        new_dict[transcript] = mapped_reads_dict[transcript]

    s = pd.Series(new_dict)
    s.to_csv('mapped_reads_to_busco_contigs.tsv', sep='\t')

if __name__ == '__main__':
    mapped_reads_to_busco_contigs()
