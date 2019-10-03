from django.db import models
from apps.signup.models import User
# Create your models here.
class Picture(models.Model):
    id_picture = models.CharField(max_length=80, primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()

class Background(models.Model):
    id_background = models.CharField(max_length=80,primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()

class Border(models.Model):
    id_border = models.CharField(max_length=80,primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()


class Userpic(models.Model):
    id_userpic = models.CharField(max_length=40, primary_key=True)
    picture = models.ForeignKey(Picture, null=True,blank=True, on_delete=models.DO_NOTHING) #id_picture
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING) #nickname

class Userbackground(models.Model):
    id_userback = models.CharField(max_length=40,primary_key=True)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING) #id_picture
    background = models.ForeignKey(Picture,null=True,blank=True,on_delete=models.DO_NOTHING) #nickname

class Userborder(models.Model):
    id_userborder = models.CharField(max_length=40,primary_key=True)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING) #id_picture
    border = models.ForeignKey(Border,null=True,blank=True,on_delete=models.DO_NOTHING) #nickname

