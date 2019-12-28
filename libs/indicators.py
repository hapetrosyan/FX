import pandas as pd
import numpy as np


def simple_moving_average(df, period):
    df['SMA'] = df.iloc[:,1].rolling(window=period).mean()
    return df