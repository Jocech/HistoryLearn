from django.db import models

# Create your models here.
class Singup(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.IntegerField()
    age = models.IntegerField()
    password = models.CharField(max_length=20)

class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)

class User(models.Model):
    nickname = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    avatar = models.CharField(max_length=50) #En este campo se colocara el src="" de la ubicacion de la imagen 
    points = models.IntegerField()
    bag = models.CharField(max_length=60)#Este campo deberia ser una instancia de clase o variable de clase Inventary

class Player(models.Model):
    nickname = models.CharField(max_length=30)
    points = models.IntegerField()
    level = models.IntegerField()
    difficulty = models.IntegerField()

class Game(models.Model):
    pic_game = models.CharField(max_length=50)#Se colocara el src de origen de la imagen
    level = models.IntegerField()
    difficulty = models.IntegerField()
    answer = models.BooleanField()
    question = models.BooleanField()

class Ranking(models.Model):
    nickname = models.CharField(max_length=30)
    points = models.IntegerField()
    level = models.IntegerField()
    difficulty = models.IntegerField()

class Inventary(models.Model):
    avatar = models.CharField(max_length=50)#Se colocara el src de la imagen
    border = models.CharField(max_length=50)#Se colocara el src de la imagen
    background = models.CharField(max_length=50)#Se colocara el style del background

class Store(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=30)
    price = models.IntegerField()
    points = models.IntegerField()
    bag = models.CharField(max_length=60)#Este campo deberia ser una instancia de clase o variable de clase Inventary