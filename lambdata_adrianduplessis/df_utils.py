import numpy as np
import pandas as pd

ONES = pd.Series(np.ones(20))
ZEROS = pd.Series(np.zeros(20))

def remove_observations_with_outliers(df, zscore=3):
    #Outlier removal
    from scipy import stats

    #Get subset within 'zscore' (default=3)  stdev
    df_cleaned = df[(np.abs(stats.zscore(
                        df.select_dtypes(
                            include=np.number))) < 2).all(axis=1)]

    return df_cleaned

def prove_that_this_even_works():
    return 'Proof.'
