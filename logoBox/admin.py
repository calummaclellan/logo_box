from django.contrib import admin
from logoBox.models import Post, UserProfile, Rating

admin.site.register(Rating)
admin.site.register(Post)
admin.site.register(UserProfile)

