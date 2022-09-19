# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:25:46 2022

@author: ACER
"""

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import joblib
import pandas as pd
model=joblib.load('linear regression_all.pkl')
file=input('請輸入檔名')
df=pd.read_csv(file)
prediction=model.predict(df)
print(prediction)
