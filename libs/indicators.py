import pandas as pd
import numpy as np


def add_simple_moving_average(df, period_in_days, col_name=''):
    # df['SMA_'+str(period_in_days)+'_D'] = df.iloc[:,1].rolling(window=period_in_days).mean()
    df['SMA_'+str(period_in_days)+'_D'] = df[col_name].rolling(window=period_in_days).mean()