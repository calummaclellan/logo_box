from django.contrib import admin
from logoBox.models import Post, UserProfile, Rating

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category',)}

admin.site.register(Rating)
admin.site.register(Post)
admin.site.register(UserProfile)

