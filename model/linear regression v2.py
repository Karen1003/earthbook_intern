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
file1=input('日照檔名：')
df1=pd.read_excel(file1,usecols=['日照計'], dtype={'日照計':float},header=1)
file2=input('溫度檔名：')
df2=pd.read_excel(file2, usecols=['溫度計'], dtype={'溫度計':float},header=1)

X=pd.concat([df1,df2],axis=1)
prediction=model.predict(X)
#print(prediction)

'''
import openpyxl
workbook = openpyxl.Workbook()
sheet = workbook.worksheets[0]
#s3 = workbook.create_sheet('工作表3') 

for i in range(0,len(prediction)):
    for j in range(0,len(prediction[i])):
        output = pd.DataFrame({'column1': prediction[i][j], 'column2': prediction[i][j]})

  
workbook.save('test.xlsx')
'''


#output = pd.DataFrame({'column1': prediction[0], 'column2': prediction[1]})



output = pd.DataFrame({'三期_17-18:17:805:mppt1_power:315':prediction[:,0], '三期_17-18:17:805:mppt2_power:315': prediction[:,1], '三期_17-18:17:805:mppt3_power:315': prediction[:,2], '三期_17-18:17:805:mppt4_power:315': prediction[:,3], '三期_17-18:17:805:mppt5_power:315': prediction[:,4], '三期_17-18:17:805:mppt6_power:315': prediction[:,5],'三期_17-18:18:806:mppt1_power:135': prediction[:,6],'三期_17-18:18:806:mppt2_power:135':prediction[:,7],
                       '三期_17-18:18:806:mppt3_power:135':prediction[:,8],'三期_17-18:18:806:mppt4_power:135':prediction[:,9],'三期_17-18:18:806:mppt5_power:135':prediction[:,10],'三期_17-18:18:806:mppt6_power:135':prediction[:,11],'三期_19-20:19:807:mppt1_power:135':prediction[:,12],'三期_19-20:19:807:mppt2_power:135':prediction[:,13],'三期_19-20:19:807:mppt3_power:135':prediction[:,14],'三期_19-20:19:807:mppt4_power:315':prediction[:,15],
                       '三期_19-20:19:807:mppt5_power:315':prediction[:,16],'三期_19-20:19:807:mppt6_power:315':prediction[:,17],'三期_19-20:20:808:mppt1_power:315':prediction[:,18],'三期_19-20:20:808:mppt2_power:315':prediction[:,19],'三期_19-20:20:808:mppt3_power:315':prediction[:,20],'三期_19-20:20:808:mppt4_power:135':prediction[:,21],'三期_19-20:20:808:mppt5_power:135':prediction[:,22],'三期_19-20:20:808:mppt6_power:135':prediction[:,23],
                       '三期_19-20:21:809:mppt1_power:135':prediction[:,24],'三期_19-20:21:809:mppt2_power:135':prediction[:,25],'三期_19-20:21:809:mppt3_power:315':prediction[:,26],'三期_19-20:21:809:mppt4_power:315':prediction[:,27],'三期_19-20:21:809:mppt5_power:135':prediction[:,28],'三期_19-20:21:809:mppt6_power:135':prediction[:,29],'三期_19-20:22:810:mppt1_power:135':prediction[:,30],'三期_19-20:22:810:mppt2_power:315':prediction[:,31],
                       '三期_19-20:22:810:mppt3_power:135':prediction[:,32],'三期_19-20:22:810:mppt4_power:315':prediction[:,33],'三期_19-20:22:810:mppt5_power:315':prediction[:,34],'三期_19-20:22:810:mppt6_power:315':prediction[:,35],'三期_19-20:23:811:mppt1_power:135':prediction[:,36],'三期_19-20:23:811:mppt2_power:135':prediction[:,37],'三期_19-20:23:811:mppt3_power:315':prediction[:,38],'三期_19-20:23:811:mppt4_power:315':prediction[:,39],
                       '三期_19-20:23:811:mppt5_power:135':prediction[:,40],'三期_19-20:23:811:mppt6_power:315':prediction[:,41]})

output.to_csv('test.csv',encoding="utf_8_sig",index=False)


print("Your submission was successfully saved!")