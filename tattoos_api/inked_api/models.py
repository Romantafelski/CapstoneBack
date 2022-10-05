from django.db import models

# Create your models here.

class Tattoo(models.Model):
    image = models.CharField(max_length=3000)
    artist = models.CharField(max_length=100)
    description = models.CharField(max_length=999)
    
    
class Admin(models.Model): 
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=55)