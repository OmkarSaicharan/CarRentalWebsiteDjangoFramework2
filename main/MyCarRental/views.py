from django.http import HttpResponse
from django.shortcuts import render
from car.models import registration

def index(request):
    return render(request, 'index.html')

def registered(request):
    # Use get() method to retrieve form data, which returns None if the key is not found
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    if first_name and last_name and email and password:  # Check if all required fields are present
        person = registration(first_name=first_name, last_name=last_name, email=email, password=password)
        person.save()
        return render(request, 'car/registered.html', {'first_name': first_name})
    else:
        return HttpResponse("Registration sucessfully completed")
