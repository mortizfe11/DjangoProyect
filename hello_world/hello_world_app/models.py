from django.db import models
import uuid, datetime

# Create your models here.

def get_time_today():
    return datetime.date.today()

def generate_slug_hash():
    return str(uuid.uuid1())[:8]

class Member(models.Model):
    #id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255) #campo de texto. 
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True)
    joined_date = models.DateField(default=get_time_today, null=True)
    slugh_hash = models.CharField(max_length=8,default=generate_slug_hash, null=False)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"