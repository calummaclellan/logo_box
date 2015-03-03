__author__ = '0701052m'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logo_box.settings')

import django
django.setup()

from logoBox.models import Post, UserProfile


def populate():
    add_user(user='Jim', password='jim1')




def add_user(user, password):
    u = UserProfile.objects.get_or_create(user=user, password=password)[0]
    u.save()
    return u

def add_post(id,content,timeCreated,poster_id):
    p = Post.objects.get_orcreate(id=id,content=content,poster_id=poster_id,timeCreated = timeCreated)[0]
    p.save()
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting logoBox population script..."
    populate()