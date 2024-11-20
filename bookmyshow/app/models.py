from django.db import models

# Create your models here.

class movie(models.Model):
    name=models.TextField()
    date=models.DateField()
    language=models.TextField()
    img=models.FileField()