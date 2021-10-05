from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db.models.enums import Choices

permissions = (
    ('t', 'Teacher'),
    ('s', 'Students')
)

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='no bio...')

    avatar = models.ImageField(upload_to='avatars', default='no_picture')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''Profile - {self.user.username}'''

class student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='no bio...')

    avatar = models.ImageField(upload_to='avatars', default='no_picture')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''Profile - {self.user.username}'''

class teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='no bio...')

    avatar = models.ImageField(upload_to='avatars', default='no_picture')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''Profile - {self.user.username}'''
