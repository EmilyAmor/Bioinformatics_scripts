
#!/usr/bin/env python

import click
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
@click.command()
@click.argument('reversed_fasta')
@click.argument('rev_compl_new_name')

def rev_compl_biopyth(reversed_fasta,rev_compl_new_name):
    def make_rc_record(record):
        return SeqRecord(seq = record.seq.reverse_complement(), id = "" + record.id, description = "")

    records = map(make_rc_record, SeqIO.parse(reversed_fasta, "fasta"))
    SeqIO.write(records, rev_compl_new_name, "fasta")


if __name__ == '__main__':
    rev_compl_biopyth()
