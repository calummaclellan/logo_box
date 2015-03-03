from django.db import models
import time
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(unique = True)
    category = models.CharField(max_length = 64)
    content = models.CharField(max_length = 256)
    likes = models.IntegerField(default =0)
    dislikes = models.IntegerField(default = 0)
    timeCreated = time.time()
    lastActive = time.localtime(timeCreated)
    poster_id = models.CharField(max_length = 64)




class User(models.User):
    email= models.CharField(unique=True, max_length = 64, min_length = 8)
   # password = models.
    username = models.CharField( max_length = 64, min_length = 3)