from django.db import models

# Create your models here.
class user (models.Model):
    name = models.TextField()
    password  = models.TextField()

class Todo(models.Model):
    summary = models.CharField(max_length=70)
    description = models.CharField()
    TIme = models.TimeField()
    iscomplete = models.BooleanField( default= False)


