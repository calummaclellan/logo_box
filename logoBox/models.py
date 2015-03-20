from django.db import models
import datetime, time
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

class Post(models.Model):
    poster_id= models.CharField(max_length = 64,default='1')
    category = models.CharField(max_length = 64, default='')
    content = models.CharField(max_length = 256)
    likes = models.IntegerField(default =0)
    dislikes = models.IntegerField(default = 0)
    timeCreated = models.DateTimeField(auto_now_add=True)
    lastActive = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='poster_images', blank=True)
    #poster_id= models.CharField(max_length = 64)
    #poster_id = models.ForeignKey(UserProfile)

    class Meta:
      get_latest_by = 'timeCreated'

    def __unicode__(self):
        return self.poster_id

class Rating(models.Model):
    post_id_rate = models.CharField(max_length = 64,default='1')
    poster_id_rate = models.CharField(max_length = 64,default='1')
    #post_id_rate = models.ForeignKey(Post, db_index = False)
    #poster_id_rate = models.ForeignKey(UserProfile, db_index = False)

    def __unicode__(self):
        return self.post_id_rate