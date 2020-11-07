from django.db import models

# Create your models here.
class Courses(models.Model):
    title=models.CharField(max_length=200)
    teacher=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    time=models.DateField(max_length=200)
    imageUrl=models.CharField(max_length=200)
    Url=models.URLField()

class Articles(models.Model):
    title = models.CharField(max_length=200)
    Url = models.URLField()

