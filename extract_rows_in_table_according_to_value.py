import click
import pandas as pd

@click.command()
@click.argument('busco.csv')

def remove_dups_from_busco(busco.csv):
