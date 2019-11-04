import numpy as np
import pandas as pd

ONES = pd.Series(np.ones(20))
ZEROS = pd.Series(np.zeros(20))


def remove_observations_with_outliers(df, zscore=3):
    '''
    TODO
    '''
    # Outlier removal
    from scipy import stats

    # Get subset within 'zscore' (default=3)  stdev
    df_cleaned = df[(
        np.abs(stats.zscore(df.select_dtypes(include=np.number))) < 2).all(axis=1)]

    return df_cleaned


def prove_that_this_even_works():
    '''
    Returns a string 'Proof.' as confirmation that the package works.
    '''
    return 'Proof.'

class Section:
    def __init__(self, id, num_fields=0):
        self.id = id
        self.num_fields = num_fields

    def __repr_(self):
        return f'Section: {self.id}'
    
    def __str__(self):
        return f'This is section number {id}.'

    def add_field(self):
        self.num_fields += 1