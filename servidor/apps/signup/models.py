from django.db import models

# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=25,primary_key=True)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    date_born = models.DateTimeField(auto_now=False,auto_now_add=False)
    phone = models.CharField(max_length=30)
    points = models.IntegerField()
 