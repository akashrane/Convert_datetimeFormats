# -*- coding: utf-8 -*-
"""Covert DateTimeformat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g0ZHpdGpA7yuUv01msDKO967NnN1mPYR
"""

import pandas as pd
import datetime

df = pd.read_csv('/content/Data_to_change_Time.csv')

def convert_timestamp(_time):
  try:
    dt = datetime.datetime.strptime(_time, "%Y-%m-%dT%H:%M:%SZ")
    formatted_timestamp = dt.strftime("%d-%m-%Y %H:%M:%S")
  except:
    print("Err")
    return formatted_timestamp

df['ConvertedTimestamp'] = df['_time'].apply(convert_timestamp)

# print(df)
df.to_excel('output.xlsx', index=False)