from django.urls import path
from django.contrib import admin

from . import views

app_name = 'cadastro'
urlpatterns = [
    path('baixar-dados/', views.get_data, name='baixar-dados'),
    path('', views.index, name='index'),
]