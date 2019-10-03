from django.db import models
from apps.signup.models import User
# Create your models here.

class Answer(models.Model):
    id_answer = models.CharField(max_length=20,primary_key=True)
    text = models.TextField()
    correct = models.BooleanField() #if 1=correct answer | if 0=incorrect answer

class Game(models.Model):
    id_game = models.CharField(max_length=50,primary_key=True)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING) #nickname
    answer = models.ForeignKey(Answer,null=True,blank=True,on_delete=models.DO_NOTHING ) #id_question
    points_earned = models.IntegerField()

class Question(models.Model):
    id_question = models.CharField(max_length=80,primary_key=True)
    image = models.CharField(max_length=80)
    text = models.TextField()
    answer = models.ForeignKey(Answer,null=True,blank=True,on_delete=models.DO_NOTHING) #id_answer
    value_level = models.IntegerField() #value of the level
    value_difficulty = models.IntegerField() #value for the difficulty in the game
    value_points = models.IntegerField() #player points when initialize the game
    value_discount = models.IntegerField() #points that are discount from value_points

class Difficulty(models.Model):
    id_difficulty = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=30)
    active = models.BooleanField()