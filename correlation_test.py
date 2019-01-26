import click
import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr

def correlation_test():
    df = pd.read_csv("correlation_poly_flava_2.csv", index_col= 0)
    df.corr(method='spearman')

if __name__ == '__main__':
      correlation_test()
