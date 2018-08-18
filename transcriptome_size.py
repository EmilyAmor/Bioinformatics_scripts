import click
from Bio import SeqIO
@click.command()
@click.argument('transcriptome')

def transcriptome_size(transcriptome):
    """ calculate the size of a transcriptome in base pairs"""

    from Bio import SeqIO
    count = 0
    for seq_record in SeqIO.parse("transcripts.fasta", "fasta"):
        count += (len(seq_record))

    print ("size of transcriptome:", (count/1000), "Mbp")

if __name__ == '__main__':
      transcriptome_size()
