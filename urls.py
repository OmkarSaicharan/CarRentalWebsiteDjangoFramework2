from django.contrib import admin
from django.urls import path, include

from MyCarRental import views
from ..car.views import registered  

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
    path('admin/', admin.site.urls),  # This line seems to be redundant
    path('', views.index, name="index"),  # Assuming 'views' is imported correctly
    path('registered', registered, name='registered')  # Assuming 'registered' is imported correctly
]
