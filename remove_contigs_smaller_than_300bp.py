#!/usr/bin/python3

import click
from Bio import SeqIO
@click.command()
@click.argument('inputfilename')

def remove_small_contigs(inputfilename):
    """remove contigs smaller than 300bp (store in separate .fa file)"""
    
    smaller_than_300bp = []
    larger_than_300bp = []
    for record in SeqIO.parse(inputfilename, "fasta"):
        if len(record.seq) <= 300:
            smaller_than_300bp.append(record)
        elif 300 < len(record.seq):
            larger_than_300bp.append(record)

    SeqIO.write(smaller_than_300bp, "contigs_smaller_than_300bp.fa", "fasta")
    SeqIO.write(larger_than_300bp, "contigs_larger_than_300bp.fa", "fasta")

if __name__ == '__main__':
    remove_small_contigs()
