# -*- coding: utf-8 -*-
"""
yimingxiao
"""
import numpy as np
from scipy import stats
import pandas as pd
from sklearn.metrics import mean_squared_error
def eval(csv):
    df = pd.read_csv(csv)
    mos = df['mos']
    mos_pred = df['mos_pred']
    pccs = np.corrcoef(mos, mos_pred)[0][1]
    rmse  = np.sqrt(mean_squared_error(mos, mos_pred))
    SROCC = stats.spearmanr(mos_pred, mos)[0]
    print(pccs)
    print(SROCC)
    print(rmse)

if __name__=='__main__':
    eval('test.csv')