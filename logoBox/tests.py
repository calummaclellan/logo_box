from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from logoBox.models import Post


#we don't really know how to write these.

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(id=1 ,content='test content 1',poster_id='old_MacTesty',likes=11,dislikes=99, category = 'testCase1')
        Post.objects.create(id=2, content='test content 2',poster_id='old_MacTestys_Brother',likes=110,dislikes=99, category = 'testCase2')

    def test_get_post_by_category(self):
        #testing if we can find a post by its category tag
        posts = Post.objects.all()
        self.assertEqual()



# Create your tests here.
