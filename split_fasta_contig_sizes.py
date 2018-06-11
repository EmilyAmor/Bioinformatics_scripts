#!/usr/bin/env python3

import click
from Bio import SeqIO
@click.command()
@click.argument('inputfilename')

def fastasplit(inputfilename):
    smaller_than_500 = []
    up_to_1000bp = []
    up_to_5000bp = []
    ten_thousand = []
    twenty_thousand = []

    for record in SeqIO.parse("trinity.fa", "fasta"):
    #print (record.seq)
      if len(record.seq) <= 500:
          smaller_than_500.append(record)
      elif 500 < len(record.seq) <= 1000:
          up_to_1000bp.append(record)
      elif 1000 < len(record.seq)  <= 5000:
          up_to_5000bp.append(record)
      elif 5000 < len(record.seq) <= 10000:
          ten_thousand.append(record)
      elif 10000 < len(record.seq):
          twenty_thousand.append(record)


    SeqIO.write(smaller_than_500, "contigs<500bp.fa", "fasta")
    SeqIO.write(up_to_1000bp, "500>contigs=1000bp.fa", "fasta")
    SeqIO.write(up_to_5000bp, "1000<contigs=5000bp.fa", "fasta")
    SeqIO.write(ten_thousand, "5000<contigs=10000bp.fa", "fasta")
    SeqIO.write(twenty_thousand, "10000<contigs.fa", "fasta")

if __name__ == '__main__':
      fastasplit()
