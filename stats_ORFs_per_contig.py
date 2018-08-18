#!/usr/bin/python3

import click
import numpy as np

@click.command()
@click.argument('orf_header_file')

def stats_ORFs_per_contig(orf_header_file):
    f= open(orf_header_file, "r")
    list_1 = f.readlines()
    list_2 = []
    for i in list_1:
        list_2.append(i.rstrip("\n"))

    list_3 = list(filter(lambda x: x!= '',list_2))
    counts = list(map(lambda x: int(x.split(" ")[0]), list_3))

    np_mean = np.mean(counts)
    np_std = np.std(counts)
    print('mean:',np_mean)
    print('stdev:',np_std)

if __name__ == '__main__':
      stats_ORFs_per_contig()
