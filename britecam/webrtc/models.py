from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Consumer(models.Model):
    user = models.ManyToManyField(User)
    name=models.CharField(max_length=200)
    contact=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    

class Uploaded_file(models.Model):
    file_name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User)
    timestamp = models.DateTimeField('file uploaded')
    docfile = models.FileField(upload_to = 'documents/%Y/%m/%d')
    Rating = models.CharField(max_length = 1)
    Notes = models.CharField(max_length=200)
# Create your models here.
