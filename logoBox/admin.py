from django.contrib import admin
from logoBox.models import Post, UserProfile, Rating, Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category',)}

admin.site.register(Rating)
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Tag)
