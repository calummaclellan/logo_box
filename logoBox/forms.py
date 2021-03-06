__author__ = '0701052m'

from django import forms
from django.contrib.auth.models import User
from logoBox.models import Post, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class PostForm(forms.ModelForm):

    #id = forms.IntegerField(widget=forms.HiddenInput())
    category = forms.CharField( max_length = 64, help_text= "Enter a tag here: ", required = False)
    content = forms.CharField(max_length = 500, help_text="Add Content here:", widget=forms.Textarea)
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=12)
    dislikes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    #timeCreated = forms.DateTimeField(widget=forms.HiddenInput())
    #lastActive = forms.DateTimeField(widget=forms.HiddenInput())
    poster_id= forms.CharField(widget=forms.HiddenInput(),max_length = 64, initial ='anonymous')
    picture = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['content','picture','category']
