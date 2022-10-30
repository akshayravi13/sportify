from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Athlete(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    sport = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
   
    def __str__(self):
        return self.f_name

class Sponsor(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    image=models.ImageField(upload_to='images')
    offer=models.CharField(max_length=20)
  
    def __str__(self):
        return self.name

    

