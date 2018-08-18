import click
from Bio import SeqIO

@click.command()
@click.argument('fasta_file')
@click.argument('wanted_file')
@click.argument('result_file_name')

def extract_sequences(fasta_file, wanted_file, result_file_name):
    """given a text file with fasta ID's, a fasta file, and the name of the new file to be created:
    extract all the sequences of give ID's into a new file"""
    #fasta_file = fasta_file # Input fasta file
    #wanted_file = wanted_file # Input interesting sequence IDs, one per line
    #result_file = result_file # Output fasta file

    wanted = set()
    with open(wanted_file) as f:
        for line in f:
            line = line.strip()
            if line != "":
                wanted.add(line)

    fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
    with open(result_file_name, "w") as f:
        for seq in fasta_sequences:
            if seq.id in wanted:
                SeqIO.write([seq], f, "fasta")

if __name__ == '__main__':
      extract_sequences()
