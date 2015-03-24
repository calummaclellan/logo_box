from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from logoBox.models import Post
from django.test.client import RequestFactory

#we don't really know how to write these.

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(id=1 ,content='test content 1',poster_id='old_MacTesty',likes=11,dislikes=99, category = 'testCase1')
        Post.objects.create(id=2, content='test content 2',poster_id='old_MacTestys_Brother',likes=110,dislikes=99, category = 'testCase2')
        User.objects.create_user(username='testuser')
        self.client.login(username='testuser')

    def test_get_post_by_category(self):
        #testing if we can find a post by its category tag
        from logoBox.views import get_tagged
        self.factory=RequestFactory()
        request = self.factory.get('/logoBox/tag/testCase2')
        posts = Post.objects.all()
        print get_tagged(request,'testCase2')
        print posts
        self.assertEqual(get_tagged(request,'testCase2'),'testCase2 Content')

    def test_login(self):
        from logoBox.views import user_login
        self.factory=RequestFactory()
        request = self.factory.get('username')
        c= Client.get(Client())
        print c.get(user_login(request),{'username': 'testuser'})
        self.assertEqual(c.get(user_login(request),{'username'}),'testuser')

    def test_likes(self):
        from logoBox.views import like_post
        self.factory=RequestFactory()

        request = self.factory.get('/logoBox/tag/testCase2')
        post_id= 2
        self.assertEqual(like_post(request),110)


# Create your tests here.
