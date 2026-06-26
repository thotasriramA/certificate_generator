from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    mobile = models.CharField(max_length=15)

    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Chat(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Message(models.Model):

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    sender = models.CharField(max_length=10)

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender
class LikeAndComment(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    liked = models.BooleanField(default=True)

    comment = models.TextField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    