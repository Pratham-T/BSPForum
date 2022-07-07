from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Post, Comment

# Register your models here.
admin.site.register(Comment)

@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'content')
