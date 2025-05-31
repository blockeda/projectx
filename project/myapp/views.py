import os
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))

def geography(request):
    tables_data = []
    csv_dir = os.path.join(current_dir, 'csv')
    for filename in os.listdir(csv_dir):
        if filename.startswith('Топ-10 городов по вакансиям в ') and filename.endswith('.csv'):
            year = filename.split(' в ')[1].split(' году.csv')[0]
            filepath=os.path.join(csv_dir,filename)
            df=pd.read_csv(filepath, encoding='utf-8')
            tables_data.append({
                'year':year,
                'title': f'Топ-10 городов по вакансиям в {year} году',
                'html_table': df.to_html(
                    classes='table table-striped table-hover',
                    index=False,
                    border=0
                )
            })


    return render(request, 'geo.html',{'tables': tables_data})

def salary(request):
    file_path = os.path.join(current_dir, 'csv', 'salary.csv')
    df = pd.read_csv(file_path)
    datafram = df.to_html(classes='table table-striped', index=False)
    return render(request, 'sal.html', {'datafr': datafram})

def home_page(request):

    return render(request, 'index.html')

def basez(request):

    return render(request, 'base.html')

def skills(request):
    file_path = os.path.join(current_dir,'csv' , 'skills.csv')
    df = pd.read_csv(file_path)
    datafram=df.to_html(classes='table table-striped', index=False)
    return render(request,'skills.html',{'datafr':datafram})

