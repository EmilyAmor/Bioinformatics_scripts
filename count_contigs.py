#!/usr/bin/env python

import click

@click.command()
@click.argument('fastafile')
def count_contigs(fastafile):
  """ Counts the number of contigs in a fasta file generated from an assembly"""

  # import file into a dictionary using biopython module
  from Bio import SeqIO
  seq_dict = {rec.id : rec.seq for rec in SeqIO.parse(fastafile, "fasta")}

  # count contigs
  count_dict = {}
  for id in seq_dict:
      count_dict[id] = len(seq_dict[id])

  # cluster amount of contigs according to their lengths
  smaller_than_500 = 0
  up_to_1000bp = 0
  up_to_5000bp = 0
  ten_thousand = 0
  twenty_thousand = 0
  fifty_thousand = 0
  hundred_thousand_and_larger = 0
  larger_than_100000 = 0

  for id in count_dict:
      if count_dict[id] <= 500:
          smaller_than_500 += 1
      elif 500 < count_dict[id] <= 1000:
          up_to_1000bp += 1
      elif 1000 < count_dict[id] <= 5000:
          up_to_5000bp += 1
      elif 5000 < count_dict[id] <= 10000:
          ten_thousand += 1
      elif 10000 < count_dict[id] <= 20000:
          twenty_thousand += 1
      elif 20000 < count_dict[id] <= 50000:
          fifty_thousand += 1
      elif 50000 < count_dict[id] <= 100000:
          hundred_thousand_and_larger += 1
      elif 100000 < count_dict[id]:
          larger_than_100000 += 1

  print ("up to 500 bp:",smaller_than_500)
  print ("500 to 1000 bp:", up_to_1000bp)
  print ("1000 - 5000 bp:", up_to_5000bp)
  print ("5000 - 10 000 bp:", ten_thousand)
  print ("10 000 - 20 000 bp:", twenty_thousand)
  print ("20 000 - 50 000 bp:", fifty_thousand)
  print ("50 000 - 100 000 bp:", hundred_thousand_and_larger)
  print ("larger than 100 000 bp:", larger_than_100000)

if __name__ == '__main__':
      count_contigs()
