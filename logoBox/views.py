from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from logoBox.forms import PostForm
from logoBox.models import Post
from logoBox.models import Rating
import time

def index(request):
    most_liked_posts = Post.objects.order_by('-likes')[:8]
    most_hated_posts = Post.objects.order_by('-dislikes')[:7]
    #most_recent_posts = Post.objects.order_by('timeCreated').latest()[:5]
    ratings = Rating.objects.all()
    form = PostForm()
    context_dict = {'most_liked_posts': most_liked_posts, 'most_hated_posts':most_hated_posts, 'ratings': ratings, 'form': form,
                    }#'most_recent_posts':most_recent_posts}
    return render(request, 'logoBox/index.html', context_dict)

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None  no user with matching credentials was found.
        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect('/logoBox/')
            else:

                return HttpResponse("Your logoBox account is disabled. You swine.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'logoBox/login.html', {})



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/logoBox/')


def create_post(request):
    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)

        #user = request.user
        #check user authenticate request user
        poster = request.user.username
        if form.is_valid():

            post = form.save(commit=False)

            post.poster_id = poster


            if 'picture' in request.FILES:
                print "pic"
                post.picture = request.FILES['picture']

            post.save()
            return HttpResponseRedirect('/logoBox/')

        else:
            print "THERE BE ERRORS"
            print form.errors

    else:
        form = PostForm()

    return render(request, 'logoBox/index.html', {'form': form})


def like_post(request):

    post_id = None
    if request.method == 'GET':
        post_id = request.GET['post_id']

    likes = 0
    if post_id:
        post = Post.objects.get(id=int(post_id))
        ratings = Rating.objects.all()
        for rating in ratings:
            if rating.poster_id_rate == request.user.username and rating.post_id_rate == post_id:
                return
        if post:
            likes = post.likes+1
            post.likes = likes
            post.save()
            rate(post_id, request.user.username)
    return HttpResponse(likes)

def dislike_post(request):
    post_id = None
    if request.method == 'GET':
        post_id = request.GET['post_id']

    print post_id
    dislikes = 0
    if post_id:
        post = Post.objects.get(id=int(post_id))
        ratings = Rating.objects.all()
        for rating in ratings:
            if rating.poster_id_rate == request.user.username and rating.post_id_rate== post_id:
                return
        if post:
            dislikes = post.dislikes+1
            post.dislikes = dislikes
            post.save()
            rate(post_id, request.user)

    return HttpResponse(dislikes)

def rate(post_id, poster_id):

    r = Rating.objects.get_or_create(post_id_rate = post_id, poster_id_rate = poster_id)

    return

