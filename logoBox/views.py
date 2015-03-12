from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from logoBox.forms import PostForm
from logoBox.models import Post
import time

def index(request):
    posts = Post.objects.all()
    context_dict = {'posts': posts}
    return render(request, 'logoBox/index.html',context_dict)

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

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/logoBox/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your logoBox account is disabled. You swine.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'logoBox/login.html', {})



def user_logout(request):

    logout(request)

    return render(request,'logoBox/index.html')

def create_post(request):

    if request.method == 'POST':

        form = PostForm(request.POST)
        #user = request.user

        #check user authenticate request user
        poster = request.user.username
        if form.is_valid():

            post = form.save(commit=False)
            post.poster_id = poster

            post.save()
            return render(request,'logoBox/index.html')

        else:
            print "THERE BE ERRORS"
            print form.errors

    else:
        form = PostForm()

    return render(request, 'logoBox/post.html',{'form':form})