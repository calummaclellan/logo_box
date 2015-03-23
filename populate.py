__author__ = '0701052m'

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logo_box.settings')

import django
django.setup()

from logoBox.models import Post, UserProfile, Rating


def populate():
    add_post(id=333,content='populate 1',poster_id='admin',likes=11,dislikes=99)
    add_post(id=334,content='populate 2',poster_id='admin',likes=12,dislikes=22)
    add_post(id=335,content='populate 3',poster_id='admin',likes=31,dislikes=16)
    add_post(id=336,content='populate 4',poster_id='admin',likes=15,dislikes=15)
    add_post(id=337,content='populate 5',poster_id='admin',likes=18,dislikes=11)
    add_post(id=338,content='populate 6',poster_id='admin',likes=54,dislikes=15)
    add_post(id=339,content='populate 7',poster_id='admin',likes=36,dislikes=13)
    add_post(id=330,content='populate 8',poster_id='admin',likes=67,dislikes=15)
    add_post(id=331,content='populate 9',poster_id='admin',likes=12,dislikes=19)
    add_post(id=332,content='populate 10',poster_id='admin',likes=99,dislikes=22)

    add_rate(post_id_rate=333,poster_id_rate='admin')
    add_rate(post_id_rate=334,poster_id_rate='admin')
    add_rate(post_id_rate=335,poster_id_rate='admin')
    add_rate(post_id_rate=336,poster_id_rate='admin')

#def add_user(user, password):
#    u = UserProfile.objects.get_or_create(user=user, password=password)[0]
#    u.save()
#    return u

def add_post(id,content,poster_id,likes,dislikes):
    p = Post.objects.get_or_create(id=id,content=content,poster_id=poster_id,likes=likes,dislikes=dislikes)[0]
    p.save()
    return p

def add_rate(post_id_rate,poster_id_rate):
    p = Rating.objects.get_or_create(post_id_rate=post_id_rate, poster_id_rate=poster_id_rate)[0]
    p.save()
    return p


# Start execution here!
if __name__ == '__main__':
    print "Starting logoBox population script..."
    populate()