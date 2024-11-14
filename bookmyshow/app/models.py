from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.TextField()
    date=models.DateField()
    lang=models.TextField()
    img=models.FileField()


