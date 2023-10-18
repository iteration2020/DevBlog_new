from django.shortcuts import render, redirect
from .forms import InputDataForm
from .models import InputData
import joblib
import pymysql
from datetime import datetime
from DevBlog_new.settings import DATABASES

# Словарь соответствия
SEX_MAPPING = {'M': 1, 'F': 2}
BP_MAPPING = {'L': 1, 'N': 2, 'H': 3}
CHOLESTEROL_MAPPING = {'L': 1, 'N': 2, 'H': 3}
DRUG_SCHEMAS = {1: 'DrugY', 2: 'drugC', 3: 'drugX', 4: 'drugA'}
#Коннект БД и курсор
database_settings = DATABASES['default']
host = database_settings['HOST']
user = database_settings['USER']
password = database_settings['PASSWORD']
database = database_settings['NAME']
connection = pymysql.connect(host=host, user=user, password=password, db=database)
cursor = connection.cursor()
def input_data(request):
    if request.method == 'POST':
        form = InputDataForm(request.POST)
        if form.is_valid():
            current_datetime = datetime.now()
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            bp = form.cleaned_data['bp']
            cholesterol = form.cleaned_data['cholesterol']
            na_to_k = form.cleaned_data['na_to_k']
            sex = SEX_MAPPING.get(sex)
            bp = BP_MAPPING.get(bp)
            cholesterol = CHOLESTEROL_MAPPING.get(cholesterol)
            query = "INSERT INTO predict_input (Age,Cholesterol,BP,Sex, Na_to_K, datestamp) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (age, cholesterol, bp, sex, na_to_k, current_datetime))
            connection.commit()
            return redirect('prediction',current_datetime)
    else:
        form = InputDataForm()
    return render(request, 'predict/input_data.html', {'form': form})


def prediction(request,current_datetime):
    current_datetime = datetime.strptime(current_datetime, "%Y-%m-%d %H:%M:%S.%f")
    model = joblib.load('web/predict/model.pkl')
    query = "SELECT Age,Cholesterol,BP,Sex, Na_to_K FROM predict_input WHERE datestamp = %s"
    cursor.execute(query, current_datetime)
    result = cursor.fetchone()
    age, sex, bp, cholesterol, na_to_k = result
    data = [[age, sex, bp, cholesterol, na_to_k]]
    predict = model.predict(data)
    query = "UPDATE predict_input SET Result = %s WHERE datestamp = %s"
    cursor.execute(query, (predict, current_datetime))
    connection.commit()
    predict = DRUG_SCHEMAS.get(predict)
    request.session['predict'] = predict
    return render(request, 'predict/prediction.html', predict)