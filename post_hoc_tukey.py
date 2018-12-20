#!/usr/bin/python3

import click
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

@click.command()
@click.argument('biochem_csv')



def post_hoc_tukey(biochem_csv):

    # user input parameters
    ignore_column1 = input("list the first column that must be ignored: ")
    ignore_column2 = input("list second column that must be ignored: ")
    column_flavonoid = input("what flavonoid group do you want to investigate? ")

    # read in data.csv file
    df = pd.read_csv(biochem_csv)
    df.drop(ignore_column1, axis= 1, inplace= True)
    df.drop(ignore_column2, axis= 1, inplace= True)

    # Tukey's HSD Post-hoc comparison
    mc = MultiComparison(df['polyphenols'], df['plant'])
    mc_results = mc.tukeyhsd()
    print(mc_results)
