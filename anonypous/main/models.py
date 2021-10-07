from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db.models.enums import Choices



class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='no bio...')

    avatar = models.ImageField(upload_to='avatars', default='no_picture')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''Profile - {self.user.username}'''

class classes(models.Model):
    name = models.CharField(max_length=30)

    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    discription = models.TextField(default='Description')
    avatar = models.ImageField(upload_to='sessionicon', default='no_picture')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''Session Name - {self.name}'''

class assignment(models.Model):
    name = models.CharField(max_length=30)

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    classes = models.OneToOneField(classes, on_delete=models.CASCADE)

    text = models.TextField(default='Description')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'''Session Name - {self.name}'''


class doc(models.Model):
    name = models.CharField(max_length=30)

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    classes = models.OneToOneField(classes, on_delete=models.CASCADE)
    assignment = models.OneToOneField(assignment, on_delete=models.CASCADE)

    text = models.TextField(default='Description')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''Session Name - {self.name}'''