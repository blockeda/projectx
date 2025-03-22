import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
df=pd.read_csv("vacancies_2024.csv")
kk=['Разработчик','Backend-developer','Backend-разработчик']
print(df)
kk='|'.join(kk)
filtered_df = df[df['name'].str.contains(kk)]
file_name = 'Data.xlsx'

filtered_df.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')

