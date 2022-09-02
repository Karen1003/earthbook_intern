# coding: utf8
"""
Created on Thu Sep  1 09:58:34 2022

@author: Karen
"""
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import joblib
import pandas as pd
model=joblib.load('linear regression_135.pkl')
file=input('請輸入檔名')
df=pd.read_csv(file)
prediction=model.predict(df)
print(prediction)

