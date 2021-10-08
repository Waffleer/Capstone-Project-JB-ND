from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class profile(models.Model):
    email = models.EmailField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, default='')
    lastname = models.CharField(max_length=30, default='')
    bio = models.TextField(default='no bio...')

    #true = teacher account, false = student account
    teacher = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''Profile - {self.email}'''

class classes(models.Model):
    name = models.CharField(max_length=30)

    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    discription = models.TextField(default='Description')
    color = models.IntegerField(default=1)
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