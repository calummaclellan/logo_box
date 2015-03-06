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
    id = models.IntegerField(unique = True, primary_key=True)
    category = models.CharField(max_length = 64, default='')
    content = models.CharField(max_length = 256)
    likes = models.IntegerField(default =0)
    dislikes = models.IntegerField(default = 0)
    timeCreated = models.DateTimeField()
    lastActive = models.DateTimeField()
    poster_id = models.ForeignKey(UserProfile, unique = True)

    def __unicode__(self):
        return self.id