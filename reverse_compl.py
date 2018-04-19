#!/usr/bin/env python

import click

@click.command()
@click.argument('data')

def rev_compl(data):
    input = open(data)
    sequence = input.read()
    rev_seq = sequence[::-1]
    rev_seq_compl = ''
    for base in rev_seq:
        if base == 'A':
            rev_seq_compl += 'T'
        if base == 'T':
            rev_seq_compl += 'A'
        if base == 'C':
            rev_seq_compl += 'G'
        if base == 'G':
            rev_seq_compl += 'C'
    print (rev_seq_compl)

if __name__ == '__main__':
    rev_compl()
