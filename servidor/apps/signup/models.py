from django.db import models
from apps.game.models import Game,Difficulty
from apps.avatar.models import Userbackground,Userborder,Userpic
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
    game = models.ForeignKey(Game,null=True,blank=True,on_delete=models.DO_NOTHING) #id_game
    difficulty = models.ForeignKey(Difficulty,null=True,blank=True,on_delete=models.DO_NOTHING) #id_difficulty
    userbackground = models.ForeignKey(Userbackground,null=True,blank=True,on_delete=models.DO_NOTHING) #id_userback
    userpic = models.ForeignKey(Userpic,null=True,blank=True,on_delete=models.DO_NOTHING) #id_userpic
    userborder = models.ForeignKey(Userborder,null=True,blank=True,on_delete=models.DO_NOTHING) #id_userborder
 