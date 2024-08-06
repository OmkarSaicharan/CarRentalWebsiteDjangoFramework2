from django.contrib import admin
from django.urls import include, path
from MyCarRental import views

urlpatterns = [
    path('', views.index, name='home')

]
 