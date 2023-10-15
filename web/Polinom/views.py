from django.shortcuts import render
from polynom import train_model

def train_model_view(request):
    if request.method == 'POST':
        # Вызов функции обучения модели из вашего файла Python
        train_model()
        return render(request, 'success.html')
    return render(request, 'polynom.html')