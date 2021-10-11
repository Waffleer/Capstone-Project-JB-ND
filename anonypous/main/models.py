from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT
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

class documentcode(models.Model):
    code = models.CharField(max_length=16)

    def __str__(self):
        return f'''{self.code}'''

class doc(models.Model):
    name = models.CharField(max_length=30)
    owner = models.OneToOneField(User, on_delete=PROTECT, default='')
    code = models.OneToOneField(documentcode, on_delete=CASCADE, default='')

    text = models.TextField(default='File Text')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''Session Name - {self.name}'''


class assignment(models.Model):
    name = models.CharField(max_length=30)

    owner = models.OneToOneField(User, on_delete=models.PROTECT, default='')
    text = models.TextField(default='Description')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'''Session Name - {self.name}'''

class classcode(models.Model):
    code = models.CharField(max_length=6)

    def __str__(self):
        return f'''{self.code}'''

class classes(models.Model):
    name = models.CharField(max_length=30)

    owner = models.OneToOneField(User, on_delete=models.PROTECT, default='')
    discription = models.TextField(default='Description')
    code = models.OneToOneField(classcode, on_delete=CASCADE, default='')

    students = models.ForeignKey(profile, on_delete=PROTECT, default='')
    assignments = models.ForeignKey(assignment, on_delete=PROTECT, default='')

    color = models.IntegerField(default=-1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''Session Name - {self.name}'''

