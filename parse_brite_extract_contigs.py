import click
import pandas as pd
import numpy as np
import sys


def brite_parse(brite_file, letter, output_tsv_name):
    """ Parse Brite modules file and count transcripts for each module"""

    my_dict = {}
    with open(brite_file) as f:
        for line in f:
            if line.startswith(letter):
                name = ((line.strip(" ")[1:]).strip("\n")).lstrip()
                my_dict[name] = 0
            if line.startswith("E"):
                my_dict[name] += 1
    df = pd.DataFrame.from_dict(my_dict, orient='index')
    df.columns = [ "count"]
    df.to_csv(output_tsv_name, sep= "\t" )


if __name__ == '__main__':
    brite_file = sys.argv[1]
    letter = sys.argv[2]
    output_tsv_name =sys.argv[3]
    brite_parse(brite_file, letter, output_tsv_name)
