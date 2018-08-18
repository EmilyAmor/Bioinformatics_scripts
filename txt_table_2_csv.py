#!/usr/bin/python3

import click
import pandas as pd

@click.command()
@click.argument('txt_table')
@click.argument('user_defined_csv_name')
def txt_table_2_csv(txt_table, user_defined_csv_name):
    """ converts table.txt to table.csv"""
    table = pd.read_csv(txt_table, sep='\s+',header=None)
    df = pd.DataFrame(table)
    csv = pd.DataFrame.to_csv(df, header=False, index=False)
    file = open(user_defined_csv_name, "w")
    file.write(csv)
    file.close()

if __name__ == '__main__':
      txt_table_2_csv()
