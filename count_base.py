#!/usr/bin/env python

import click

@click.command()
@click.argument('data')

def count_base(data):
    input = open(data)
    inputfile = input.read()
    a_count = 0
    t_count = 0
    c_count = 0
    g_count = 0
    for base in inputfile:
        if base == 'A':
            a_count += 1
        if base == 'T':
            t_count += 1
        if base == 'C':
            c_count += 1
        if base == 'G':
            g_count += 1
    print ("A:", a_count)
    print ("C:", c_count)
    print ("G:", g_count)
    print ("T:", t_count)

if __name__ == '__main__':
    count_base()
