from django.db import models
class registration(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=50)

# Create your models here.
