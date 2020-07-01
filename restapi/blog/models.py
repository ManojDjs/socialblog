from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import generics
from datetime import datetime
from django.utils.timezone import timezone


# Create your models here.
class Blogpost(models.Model):
    head = models.CharField(max_length=150, default='manoj')
    body = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.head


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.text


class Messages(models.Model):
    sender = models.ForeignKey(User, to_field="username", related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE, related_name='receiver',
                                 null=True, blank=True)
    text = models.TextField()
    time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.text


class Posts(models.Model):
    author = models.ForeignKey(User, to_field='username', related_name='author', on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='\media')
    time = models.DateTimeField(default=datetime.now(), blank=True)
    # likes = models.IntegerField()
    def __str__(self):
        return self.text
