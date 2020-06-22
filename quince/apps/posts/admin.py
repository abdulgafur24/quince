from django.contrib import admin
from django.contrib.admin import site
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_body', 'post_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment_body')


site.register(Post, PostAdmin)
site.register(Comment, CommentAdmin)
