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
    #category = forms.CharField(widget=forms.HiddenInput() ,max_length = 64,)
    content = forms.CharField(max_length = 256, help_text="Add Content here:")
    #likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    #dislikes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    timeCreated = forms.DateTimeField(widget=forms.HiddenInput())
    lastActive = forms.DateTimeField(widget=forms.HiddenInput())
    #poster_id = forms.ForeignKey(UserProfile, widget=forms.HiddenInput(),unique = True)

    class Meta:
        model = Post
        fields = ['content','timeCreated','lastActive']