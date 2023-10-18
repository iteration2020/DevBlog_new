from django.urls import path
from .views import input_data, prediction

urlpatterns = [
    path('input/', input_data, name='input_data'),
    path('prediction/<str:current_datetime>/', prediction, name='prediction'),
]
