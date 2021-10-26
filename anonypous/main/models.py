from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import CharField
# Create your models here.

class documentcode(models.Model):
    code = models.CharField(max_length=16)

    def __str__(self):
        return f'''{self.code}'''

class profile(models.Model):
    email = models.EmailField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, default='')
    lastname = models.CharField(max_length=30, default='')
    bio = models.TextField(default='no bio...')

    #true = teacher account, false = student account
    teacher = models.BooleanField(default=False)
    submissions = models.ManyToManyField(documentcode, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''{self.email}'''


class doc(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=PROTECT, default='')
    code = models.OneToOneField(documentcode, on_delete=CASCADE, default='')

    text = models.TextField(default='File Text')
    submissionDate = models.DateTimeField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''Doc - {self.code}'''


class assignmentcode(models.Model):
    code = models.CharField(max_length=17)

    def __str__(self):
        return f'''{self.code}'''

class assignmentObj(models.Model):
    name = models.CharField(max_length=30)

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    ownerstr = models.CharField(max_length=30, default='')

    code = models.OneToOneField(assignmentcode, on_delete=models.CASCADE, default='')
    codestr = models.CharField(max_length=30, default='')
    pointValue = models.IntegerField(default='-1')
    dueDate = models.DateField(null=True, blank=True)

    submissions = models.ManyToManyField(doc, blank=True)
    instructions = models.TextField(default='Instructions')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'''{self.code}'''


class classcode(models.Model):
    code = models.CharField(max_length=6)

    def __str__(self):
        return f'''{self.code}'''

class classes(models.Model):
    name = models.CharField(max_length=30)

    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    ownerstr = models.CharField(max_length=30, default='')
    description = models.TextField(default='Description')
    code = models.OneToOneField(classcode, on_delete=CASCADE)
    codestr = models.CharField(max_length=6, default='')

    students = models.ManyToManyField(profile, blank=True)
    assignments = models.ManyToManyField(assignmentObj, blank=True)
    subject = models.CharField(max_length=10, default='')
    color = models.CharField(default='', max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'''{self.code}'''

