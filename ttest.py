import click
import numpy as np
import pandas as pd
from scipy import stats

@click.command()
@click.argument('input_file')
@click.argument('correlation_test')

def ttest(input_file, correlation_test):
    df = pd.read_csv("test_allsamples_and_nanvalues.csv")
