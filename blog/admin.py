from django.contrib import admin
from .models import Post
from .models import PostImage

admin.site.register(Post)
admin.site.register(PostImage)
