__author__ = '0701052m'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logo_box.settings')

import django
django.setup()

from logoBox.models import Post, UserProfile, Rating


def populate():
    add_post(id=333,content='populate one',poster_id='admin')
    add_post(id=334,content='populate one',poster_id='admin')
    add_post(id=335,content='populate one',poster_id='admin')
    add_post(id=336,content='populate one',poster_id='admin')
    add_post(id=337,content='populate one',poster_id='admin')
    add_post(id=338,content='populate one',poster_id='admin')
    add_post(id=339,content='populate one',poster_id='admin')
    add_post(id=330,content='populate one',poster_id='admin')
    add_post(id=331,content='populate one',poster_id='admin')
    add_post(id=332,content='populate one',poster_id='admin')
    add_post(id=322,content='populate one',poster_id='admin')


#def add_user(user, password):
#    u = UserProfile.objects.get_or_create(user=user, password=password)[0]
#    u.save()
#    return u

def add_post(id,content,poster_id):
    p = Post.objects.get_or_create(id=id,content=content,poster_id=poster_id)[0]
    p.save()
    return p

# Start execution here!
if __name__ == '__main__':
    print "Starting logoBox population script..."
    populate()