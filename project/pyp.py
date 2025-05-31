import csv
import json
from http.client import responses

import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import requests

df=pd.read_csv("myapp/csv/vacancies_2024.csv")
kk=['Разработчик','Backend-developer','Backend-разработчик']
print(df)
kk='|'.join(kk)
filtered_df = df[df['name'].str.contains(kk)]
file_name = 'Data.xlsx'

filtered_df.to_excel(file_name)
print('DataFrame successfully.')

def currency_to_RUB(df: pd.DataFrame):
    response=requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    curr=json.loads(response.text)
    mask=df['salary_currency'] == 'RUB'
    for index, row in df.iterrows():
        if row['salary_currency'] == 'USD':
            print(row)

    # df.loc[mask ,'salary_from'] = df.loc[mask,'salary_from'] * float(curr['Valute'][df.loc[i,'salary_currency']]['Value'])
currency_to_RUB(df)