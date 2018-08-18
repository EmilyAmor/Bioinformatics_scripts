#!/usr/bin/python3

import click

@click.command()
@click.argument('pfam_transcripts1')
@click.argument('pfam_transcripts2')
@click.argument('new_file_name')

def common_domains(pfam_transcripts1, pfam_transcripts2, new_file_name):
    """ outputs which transcripts have both domains"""
    f1 = open(pfam_transcripts1, 'r')
    f2 = open(pfam_transcripts2, 'r')
    domain1 = []
    domain2 = []
    for line in f1:
        domain1.append(line)
    for line in f2:
        domain2.append(line)
    transcripts_with_both_domains = set(domain1) & set(domain2)

    #write to file
    c = open(new_file_name, "w")
    for i in transcripts_with_both_domains:
        c.write(i)
    c.close()

if __name__ == '__main__':
      common_domains()
