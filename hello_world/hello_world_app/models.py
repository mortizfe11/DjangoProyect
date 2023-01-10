from django.db import models

# Create your models here.

class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255) #campo de texto. 
    lastname = models.CharField(max_length=255)