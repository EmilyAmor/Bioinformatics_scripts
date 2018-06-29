import click
from Bio import SeqIO

@click.command()
@click.argument('fastafile')

def clean_fasta_headers(fastafile):
    """ from TransDecoders predicted ORFs output (.cds), extract all the names of ORFs that refer to the contigs from which they came
    e.g.
    input:
    >TRINITY_DN10006_c0_g1_i1.p1 TRINITY_DN10006_c0_g1~~TRINITY_DN10006_c0_g1_i1.p1  ORF type:5prime_partial len:155 (-),
    score=35.04,tify|PF06200.13|5.4e-12,CCT_2|PF09425.9|7.8e-07 TRINITY_DN10006_c0_g1_i1:429-893(-)
    ACTCTAAAATTTCAATCTATCTTGGAGCGAGAAAGAAAGATGAGGAGAAATTGCAATTTG
    GAACTTGCTCTTTTTCCTTCCTACGGTTCTGACCACCACCACCACCCCATGATGATGGAA
    GAAGGTTGTGGGAGCCCAAAGCTACAGCATCTGATCCACCACCAGCAGCAACGTCAGGAG
    >TRINITY_DN10007_c0_g1_i1.p1 TRINITY_DN10007_c0_g1~~TRINITY_DN10007_c0_g1_i1.p1  ORF type:internal len:113 (-),
    score=23.54,OTU|PF02338.18|0.00051 TRINITY_DN10007_c0_g1_i1:3-338(-)
    CCGGCGAGGTGGCTCCACCGTTCTGACTCGGCTTGGCTACTCTTTGGCGTCTGCGCCTGC
    CTCGCGCCGCCGCCACCGCCGCTTTTGGTTGGCGAATTTCCCGAGGCGCCGTTGCCGGTG

    output: TRINITY_DN10006_c0_g1_i1
            TRINITY_DN10007_c0_g1_i1 """


    transcript_names = []
    for record in SeqIO.parse(fastafile, "fasta"):
        transcript_names.append((record.id).split("."))
    for i in transcript_names:
        print (i[0])

if __name__ == '__main__':
      clean_fasta_headers()
