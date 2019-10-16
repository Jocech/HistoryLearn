from django.db import models

# Create your models here.


class User(models.Model):
    nickname = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    date_born = models.DateTimeField(auto_now=False,auto_now_add=False)
    phone = models.CharField(max_length=30)
    points = models.IntegerField()

class Difficulty(models.Model):
    name = models.CharField(max_length=30)
    active = models.BooleanField()

class Picture(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

class Background(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

class Border(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

class Question(models.Model):
    image = models.CharField(max_length=80)
    text = models.TextField()
    value_level = models.IntegerField() #value of the level
    value_difficulty = models.IntegerField() #value for the difficulty in the game
    value_points = models.IntegerField() #player points when initialize the game
    value_discount = models.IntegerField() #points that are discount from value_points
    id_user = models.ForeignKey(User,null=True,blank = True, on_delete=models.DO_NOTHING)   

class Answer(models.Model):
    text = models.TextField()
    correct = models.BooleanField() #if 1=correct answer | if 0=incorrect answer
    id_question = models.ForeignKey(Question,null=True,blank = True, on_delete=models.DO_NOTHING)

class Userpic(models.Model):
    picture = models.ForeignKey(Picture, null=True,blank=True, on_delete=models.DO_NOTHING) #id_picture
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING) #nickname

class Userbackground(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING) #id_picture
    background = models.ForeignKey(Background,null=True,blank=True,on_delete=models.DO_NOTHING) #nickname

class Userborder(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING) #id_picture
    border = models.ForeignKey(Border,null=True,blank=True,on_delete=models.DO_NOTHING) #nickname
