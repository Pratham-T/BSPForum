from django.db import models
from django.db.models.base import Model
from django.urls import reverse
# from django.conf import global_settings
import uuid
from django.contrib.auth.models import User
from datetime import date

from BSPForum import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, help_text='Post header')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pub_date = models.DateField(null=False)
    content = models.TextField(max_length=5000, help_text='Post body', null=True)
    images = models.ImageField(upload_to = settings.MEDIA_ROOT, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment = models.TextField(help_text='Comment body')