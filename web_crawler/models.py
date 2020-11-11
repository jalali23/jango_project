from django.db import models

# Create your models here.
class Courses(models.Model):
    title=models.CharField(max_length=200)
    teacher=models.CharField(max_length=200,blank=True,null=True)
    price=models.CharField(max_length=200,blank=True,null=True)
    category = models.CharField(max_length=128)
    time=models.CharField(max_length=200,blank=True,null=True)
    image=models.CharField(max_length=200)
    Url=models.URLField()

    def __str__(self):
        return self.title
    

class Articles(models.Model):
    title = models.CharField(max_length=200)
    Url = models.URLField()
    def __str__(self):
        return self.title
