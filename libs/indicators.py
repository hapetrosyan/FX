import pandas as pd
import numpy as np


def simple_moving_average(df_inp, period):
    df_out = df_inp
    df_out['SMA'] = df_out.iloc[:,1].rolling(window=period).mean()
    return df_out