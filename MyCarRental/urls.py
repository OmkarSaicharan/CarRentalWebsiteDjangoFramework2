"""
URL configuration for MyCarRental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from MyCarRental import views

# Define app-specific URL patterns
car_patterns = [
    path('', include('car.urls')),
]

bike_patterns = [
    path('', include('bike.urls')),
]

truck_patterns = [
    path('', include('truck.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include(car_patterns)),
    path('bike/', include(bike_patterns)),
    path('truck/', include(truck_patterns)),
    path('',views.index,name='index'),
    path('registered',views.registered,name='registered')
]