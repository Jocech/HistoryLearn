from django.db import models
from apps.signup.models import User
# Create your models here.

class Answer(models.Model):
    id_answer = models.CharField(max_length=20,primary_key=True)
    text = models.TextField()
    correct = models.BooleanField()

class Game(models.Model):
    id_game = models.CharField(max_length=50,primary_key=True)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING)
    answer = models.ForeignKey(Answer,null=True,blank=True,on_delete=models.DO_NOTHING)#falta por terminar

class Question(models.Model):
    id_question = models.CharField(max_length=80,primary_key=True)
    image = models.CharField(max_length=80)
    text = models.TextField()
    answer = models.ForeignKey(Answer,null=True,blank=True,on_delete=models.DO_NOTHING)
    