from django.contrib import admin

from .models import Blog, BlogComment, BlogView, Like

admin.site.register(Blog)
admin.site.register(BlogComment)
admin.site.register(BlogView)
admin.site.register(Like)
